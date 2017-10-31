<template>
  <footer>
    <div class="service">
      <a :href="item.link" v-for="(item,index) in service" :key="index">
        <span class="iconfont">{{item.unicode}}</span>
        <span class="text">{{item.text}}</span>
      </a>
    </div>
    <div class="link">
      <div class="item" v-for="(item,index) in link" :key="index">
        <span class="title">{{item.title}}</span>
        <a :href="key.link" v-for="(key,index) in item.text" :key="key">
          <span>{{key.title}}</span>
        </a>
      </div>
      <div class="contact">
        <span class="number">134119XXXXX</span>
        <span class="text">周一至周日 8:00-18:00<br></span>
        <span class="customer">联系我们</span>
      </div>
    </div>
    <div class="info">
      <div class="info-container">

      </div>
    </div>
  </footer>
</template>

<script>
  export default {
    data(){
      return {
        link: [
          {
            title: '帮助中心',
            text: [
              {title: '账户管理', link: 'https://www.mi.com/service/account/register/'},
              {title: '购物指南', link: 'https://www.mi.com/service/buy/buytime/'},
              {title: '订单操作', link: 'https://www.mi.com/service/order/sendprogress/'}
            ]
          },
          {
            title: '服务支持',
            text: [
              {title: '售后政策', link: 'https://www.mi.com/service/exchange'},
              {title: '自助服务', link: 'http://fuwu.mi.com/'},
              {title: '相关下载', link: 'http://xiazai.mi.com/'}
            ]
          }
        ]
      }
    }
  }
</script>

<style lang="scss">
  @font-face {
    font-family: 'iconfont';  /* project id 273742 */
    src: url('//at.alicdn.com/t/font_o29w1lx6rktn8kt9.eot');
    src: url('//at.alicdn.com/t/font_o29w1lx6rktn8kt9.eot?#iefix') format('embedded-opentype'),
    url('//at.alicdn.com/t/font_o29w1lx6rktn8kt9.woff') format('woff'),
    url('//at.alicdn.com/t/font_o29w1lx6rktn8kt9.ttf') format('truetype'),
    url('//at.alicdn.com/t/font_o29w1lx6rktn8kt9.svg#iconfont') format('svg');
  }
  .iconfont{
    font-family:"iconfont" !important;
    font-size:16px;font-style:normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
  }
  footer{
    display: flex;
    margin: 0 auto;
    flex-direction: column;
    justify-content: space-between;
    align-content: center;
    .service{
      width: 1226px;
      margin-bottom: 30px;
      background: #fff;
      display: flex;
      justify-content: center;
      >a{
        width: 240px;
        height: 25px;
        border-left: 1px solid #e0e0e0;
        font-size: 16px;
        line-height: 25px;
        color: #616161;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: all .2s;
        &:hover{
          color: rgb(237, 61, 161);
        }
        &:nth-child(1){
          border: none;
        }
        .iconfont{
          font-size: 24px;
          margin-right: 5px;
        }
      }
    }
    .link{
      width: 1226px;
      margin: 0 auto 30px;
      display: flex;
      justify-content: space-between;
      .item{
        width: 160px;
        height: 112px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        >.title{
          margin: 0 0 26px;
          font-size: 14px;
          color: #424242;
        }
        >a{
          display: flex;
          align-items: center;
          transition: all .2s;
          color: #757575;
          &:hover{
            color: rgb(237, 61, 161);
          }
        }
      }
      .contact{
        width: 251px;
        height: 112px;
        border-left: 1px solid #e0e0e0;
        text-align: center;
        color: #616161;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        .number{
          margin: 0 0 5px;
          font-size: 22px;
          color: rgb(237, 61, 161);
        }
        .text{
          line-height: 16px;
        }
        .customer{
          background: #fff;
          color: rgb(237, 61, 161);
          width: 118px;
          height: 28px;
          line-height: 28px;
          border: 1px solid rgb(237, 61, 161);
          cursor: pointer;
          transition: all .2s;
          &:hover{
            background: rgb(237, 61, 161);
            color: #fff;
          }
        }
      }
    }
    .info{
      width: 100%;
      padding: 30px 0;
      font-size: 12px;
      background: #fafafa;
      .info-container{
        width: 1226px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        .mi-logo>img{
          width: 57px;
          height: 57px;
          margin-right: 10px;
        }
        .text{
          color: #b0b0b0;
          text-align: left;
          margin-right: auto;
          line-height: 18px;
          >p:nth-child(1){
            color: #757575;
          }
        }
        .info-logo{
          display: flex;
          justify-content: space-between;
          height: 28px;
        }
      }
    }
    .slogan{
      text-align: center;
      background: #fafafa;
      padding-bottom: 30px;
    }
  }
</style>
