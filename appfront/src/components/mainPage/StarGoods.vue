<template>
  <div class="hot-search">
    <h2>今日热搜</h2>
    <div class="goods-container">
      <div class="goods-item" v-for="(item,index) in starGoods" :key="index">
        <a :href="item.link">
          <img :src="item.imgUrl" alt="">
          <p class="title">{{item.title}}</p>
        </a>
        <p class="text">{{item.text}}</p>
        <p class="price">{{item.price}}</p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data(){
      return{
        starGoods: [
          {title: '草木良品 粉扑', text: '三层气垫美妆粉扑 7片装', price: '29.80元', imgUrl: 'https://img14.360buyimg.com/n7/jfs/t3181/1/7063487291/356223/dd098dcf/58afec60Ne696710b.jpg', link: 'https://item.jd.com/4500384.html'},
          {title: '贝德玛（Bioderma）', text: '舒妍多效洁肤液500ml', price: '29.80元', imgUrl: 'https://img11.360buyimg.com/n7/jfs/t5314/278/1411992625/75643/48151408/59102922Nb437b10f.jpg', link: 'https://item.jd.com/234366.html'},
          {title: '玛丽黛佳（MARIEDALGAR）', text: '自然生动眉笔0.2g*2 05 棕色', price: '29.80元', imgUrl: 'https://img11.360buyimg.com/n7/jfs/t4441/91/2516213441/99992/412ca7fd/58f0809dN9ce5c595.jpg', link: 'https://item.jd.com/1133491.html'},
          {title: '草木良品 粉扑', text: '三层气垫美妆粉扑 7片装', price: '29.80元', imgUrl: 'https://img14.360buyimg.com/n7/jfs/t3181/1/7063487291/356223/dd098dcf/58afec60Ne696710b.jpg', link: 'https://item.jd.com/4500384.html'},
          {title: '草木良品 粉扑', text: '三层气垫美妆粉扑 7片装', price: '29.80元', imgUrl: 'https://img14.360buyimg.com/n7/jfs/t3181/1/7063487291/356223/dd098dcf/58afec60Ne696710b.jpg', link: 'https://item.jd.com/4500384.html'}
        ]
      }
    }
  }
</script>

<style lang="scss">
  .hot-search{
    width: 1226px;
    margin: 26px auto 0;
    h2{
      font-size: 22px;
      font-weight: 200;
      line-height: 58px;
      color: #333;
      text-align: left;
    }
    .goods-container{
      height: 340px;
      width: 1226px;
      display: flex;
      justify-content: space-between;
      .goods-item{
        width: 234px;
        height: 300px;
        background: #fafafa;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        transition: all .2s linear;
        &:hover{
          box-shadow: 0 15px 30px rgba(0,0,0,0.1);
          margin-top: -1px;
        }
        &:nth-child(1){
          border-top: 1px solid #ffac13;
        }
        &:nth-child(2){
          border-top: 1px solid #83c44e;
        }
        &:nth-child(3){
          border-top: 1px solid #2196f3;
        }
        &:nth-child(4){
          border-top: 1px solid #e53935;
        }
        &:nth-child(5){
          border-top: 1px solid #00c0a5;
        }
        a{
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          font-size: 14px;
          font-weight: 400;
          img{
            width: 160px;
            height: 160px;
          }
        }
        .text{
          color: #b0b0b0;
          font-size: 12px;
          margin-top: 10px;
          margin-bottom: 15px;
        }
        .price{
          color: rgb(237, 61, 161);
          font-size: 14px;
        }
      }
    }
  }
</style>


