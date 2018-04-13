<template>
  <div class="main">
    <topBar class="topbar"></topBar>
    <contents class="contents"></contents>
    <bfooter class="footer"></bfooter>
  </div>
</template>

<script>
  import 'normalize.css/normalize.css'
  import '../../assets/reset.css'
  import TopBar from './parts/TopBar'
  import Contents from './parts/Contents'
  import BFooter from './parts/Footer'
  export default {
    activeIndex: '/',
    data () {
      return {

      }
    },
    components: {
      'topBar': TopBar,
      'contents': Contents,
      'bfooter': BFooter
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
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

  .main {
    display: -webkit-flex; /* Safari  chrome */
    display: flex;
    flex-direction: column; /* 方向 列   上到下*/
    height: 100%;
    background: #f5f5f5;
    min-height: 100vh;

    .contents {
      flex: 1;
    }

  }
</style>
