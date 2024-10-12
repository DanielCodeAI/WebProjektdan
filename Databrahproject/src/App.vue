<template>
  <div id="app">
    <FitnessForm />
  </div>
</template>

<script>
import FitnessForm from './components/FitnessForm.vue';
export default {
  name: 'App',
  components: {
    FitnessForm
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #3c648d;
  margin-top: 60px;
}
</style>