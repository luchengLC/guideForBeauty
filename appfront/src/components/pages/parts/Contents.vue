<template>
  <div class="contents" style="margin: 0; padding: 0">

    <!--搜索框-->
    <div class="search-bar">
      <div class="div-input">
        <el-input class="search-input" placeholder="请输入内容" v-model="input"></el-input>
        <el-button class="search-btn" slot="append" icon="el-icon-search" @click="searchWithPage(1)"></el-button>
      </div>
    </div>

    <!--价格排序 下拉选择框-->

    <!--item 表-->
    <div class="hot-search">
      <h2>{{showWords}}</h2>
      <div class="goods-container">
        <div class="goods-item" v-for="(item, index) in searchGoods" :key="index">
          <a :href="item.address">
            <img :src="item.img1_address" alt="">
            <p class="title">{{item.name}}</p>
          </a>
          <!--<p class="text">{{item.description}}</p>-->
          <div class="btn-div">
            <p class="price">{{item.price}}</p>
            <el-button class="price-btn" type="text">降价通知</el-button>
          </div>
          <div class="btn-div">
            <p class="store">{{item.store}}</p>
            --
            <p class="platform">{{item.platform}}</p>
          </div>
        </div>
      </div>
    </div>


    <!--分页器-->
    <!--<div style="margin: 50px 0 20px 0; padding: 0;">-->
    <!--<el-pagination-->
    <!--background-->
    <!--layout="prev, pager, next"-->
    <!--:total="1000">-->
    <!--</el-pagination>-->
    <!--</div>-->

  </div>
</template>

<script>
  import ElButton from '../../../../node_modules/element-ui/packages/button/src/button'
  export default {
    components: {ElButton},

    data () {
      return {
        input: '',
        showWords: '',
//        searchGoods:[],
        searchGoods: [
          {
            name: '草木良品 粉扑',
            description: '三层气垫美妆粉扑 7片装',
            price: '29.80元',
            img1_address: 'https://img14.360buyimg.com/n7/jfs/t3181/1/7063487291/356223/dd098dcf/58afec60Ne696710b.jpg',
            address: 'https://item.jd.com/4500384.html',
            store: '佚名',
            platform: '京东',
          },
          {
            name: '贝德玛（Bioderma）',
            description: '舒妍多效洁肤液500ml',
            price: '29.80元',
            img1_address: 'https://img11.360buyimg.com/n7/jfs/t5314/278/1411992625/75643/48151408/59102922Nb437b10f.jpg',
            address: 'https://item.jd.com/234366.html',
            store: '佚名',
            platform: '京东',
          },
          {
            name: '玛丽黛佳（MARIEDALGAR）',
            description: '自然生动眉笔0.2g*2 05 棕色',
            price: '29.80元',
            img1_address: 'https://img11.360buyimg.com/n7/jfs/t4441/91/2516213441/99992/412ca7fd/58f0809dN9ce5c595.jpg',
            address: 'https://item.jd.com/1133491.html',
            store: '佚名',
            platform: '京东',
          }
        ]
      }
    },
    methods: {
        searchWithPage(pageNo){
          let kw = this.input.replace(' ', '%20');
          this.$http.get('http://127.0.0.1:8000/beauty/productsList/getProductsPage?wd=' + kw + '&PageNo=' + pageNo)
            .then((response) => {
            let res = response.data
            if (res.error_code === 0) {
              // 成功
              console.log(res)
              this.searchGoods = [].concat(res.item_list)

            } else {  // 失败
              this.$message.error('没有查找到对应的商品，请重试！')
              console.log(res['msg'])
            }
          })
        }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .contents {
    .search-bar {
      display: -webkit-flex; /* Safari  chrome */
      display: flex;
      justify-content: center;
      .div-input {
        margin: 15px 0 15px 0;
        width: 400px;
        display: -webkit-flex; /* Safari  chrome */
        display: flex;
        flex-direction: row;
        .search-input {
        }
        .search-btn {
        }
      }
    }
    .hot-search {
      width: 1226px;
      margin: 26px auto 0;
      h2 {
        font-size: 22px;
        font-weight: 200;
        line-height: 58px;
        color: #333;
        text-align: left;
      }
      .goods-container {
        width: 1226px;
        display: -webkit-flex; /* Safari  chrome */
        display: flex;
        justify-content: left;
        flex-wrap: wrap; // 自动换行
        .goods-item {
          width: 234px;
          height: 300px;
          background: #fafafa;
          display: -webkit-flex; /* Safari  chrome */
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          text-align: center;
          transition: all .2s linear;
          margin: 8px 5px 12px 5px;

          &:hover {
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
            border-top: 3px solid #ff8080; //#e53935
            margin-top: -1px;
          }

          a {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            font-size: 12px;
            font-weight: 400;
            img {
              width: 160px;
              height: 160px;
            }
            .title {
              margin-top: 10px;
            }
          }
          .text {
            color: #b0b0b0;
            font-size: 9px;
            margin-top: 5px;
            margin-bottom: 10px;
          }
          .btn-div {
            display: -webkit-flex; /* Safari  chrome */
            display: flex;
            flex-direction: row;
            flex-wrap: nowrap;
            margin: 10px 0 0 0;
            padding: 0;
            text-align: right;
            .price {
              color: #ff8080;
              font-size: 16px;
              margin-right: 10px;
            }
            .price-btn {
              font-size: 10px;
              margin: 0;
              padding: 0;
            }

            .store {
              color: #b0b0b0;
              font-size: 9px;
            }
            .platform {
              color: #ffA0A0;
              font-size: 9px;
            }

          }

        }
      }
    }
  }

</style>
