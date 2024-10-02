<template>
    <div>
      <button @click="signIn">Login with Google</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      signIn() {
        gapi.auth2.getAuthInstance().signIn().then((googleUser) => {
          const profile = googleUser.getBasicProfile();
          const id_token = googleUser.getAuthResponse().id_token;
          // You can save the token in the local storage
          localStorage.setItem('googleToken', id_token);
          this.$router.push('/');
        });
      }
    }
  };
  </script>
  