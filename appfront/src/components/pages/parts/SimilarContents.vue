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
    <div class="hot-search">
      <h2>{{showWords}}</h2>
      <div class="goods-container" v-loading.fullscreen.lock="fullscreenLoading">
        <div class="goods-item" v-for="(item,index) in similarGoods" :key="index">
          <a :href="item.address" :title="item.name" target="_blank">
            <img :src="item.img1_address" alt="item.name">
            <p class="title">{{item.name}}</p>
          </a>
          <p class="text" :title="item.description">{{item.description}}</p>
          <div class="btn-div">
            <p class="price">{{item.price}}</p>
            <el-button class="price-btn" type="text">评论数：{{item.comment_count}}</el-button>
          </div>
          <div class="btn-div">
            <p class="store">{{item.store}}</p>
            <p class="platform">平台：{{item.platform}}</p>
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
        showWords: '相似商品',
        item: {},
        similarGoods: [],
        fullscreenLoading: false,
      }
    },
    methods: {
      init(){
        this.item = this.$route.params.item;
        console.log(this.item);
        console.log('传参 sussess');
        console.log(this.item['category']);
        console.log(this.item['name']);

        this.similarGoods = [];
        console.log('到达init');
//        this.similarGoods.push(this.item);
//        console.log('this.similarGoods=')
//        console.log(this.similarGoods);
        this.handleGetSimilarGoods();
      },
      handleGetSimilarGoods() {
        console.log('到达handleGetSimilarGoods');
        if (this.item === null) {
          this.$message.error('操作失误，请重新操作！')
        } else {
          this.fullscreenLoading = true;
          let category = this.item.category;
          let pname = this.item.name;

          console.log('原始的pname = ' + pname);
          console.log('原始的category = ' + category);
          pname = encodeURIComponent(pname);
          console.log('encode的pname = ' + pname);
          let pnamem = decodeURIComponent(pname);
          console.log('decode的pnamem = ' + pnamem);

          // url编码
          let url = 'http://127.0.0.1:8000/beauty/productsList/getAllSimilarProducts?category=' + category + '&pname=' + pname;

          this.$http.get(url)
            .then((response) => {
              this.res = response.data;
              console.log('========================')
              console.log(this.res);
              if (this.res.error_code === 0) {
                // 成功
                let ress = this.res['data'];
                // 换大图
                for (let i in ress) {
                  ress[i]['img1_address'] = ress[i]['img1_address'].toString().replace('360buyimg.com/n5', '360buyimg.com/n7')
                }
                this.similarGoods = this.res['data'];

              } else {  // 失败
                this.$message.error('没有查找到对应的相似商品，请重试！')
                console.log(this.res['msg']);
              }
              this.fullscreenLoading = false;
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
              overflow: hidden;
              text-overflow: ellipsis;
              -o-text-overflow: ellipsis;
              white-space: nowrap;
              width: 180px;
            }
          }
          .text {
            overflow: hidden;
            text-overflow: ellipsis;
            -o-text-overflow: ellipsis;
            white-space: nowrap;
            width: 180px;

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
