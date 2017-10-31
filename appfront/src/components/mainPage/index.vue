<template>
  <div class="main">
    <topBar></topBar>
    <topHeader></topHeader>
    <mainPage></mainPage>
    <miFooter></miFooter>
  </div>
</template>

<script>
  import 'normalize.css/normalize.css'
  import '../../assets/reset.css'
  import TopBar from './TopBar'
  import TopHeader from './TopHeader'
  import MainPage from './MainPage'
  import MiFooter from './MiFooter'
  export default {
    name: 'main',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    components: {
      'topBar': TopBar,
      'topHeader': TopHeader,
      'mainPage': MainPage,
      'miFooter': MiFooter
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
