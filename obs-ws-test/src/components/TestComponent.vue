<template>
  <div class="test-component">
    <div class="container">
      <div class="row">
        <div class="col-sm">
          <h2>Scenes</h2>
          <div
            v-for="(item, index) in sceneList"
            :key="`scene-${index}`"
          >
            <label>
              <input
                :id="`scene-${index}`"
                v-model="activeScene"
                type="radio"
                :value="`${item.name}`"
                @change="switchScenes($event.target.value)"
              >
              {{ `Scene${index}: ${item.name}` }}
            </label>
          </div>
        </div>
        <div class="col-sm mt-5">
          <label
            for="desktopVolumeSlider"
            class="form-label"
          >Desktop Volume Slider: {{ (1.0 * sourceDesktopAudioValue).toPrecision(2) }}</label>
          <input
            id="desktopVolumeSlider"
            v-model="sourceDesktopAudioValue"
            type="range"
            class="form-range"
            min="0"
            max="1"
            step="0.05"
            @change="setVolume($event.target.value)"
          >
        </div>
        <div class="col-sm mt-5">
          <button>Submit</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import OBSWebSocket from 'obs-websocket-js';
import amqp from 'amqplib/callback_api';

const obs = new OBSWebSocket();

export default {
  name: 'TestComponent',
  data() {
    return {
      sceneList: () => [],
      activeScene: '',
      activeSceneSourceList: [],
      sourceDesktopAudioName: 'Desktop Audio',
      sourceDesktopAudioValue: 0.6,
      obs,
      amqp,
      amqpConn: null,
      pubChannel: null,
      offlinePubQueue: () => [],
    };
  },
  created() {
    // Declare some events to listen for.
    this.obs.on('ConnectionOpened', () => {
      console.log('Websocket Connection Opened for Sneakbike Remote Controller.'); // eslint-disable-line no-console

      this.obs.send('GetSceneList').then((data) => {
        this.sceneList = data.scenes;
      });

      this.obs.send('GetCurrentScene').then((data) => {
        this.activeScene = data.name;
      });

      this.obs.send('GetVolume', { source: this.sourceDesktopAudioName }).then((data) => { this.sourceDesktopAudioValue = data.volume; });
    });

    this.obs.on('SwitchScenes', (data) => {
    // eslint-disable-next-line no-console
      console.log('SwitchScenes', data.sources.map((x) => x.name));
    });

    // this.obs.on('SourceVolumeChanged', (data) => console.log('Volume Changed', data));

    this.obs.connect();
    this.rabbitStart();

    setInterval(() => {
      this.rabbitPublish('', 'jobs', Buffer.from('work work work'));
    }, 1000);
  },
  methods: {
    switchScenes(sceneName) {
      console.log(`Scene name: ${sceneName}`); // eslint-disable-line no-console
      this.obs.send('SetCurrentScene', {
        'scene-name': sceneName,
      });
    },

    setVolume(value) {
      console.log(`Setting volume to value ${1.0 * value}`); // eslint-disable-line no-console
      this.obs.send('SetVolume', {
        source: this.sourceDesktopAudioName,
        volume: 1.0 * value,
      });
    },

    getPayload() {
      return {
        sourceDesktopAudioValue: this.sourceDesktopAudioValue,
        activeScene: this.activeScene,
      };
    },

    rabbitStart() {
      amqp.connect('amqp://localhost:15672', (err, conn) => {
        if (err) {
          // eslint-disable-next-line
          console.error('[AMQP]', err.message);
          return setTimeout(this.rabbitStart, 1000);
        }

        conn.on('error', (err1) => {
          if (err.message !== 'Connection closing') {
            // eslint-disable-next-line
            console.error('[AMQP] conn error', err1.message);
          }
        });
        conn.on('close', () => {
          // eslint-disable-next-line
          console.error('[AMQP] reconnecting');
          return setTimeout(this.rabbitStart, 1000);
        });

        // eslint-disable-next-line
        console.log('[AMQP] connected');
        this.amqpConn = conn;
        this.whenRabbitConnected();
        return 0;
      });
    },

    whenRabbitConnected() {
      this.startRabbitPublisher();
      this.startRabbitWorker();
    },

    startRabbitPublisher() {
      this.amqpConn.createConfirmChannel((err, ch) => {
        if (this.closeOnErr(err)) return;
        ch.on('error', (err1) => {
          // eslint-disable-next-line
          console.error('[AMQP] channel error', err1.message);
        });
        ch.on('close', () => {
        // eslint-disable-next-line
          console.log('[AMQP] channel closed');
        });

        this.pubChannel = ch;
        // eslint-disable-next-line
        while (true) {
          const [exchange, routingKey, content] = this.offlinePubQueue.shift();
          this.rabbitPublish(exchange, routingKey, content);
        }
      });
    },

    rabbitPublish(exchange, routingKey, content) {
      try {
        this.pubChannel.publish(exchange,
          // eslint-disable-next-line
          routingKey, content, { persistent: true }, (err, ok) => {
            if (err) {
              // eslint-disable-next-line
              console.error('[AMQP] publish', err);
              this.offlinePubQueue.push([exchange, routingKey, content]);
              this.pubChannel.connection.close();
            }
          });
      } catch (e) {
      // eslint-disable-next-line
        console.error('[AMQP] publish', e.message);
        this.offlinePubQueue.push([exchange, routingKey, content]);
      }
    },

    startRabbitWorker() {
      this.amqpConn.createChannel((err, ch) => {
        if (this.closeOnErr(err)) return;

        function processMsg(msg) {
          this.workRabbit(msg, (ok) => {
            try {
              if (ok) ch.ack(msg);
              else ch.reject(msg, true);
            } catch (e) {
              this.closeOnErr(e);
            }
          });
        }

        ch.on('error', (err2) => {
          // eslint-disable-next-line
          console.error('[AMQP] channel error', err2.message);
        });
        ch.on('close', () => {
          // eslint-disable-next-line
          console.log('[AMQP] channel closed');
        });
        ch.prefetch(10);
        // eslint-disable-next-line
        ch.assertQueue('jobs', { durable: true }, (err3, _ok) => {
          if (this.closeOnErr(err3)) return;
          ch.consume('jobs', processMsg, { noAck: false });
          // eslint-disable-next-line
          console.log('Worker is started');
        });
      });
    },
    workRabbit(msg, cb) {
      // eslint-disable-next-line
      console.log('Got msg', msg.content.toString());
      cb(true);
    },
    closeOnErr(err) {
      if (!err) return false;
      // eslint-disable-next-line
      console.error('[AMQP] error', err);
      this.amqpConn.close();
      return true;
    },

  },
};

</script>
<style scoped>
label {
  margin-left: 0.35rem;
}
</style>
