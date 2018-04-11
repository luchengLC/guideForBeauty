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
          <a :href="item.address" :title="item.name">
            <img :src="item.img1_address" alt="item.name">
          </a>

          <div class="info">
            <a :href="item.address" :title="item.name"><p class="title">{{item.name}}</p></a>
            <p class="description">{{item.description}}</p>
            <p class="platform">平台： <span>{{item.platform}}</span></p>
            <p class="store">商店： <span>{{item.store}}</span></p>
            <p class="comment-no">评论数： <span>{{item.comment_count}}</span></p>
            <p class="comment-rate">好评率： <span>{{item.good_comment_percentage}}</span></p>
          </div>


          <div class="price-div">
            <p>￥<span class="price">{{item.price}}</span></p>
            <div class="btn-div">
              <el-button class="price-btn" type="text">降价通知</el-button>
              <el-button class="similar-btn" type="text">找相似物</el-button>
            </div>
          </div>
          <!--<div class="btn-div">-->
          <!--</div>-->
        </div>
      </div>
    </div>


    <!--分页器-->
    <div style="margin: 50px 0 20px 0; padding: 0;">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="pageCount">
      </el-pagination>
    </div>

  </div>
</template>

<script>
  import ElButton from '../../../../node_modules/element-ui/packages/button/src/button'
  export default {
    components: {ElButton},

    data () {
      return {
        res: {},
        input: '',
        showWords: '',
        pageCount: 0,
//        searchGoods:[],
        searchGoods: [
          {
            name: '卡姿兰气垫cc霜 蜗牛调控气垫bb霜 持久保湿遮瑕美颜白皙底妆礼盒套装粉底液14.5g*2 02柔缎色+蜜语礼包',
            description: '三层气垫美妆粉扑 7片装',
            price: '29.80元',
            img1_address: 'https://img14.360buyimg.com/n7/jfs/t3181/1/7063487291/356223/dd098dcf/58afec60Ne696710b.jpg',
            address: 'https://item.jd.com/4500384.html',
            store: '佚名',
            platform: '京东',
            good_comment_percentage: "0.95",
            comment_count: 11000,
          },
          {
            name: '贝德玛（Bioderma）',
            description: '舒妍多效洁肤液500ml',
            price: '29.80元',
            img1_address: 'https://img11.360buyimg.com/n7/jfs/t5314/278/1411992625/75643/48151408/59102922Nb437b10f.jpg',
            address: 'https://item.jd.com/234366.html',
            store: '佚名',
            platform: '京东',
            good_comment_percentage: "0.95",
            comment_count: 11000,
          },
          {
            name: '玛丽黛佳（MARIEDALGAR）',
            description: '自然生动眉笔0.2g*2 05 棕色',
            price: '29.80元',
            img1_address: 'https://img11.360buyimg.com/n7/jfs/t4441/91/2516213441/99992/412ca7fd/58f0809dN9ce5c595.jpg',
            address: 'https://item.jd.com/1133491.html',
            store: '佚名',
            platform: '京东',
            good_comment_percentage: "0.95",
            comment_count: 11000,
          }
        ]
      }
    },
    methods: {
      searchWithPage(pageNo){
        if (this.input === '') {
          this.$message.error('请输入搜索信息！')
        } else {
          let kw = this.input.replace(' ', '%20');
          this.$http.get('http://127.0.0.1:8000/beauty/productsList/getProductsPage?wd=' + kw + '&PageNo=' + pageNo)
            .then((response) => {
              this.res = response.data
              if (this.res.error_code === 0) {
                // 成功
                let ress = this.res['data']['item_list']
                // emmmmmm， 将小图换成大图
                for (let i in ress) {
                  ress[i]['img1_address'] = ress[i]['img1_address'].toString().replace('360buyimg.com/n5', '360buyimg.com/n7')
                }

                this.searchGoods = this.res['data']['item_list']
                // page数
                this.pageCount = this.res['page_count'] * 10

              } else {  // 失败
                this.$message.error('没有查找到对应的商品，请重试！')
                console.log(this.res['msg'])
              }
            })
        }

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
        flex-direction: row;
        justify-content: center;
        flex-wrap: wrap; // 自动换行
        .goods-item {
          width: 80%;
          height: 180px;
          background: #fcfcfc;
          display: -webkit-flex; /* Safari  chrome */
          display: flex;
          flex-direction: row;
          justify-content: left;
          align-items: center;
          text-align: center;
          transition: all .2s linear;
          margin: 8px 5px 12px 5px;

          &:hover {
            box-shadow: 0 20px 35px rgba(0, 0, 0, 0.1);
            border-top: 3px solid #ff8080; //#e53935
            border-bottom: 3px solid #ff8080; //#e53935
            margin-top: -1px;
          }

          a {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            font-size: 12px;
            font-weight: 400;
            text-align: left;
            margin-left: 40px;
            img {
              width: 160px;
              height: 160px;
            }
          }

          .info {
            display: -webkit-flex; /* Safari  chrome */
            display: flex;
            flex-direction: column;
            justify-content: left;
            text-align: left;
            margin: 0 0 0 60px;

            a {
              margin: 0;
              .title {
                width: 400px;
                font-size: 14px;
                color: #096296;
                &:hover {
                  text-decoration: underline;
                }
              }
            }

            .description {
              color: #b0b0b0;
              font-size: 10px;
              margin: 10px 0 5px 0;
            }

            .platform {
              margin: 7px 0 0 0;
              span {
                color: #409EFF;
                font-size: 12px;
              }
            }
            .store {
              margin: 5px 0 0 0;
              span {
                color: #bbbbbb;
                font-size: 12px;
              }
            }

            .comment-no {
              margin: 7px 0 0 0;
              span {
                color: #ff8080;
                font-size: 12px;
              }
            }

            .comment-rate {
              margin: 7px 0 0 0;
              span {
                color: #ff8080;
                font-size: 12px;
              }
            }
          }

          .price-div {
            display: -webkit-flex; /* Safari  chrome */
            display: flex;
            flex-direction: row;
            flex-wrap: nowrap;
            margin: 0 0 0 40px;
            padding: 0;
            text-align: right;
            .price {
              color: #ff8080;
              font-size: 24px;
            }

            .btn-div {
              margin-left: 50px;
              display: -webkit-flex; /* Safari  chrome */
              display: flex;
              flex-direction: column;
              font-size: 12px;
              .price-btn {
                margin: 0;
                padding: 0;
                &:hover {
                  text-decoration: underline;
                }
              }
              .similar-btn {
                color: #ff8888;
                margin: 10px 0 0 0;
                padding: 0;
                &:hover {
                  text-decoration: underline;
                }
              }
            }

          }

        }
      }
    }
  }

</style>
