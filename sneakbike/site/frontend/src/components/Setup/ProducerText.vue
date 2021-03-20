<template>
  <div class="setup-producer-text">
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1>Producer Setup</h1>
          <div class="ml-6 mt-6">
            <h2>Sneakbike Basic Architecture</h2>
            <p>
              <b>User &#8594; RTMP Server &#8594; Producer &#8594; Twitch</b>
            </p>
            <p>
              Sneakbike has a producer use
              <a
                href="https://learn.hashicorp.com/collections/terraform/aws-get-started"
                target="_blank"
              >Terraform</a> to create an AWS-hosted
              <a
                href="https://en.wikipedia.org/wiki/Real-Time_Messaging_Protocol"
                target="_blank"
              >RTMP</a> server. Our racers broadcast their streams to this server and the producer pulls these streams down from the server using the VLC Plugin for OBS. This allows us to receive multiple streams and aggregate them onto one OBS instance.
            </p>
          </div>

          <div class="ml-6 mt-6">
            <h2>Building the Server</h2>

            <h3>Requirements</h3>
            <p>
              <info-card>
                Hosting a server on AWS
                <b>will cost real money.</b> Make sure to read about
                <a
                  href="https://aws.amazon.com/ec2/pricing/on-demand/"
                  target="_blank"
                >AWS EC2 pricing</a> for a
                <i>t3a.micro</i> instance.
              </info-card>
            </p>

            <ol class="pt-1 pb-4">
              <li class="pb-2">
                <b>[AWS]:</b> Complete
                <a
                  href="https://docs.aws.amazon.com/polly/latest/dg/setting-up.html"
                  target="_blank"
                >Step 1.1</a> here.
              </li>
              <li class="pb-2">
                <b>[AWS]:</b> Create an AWS Access Token by following
                <a
                  href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey"
                  target="_blank"
                >
                  the
                  <b>To Create, Modify, Or Delete Your Own IAM User Access Keys (Console)</b> section
                </a>. Download the credential file somewhere safe for backup.
              </li>
              <li class="pb-2">
                <b>[Windows]</b>: On your Windows Desktop, click on the Start menu and search for "Powershell". Right-click and "Run As Administrator.
              </li>

              <li class="pb-2">
                <b>[Powershell Admin]:</b>
                While in Powershell, install the
                <a
                  href="https://chocolatey.org/"
                  target="_blank"
                >Chocolatey package manager</a>:
                <prism language="powershell">
                  Set-ExecutionPolicy Bypass -Scope Process -Force;
                  [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
                  iex((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
                </prism>
              </li>
              <li class="pb-2">
                <b>[Powershell Admin]:</b> Close and re-open Admin Powershell like in the previous step. Install git, Terraform, VLC, and the AWS CLI:
                <prism language="powershell">choco install git vlc terraform awscli</prism>
              </li>
              <li class="pb-2">
                <b>[Powershell]:</b> Close and re-open Powershell
                <i>but not as Administrator this time</i>. Configure AWS CLI:
                <prism language="powershell">aws configure</prism>It'll ask for the following values:
                <ul class="pt-1 pb-2">
                  <li>
                    <b>Access Key ID, Secret Access Key:</b> In the AWS Access Keys file you downloaded. Open with Notepad.
                  </li>
                  <li>
                    <b>Default Region Name:</b> us-east-1
                  </li>
                  <li>
                    <b>Default Output Format:</b> json
                  </li>
                </ul>
              </li>
              <li class="pb-2">
                <b>[Powershell]:</b> Using Powershell (not as admin), create an SSH key for Terraform, create a directory for Sneakbike, and download the Sneakbike code:
                <prism language="powershell">{{snippet1}}</prism>The Sneakbike folder is now located in the "repo" folder in your home folder, usually something like:
                <b>C:\Users\yourname\repos\Sneakbike</b>
              </li>
            </ol>

            <h3>Creating the Server</h3>

            <p>
              <b>
                For what follows, open Powershell (not as admin). If you're creating a server, keep Powershell open until you've run
                <prism inline language="powershell">terraform destroy</prism>.
              </b>
            </p>

            <ol class="pt-1">
              <li class="pb-2">
                Go into the Sneakbike Terraform folder:
                <prism language="powershell">cd $HOME/repos/sneakbike/terraform</prism>
              </li>
              <li class="pb-2">
                Run the Terraform initialization script. You only need to do this once, so if you've already done it skip this step.
                <prism language="powershell">terraform init</prism>
              </li>
              <li class="pb-2">
                <b>To Create an RTMP Server</b> for a race:
                <prism language="powershell">terraform apply</prism>After you run this, you'll see a bunch of text and then it'll ask you for a response. You'll have to answer "yes" to have it create the server for you.
              </li>
              <li class="pb-2">
                The server will take about a minute or two to be created. At the end, it will print out the RTMP address, which will look something like:
                <prism inline language="powershell">rtmp://NumbersAndPeriods:1935/live</prism>. This is what you'll copy-and-paste to your racers with keys you make up for them.
              </li>
              <li class="pb-2">
                <b>To Destroy the RTMP Server</b> when you're finished:
                <prism language="powershell">terraform destroy</prism>
              </li>
            </ol>

            <warning-card>
              Make sure to destroy the server when you're done otherwise you'll
              incur charges when you're not using the server!
            </warning-card>
          </div>
          <div class="ml-6 mt-6">
            <h2>Producing</h2>

            <p>In order to Produce, you'll need to create an RTMP server, distribute "keys" to the runners, and capture their broadcast in OBS.</p>

            <ol class="pt-1 pb-4">
              <li class="pb-2">
                Download the
                <a
                  href="https://drive.google.com/file/d/138tSmlSwFQ4JRqjFUvfjgUY5kTkrWKM1/view?usp=sharing"
                  target="_blank"
                >Sneakbike_Ops.zip profile</a>
                (if you don't have permissions, ask in the Sneakbike discord channel).
              </li>
              <li class="pb-2">
                (Optional) Download the Sneakbike Scene Collection
                <a
                  href="https://drive.google.com/file/d/1vo2bvxwPDIcOZqGdMpTFlbXfgL9gXIHj/view?usp=sharing"
                  target="_blank"
                >Sneakbike_Ops.json</a>
                for examples of scenes we usually use.
              </li>
              <li class="pb-2">
                Import the Sneakbike_Ops profile into OBS the same way we import the runner profile in
                <router-link to="/runner-setup">Runner Setup</router-link>.
              </li>
              <li
                class="pb-2"
              >Distribute the RTMP address (from your server creation above) to the runners, and give each a different key. The key acts like a password or identifier. For example, we will usually give a runner a key which is their name in lowercase.</li>
              <li class="pb-2">
                To get a runner's RTMP stream, choose the
                <prism inline language="powershell">VLC Video Source</prism>, add their RTMP address, and use "Always Play Even When Not Visible". The address should be the RTMP address for that runner, similar to
                <prism inline language="powershell">rtmp://the_ec2_ip:1935/live/the_runner_key</prism>
              </li>
              <li
                class="pb-2"
              >Create your scene however you'd like with an overlay, background, etc.</li>
            </ol>

            <h3>Troubleshooting</h3>
            <p>The most common issue we have is the VLC not capturing the runner's stream. In this case, you can do a few things:</p>
            <ul class="pt-1">
              <li
                class="pb-2"
              >Make sure the runner is streaming to the right address and has the correct key. Note keys are case-sensitive.</li>
              <li class="pb-2">Delete the VLC source and recreate it.</li>
            </ul>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
const snippet1 = `# Create an SSH Key for Terraform 
mkdir -p $HOME/.ssh
ssh-keygen -t rsa -f $HOME/.ssh/terraform -q -N """"

# Clone Sneakbike 
mkdir -p $HOME/repos
cd $HOME/repos ; git clone https://github.com/jsal13/sneakbike.git 
`;

export default {
  name: "SetupProducerText",
  data() {
    return { snippet1 };
  },
};
</script>
