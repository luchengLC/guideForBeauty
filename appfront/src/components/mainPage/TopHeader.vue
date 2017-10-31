<template>
  <div class="top-header">
    <div class="container">
      <div class="header-nav">
        <!--// 待删-->
      </div>
      <div class="header-search"
           @mouseenter="searchEnter"
           @mouseleave="searchLeave">
        <form>
          <input class="search-text" type="search"
                 @focus="inputFocus" @blur="inputBlur"
                 :class="{'search-focus': isFocus,'search-enter': isEnter}"
          >
          <label class="search-btn" value=""
                 :class="{'search-focus': isFocus,'search-enter': isEnter}"
          >
            <span class="icon"></span>
          </label>
        </form>
        <ul class="search-result" v-show="isFocus">
          <li v-for="(item,index) in results"  :key="index">
            <span class="item-name">{{item.name}}</span>
            <span class="item-num">约有{{item.number}}件</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="header-menu" v-show="(selected !== '') && (isNavEnter || isMenuEnter)" @mouseenter="isMenuEnter = true" @mouseleave="isMenuEnter = false">
      <ul v-for="(item,index) in navItems" v-show="item.type === selected"  :key="index">
        <li v-for="(key,index) in tabItems[item.type]"  :key="index">
          <div class="product">
            <p class="info" >{{key.info}}</p>
            <a :href="key.link"><img :src="key.imgUrl" alt=""></a>
            <p class="title">{{key.title}}</p>
            <p class="price">{{key.price}}</p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  // import $ from 'jQuery'
  // import HeaderMenu from './HeaderMenu'

  export default {
    data (){
      return {
        results: [
          {name: '香水', number: '22'},
          {name: '气垫', number: '123'},
          {name: '眉笔', number: '4'},
        ],
        selected: '',
        isFocus: false,
        isEnter: false,
        isNavEnter: false,
        isMenuEnter: false
      }
    },
    methods: {
      inputFocus: function(){
        this.isFocus = true
      },
      inputBlur: function(){
        this.isFocus = false
      },
      searchEnter: function(){
        this.isEnter = true
      },
      searchLeave: function(){
        this.isEnter = false
      }
    },
    components: {
    }
  }
</script>

<!--<style lang="scss" scoped>-->
<style lang="scss">
  .top-header{
    width: 100%;
    position: relative;
    >.container{
      width: 1226px;
      height: 100px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      >.header-nav{
        margin-right: auto;
        height: 100px;
        display: flex;
        align-items: center;
        ul{
          display: flex;
          flex-direction: row;
          justify-content: space-between;
          .item>a{
            height: 66px;
            line-height: 66px;
            padding: 0 10px;
            font-size: 16px;
            &:hover{
              color: rgb(237, 61, 161);
            }
          }
        }
      }
      >.header-search{
        position: relative;
        form{
          height: 50px;
          display: flex;
          align-items: center;
          .search-text{
            width: 223px;
            height: 50px;
            padding: 0 10px;
            border: 1px solid #e0e0e0;
            border-right: none;
            font-size: 14px;
            line-height: 48px;
            outline: 0;
            transition: all .2s;
          }
          .search-enter{
            border-color: #333;
          }
          .search-btn{
            width: 52px;
            height: 48px;
            border: 1px solid #e0e0e0;
            font-size: 24px;
            line-height: 24px;
            background: #fff;
            color: #616161;
            outline: 0;
            transition: all .2s;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            >.icon{
              background: url(../../assets/icon-search.png)  no-repeat;
              display: inline-block;
              width: 20px;
              height: 20px;
              background-size: 100% 100%;
              transition: all 0.2s;
            }
            &:hover{
              background: rgb(237, 61, 161);
              >.icon{
                background: url(../../assets/icon-search-white.png)  no-repeat;
                display: inline-block;
                width: 20px;
                height: 20px;
                background-size: 100% 100%;
              }
            }
          }
          .search-enter{
            border-color: #b0b0b0;
          }
          .search-focus{
            border-color: rgb(237, 61, 161);
          }
        }
        .search-result{
          position: absolute;
          z-index: 3;
          box-sizing: border-box;
          top: 50px;
          width: 224px;
          border: 1px solid rgb(237, 61, 161);
          border-top: 0;
          background: #fff;
          li{
            padding: 7px 13px;
            color: #424242;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            .item-num{
              color: #b0b0b0;
            }
            &:hover{
              color: rgb(237, 61, 161);
            }
          }
        }
      }
    }
  }

  .header-menu{
    position: absolute;
    top: 100px;
    left: 0;
    right: 0;
    height: 230px;
    z-index: 6;
    background: #fff;
    border-top: 1px solid #e0e0e0;
    border-bottom: 1px solid #e0e0e0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
    >ul{
      display: flex;
      justify-content: flex-start;
      >li{
        width: 160px;
        padding: 0 10px;
        &:first-child{
          margin-left: 80px;
        }
        &:last-child>.product>a{
          border-right: 0;
        }
        .product{
          display: flex;
          flex-direction: column;
          justify-content: flex-start;
          align-items: center;
          >a{
            border-right: 1px solid #e0e0e0;
            padding-right: 10px;
          }
          a>img{
            width: 159px;
            height: 110px;
          }
          .info{
            line-height: 10px;
            height: 10px;
            padding: 5px 20px;
            margin-bottom: 20px;
            color: rgb(237, 61, 161);
            border: 1px solid rgb(237, 61, 161);
          }
          .title{
            margin-top: 20px;
            margin-bottom: 5px;
            color: #333;
          }
          .price{
            color: rgb(237, 61, 161);
          }
        }
      }
    }
  }
</style>
