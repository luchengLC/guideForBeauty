<template>
  <div class="main">
    <topBar></topBar>
    <contents></contents>
    <bfooter></bfooter>
  </div>
</template>

<script>
  import 'normalize.css/normalize.css'
  import '../../assets/reset.css'
  import TopBar from './parts/TopBar'
  import Contents from './parts/SimilarContents'
  import BFooter from './parts/Footer'
  export default {
    activeIndex: 'focus',
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
<style lang="scss" scoped>
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

    background: #f5f5f5;

    .bottom {
      background: #fff;
    }
  }
</style>
