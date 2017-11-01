<template>
  <div class="main">
    <div class="main-top">
      <mainNav></mainNav>
      <mainCarousel></mainCarousel>
    </div>
    <div class="main-page">
      <hotGoods></hotGoods>
      <realativeSearchGoods></realativeSearchGoods>
    </div>
  </div>
</template>

<script>
  import MainNav from './MainNav'
  import MainCarousel from './MainCarousel'
  import HotGoods from './HotGoods'
  import RealativeSearchGoods from './RealativeSearchGoods'
  export default {
    components: {
      'mainNav': MainNav,
      'mainCarousel': MainCarousel,
      'hotGoods': HotGoods,
      'realativeSearchGoods': RealativeSearchGoods
    }
  }
</script>

<style lang="scss">
  .main{
    >.main-top{
      width: 1226px;
      margin: 0 auto;
      background: #fff;
      position: relative;
    }
    .main-page{
      background: #f5f5f5;
      margin: 0 auto;
    }
  }
</style>

