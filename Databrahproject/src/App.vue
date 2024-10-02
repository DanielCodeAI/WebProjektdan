<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>


//////
<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  mounted() {
    // Load Google API client library
    gapi.load('client:auth2', () => {
      gapi.client.init({
        apiKey: 'YOUR_GOOGLE_API_KEY',
        clientId: 'YOUR_GOOGLE_CLIENT_ID',
        discoveryDocs: ["https://sheets.googleapis.com/$discovery/rest?version=v4"],
        scope: 'https://www.googleapis.com/auth/spreadsheets',
      }).then(() => {
        console.log("Google API initialized");
      });
    });
  }
};
</script>

