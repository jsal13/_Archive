<template>
  <div id="app">
    <!-- <nav class="navbar navbar-expand navbar-light bg-light">
      <div class="container-fluid">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown"
              aria-expanded="false">
              <span class="navbar-toggler-icon"></span>
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><router-link class="dropdown-item" :to="'/setup'">Runner Setup</router-link></li>
              <li><router-link class="dropdown-item" :to="'/runner-troubleshooting'">Runner Troubleshooting & FAQ</router-link>
              <li><router-link class="dropdown-item" :to="'/resource-map'">Document Map</router-link></li>
            </ul>
          </li>
          <li class="nav-item">
            <router-link class="navbar-brand" :to="'/'"><span class="site-title">Sneakbike</span></router-link>
          </li>
        </ul>

        <a class="a-no-dec" href="https://twitch.tv/sneakbike" target="_blank">
          <i class="navbar-icon bi-twitch"></i>
        </a>

        <a class="a-no-dec" href="https://www.youtube.com/channel/UC5WLNGgGQH2tpNHM5uk2kCg" target="_blank">
          <i class="navbar-icon bi-youtube"></i>
        </a>

        <a class="a-no-dec" href="https://www.github.com/jsal13/sneakbike-utils/" target="_blank">
          <i class="navbar-icon bi-github"></i>
        </a>

        <a class="a-no-dec" href="https://discord.gg/3sKkemTtWK" target="_blank">
          <i class="navbar-icon bi-discord"></i>
        </a>

      </div>
    </nav> -->
    <!-- <div class="container-fluid container-md mt-5 px-5"> -->
    <router-view/>
    <!-- </div> -->
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>
