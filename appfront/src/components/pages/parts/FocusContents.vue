<template>
  <div class="contents" style="margin: 0; padding: 0">

    <!--搜索框-->
    <!--<div class="search-bar">-->
    <!--<div class="div-input">-->
    <!--<el-input class="search-input" placeholder="请输入内容" v-model="input5"></el-input>-->
    <!--<el-button class="search-btn" slot="append" icon="el-icon-search"></el-button>-->
    <!--</div>-->
    <!--</div>-->

    <!--item 表-->
    <div class="hot-search" v-loading.fullscreen.lock="fullscreenLoading">
      <h2>{{showWords}}</h2>
      <div class="goods-container">
        <div class="goods-item" v-for="(item,index) in hotGoods" :key="index">
          <a :href="item.item_url" :title="item.name" target="_blank">
            <img :src="item.img_url" alt="item.name">
            <p class="title">{{item.name}}</p>
          </a>
          <p class="text" :title="item.name">{{item.name}}</p>
          <div class="btn-div">
            <p class="price">{{item.price}}</p>
            <el-button class="price-btn" type="text">移除关注</el-button>
          </div>
          <div class="btn-div">
            <!--<p class="store">{{item.store}}</p>-->
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
        username: '',
        showWords: '我的降价通知商品 列表',
        fullscreenLoading: false,
        hotGoods: [

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
      init() {
        this.username = this.$route.params.username;
        console.log(this.username);
        console.log('传参 sussess');
        this.hotGoods=[];
        this.handleGetFocusGoods();
      },
      handleGetFocusGoods(){
        console.log('handleGetFocusGoods');
        let _this = this;
        if (this.username === '') {
          this.$message.error('操作失误，请重新操作！')
        } else {
          let url = 'http://127.0.0.1:8000/beauty/cut_price/get_products?user_phone='+this.username;
          this.$http.get(url)
            .then((response) => {
              let res = response.data;
              console.log('========================')
              console.log(res);
              if (res.error_code === 0) {
                // 成功
                let ress = res['data']['item_list'];
                // 换大图
                for (let i in ress) {
                  ress[i]['img_url'] = ress[i]['img_url'].toString().replace('360buyimg.com/n5', '360buyimg.com/n7')
                }
                _this.hotGoods = ress;

              } else {  // 失败
                _this.$message.error(res['msg'])
                console.log(res['msg']);
              }
              _this.fullscreenLoading = false;
            });
        }
      }
    },
    mounted: function () {
      this.$nextTick(function () {
        this.init();
      })
    },

    watch: {
      '$route'(to, from){
        this.init();
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
              overflow:hidden;
              text-overflow:ellipsis;
              -o-text-overflow:ellipsis;
              white-space:nowrap;
              width:180px;
            }
          }
          .text {
            color: #b0b0b0;
            font-size: 9px;
            margin-top: 5px;
            margin-bottom: 10px;

            overflow:hidden;
            text-overflow:ellipsis;
            -o-text-overflow:ellipsis;
            white-space:nowrap;
            width:180px;
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
