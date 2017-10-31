<template>
  <div class="main-nav">
    <div class="nav-first" @mouseenter="isNavEnter = true" @mouseleave="isNavEnter = false">
      <ul>
        <li v-for="(item,index) in navFirst" :key="index"
            :class="{active: item.type === selected}"
            @mouseenter="selected = item.type">
          <p>
            <span>{{item.name}}</span>
            <span class="icon">></span>
          </p>
        </li>
      </ul>
    </div>
    <div class="nav-sec" v-show="isNavEnter || isMenuEnter"
         @mouseenter="isMenuEnter = true" @mouseleave="isMenuEnter = false">
      <ul v-for="(item,index) in navFirst" v-show="item.type === selected" :key="index">
        <li v-for="(key,index) in navSec[item.type]"  :key="index">
          <div class="product">
            <a :href="key.link">
              <img :src="key.imgUrl" alt="">
              <p class="title">{{key.title}}</p>
            </a>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>

  export default {
    data(){
      return {
        selected: '',
        isNavEnter: false,
        isMenuEnter: false,
        navFirst: [
          {name: '香水', type: 'perfume'},
          {name: '口红', type: 'lipstick'},
          {name: '底妆', type: 'makeup'},
          {name: '眼线', type: 'eye'},
          {name: '睫毛膏', type: 'mascara'},
          {name: '腮红', type: 'blush'},
          {name: '身体乳', type: 'lotion'},
          {name: '眉笔', type: 'eyebrowPencil'},
          {name: '卸妆水', type: 'cleansingWater'},
          {name: '粉扑', type: 'puff'}
        ],
        navSec: {
          perfume: [
            {title: '女士香水', imgUrl: './static/img/xm6.png', link: 'https://coll.jd.com/list.html?sub=12469'},
            {title: '男士香水', imgUrl: './static/img/max2.png', link: 'https://coll.jd.com/list.html?sub=12472'},
          ],
          lipstick: [
            {title: '口红', imgUrl: './static/img/mipad3.png', link: 'https://search.jd.com/Search?keyword=%E5%8F%A3%E7%BA%A2&enc=utf-8&wq=%E5%8F%A3%E7%BA%A2&pvid=656b611c6a224f698e30e8b098b68f5b'}
          ],
          makeup: [
            {title: '底妆', imgUrl: './static/img/xmds_49.png', link: 'https://coll.jd.com/list.html?sub=12477'}
          ],
          eye: [
            {title: '眼线', imgUrl: './static/img/HD-Pro.png', link: 'https://coll.jd.com/list.html?sub=12508'}
          ],
          mascara: [
            {title: '睫毛膏1', imgUrl: './static/img/dianyuan.jpg', link: 'https://item.jd.com/1041897.html'},
            {title: '睫毛膏2', imgUrl: './static/img/c1xb.jpg', link: 'https://item.jd.com/1133499.html'}
          ],
          blush: [
            {title: '腮红', imgUrl: './static/img/toudai.jpg', link: 'https://coll.jd.com/list.html?sub=12134'},
            {title: '美宝莲腮红', imgUrl: './static/img/toudai.jpg', link: 'https://item.jd.com/3985553.html'}
          ],
          lotion: [
            {title: '身体乳1', imgUrl: './static/img/tiemo.jpg', link: 'https://item.jd.com/908037.html'},
            {title: '凡士林身体乳', imgUrl: './static/img/baohu.jpg', link: 'https://item.jd.com/1686564.html'}
          ],
          eyebrowPencil: [
            {title: '眉笔1', imgUrl: './static/img/xiancai.jpg', link: 'https://item.jd.com/1133491.html'}
          ],
          cleansingWater: [
            {title: '卸妆水某牌子', imgUrl: './static/img/xiangbao.jpg', link: 'https://item.jd.com/234366.html'}
          ],
          puff: [
            {title: '粉扑某牌子', imgUrl: './static/img/mitu.jpg', link: 'https://item.jd.com/4500384.html'}
          ]
        }
      }
    }
  }
</script>

<style lang="scss">
  .main-nav{
    font-size: 14px;
    width: 1226px;
    background: #fff;
    margin: 0 auto;
    position: relative;
    display: flex;
    justify-content: flex-start;
    >.nav-first{
      width: 235px;
      height: 458px;
      position: relative;
      z-index: 5;
      ul{
        display: flex;
        justify-content: space-between;
        flex-direction: column;
        background: rgba(0,0,0,0.6);
        padding: 20px 0;
        color: #fff;
        li{
          padding-left: 30px;
          height: 42px;
          line-height: 42px;
          cursor: pointer;
          &:hover{
            background: rgb(237, 61, 161);
          }
          >p{
            display: flex;
            justify-content: space-between;
            >.icon{
              margin-right: 20px;
              font-weight: bold;
            }
          }
        }
      }
    }
    .nav-sec{
      height: 458px;
      width: 992px;
      position: absolute;
      top: 0;
      right: 0;
      background: rgba(255, 255, 255, 0.8);
      z-index: 5;
      overflow: hidden;
      border: 1px solid #e0e0e0;
      border-left: none;
      box-shadow: 0 8px 16px rgba(0,0,0,0.8);
      ul{
        height: 458px;
        display: flex;
        flex-flow: wrap;
        flex-direction: column;
        align-items: flex-start;
        align-content: flex-start;
        justify-content: flex-start;
        li{
          width: 265px;
          height: 76px;
          .product{
            a{
              display: flex;
              justify-content: flex-start;
              align-items: center;
              transition: color .2s;
              width: 265px;
              padding: 20px 20px;
              &:hover{
                color: rgb(237, 61, 161);
              }
              img{
                width: 40px;
                height: 40px;
                margin-right: 12px;
              }
            }
          }
        }
      }
    }
  }
</style>
