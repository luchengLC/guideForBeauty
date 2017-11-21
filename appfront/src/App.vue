<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  urlHeader: 'http://127.0.0.1:8000/beauty/',
  name: 'app',
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}
</style>
