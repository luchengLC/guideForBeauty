<template>
  <div class="home">


    <h1><strong>美妆商品导购系统</strong></h1>

    <el-row style="margin:30px 0 20px 0">
      <el-dropdown @command="handleCommand"
                   split-button type="primary"
                   style="display:inline-table; float:left">
        <span class="el-dropdown-link">
          {{ selectedClassify }}
        </span>
        <el-dropdown-menu slot="dropdown" style="width: 170px">
          <el-dropdown-item command="底妆" divided>底妆</el-dropdown-item>
          <el-dropdown-item command="古龙水" divided>古龙水</el-dropdown-item>
          <el-dropdown-item command="香精" divided>香精</el-dropdown-item>
          <el-dropdown-item command="唇妆" divided>唇妆</el-dropdown-item>
          <el-dropdown-item command="眼妆" divided>眼妆</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-button type="primary" style="float:right; margin: 2px;" @click.native="showSearchList">搜索</el-button>
      <el-input v-model="input" placeholder="请输入商品名称..." style="display:inline-table; width: 30%; float:right"></el-input>
    </el-row>
    <el-row>
      <el-table :data="responseList" style="width: 100%" border stripe>
        <el-table-column prop="id" label="名称" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.name }} </template>
        </el-table-column>
        <el-table-column prop="book_name" label="价格" min-width="50">
          <template slot-scope="scope"> {{ scope.row.fields.price }} </template>
        </el-table-column>
        <el-table-column prop="add_time" label="品牌" min-width="80">
          <template slot-scope="scope">{{ scope.row.fields.brand }}</template>
        </el-table-column>
        <el-table-column prop="add_time" label="产地、店名" min-width="60">
          <template slot-scope="scope">{{ scope.row.fields.produce_address }} <br/> {{ scope.row.fields.store }}</template>
        </el-table-column>
        <el-table-column prop="add_time" label="商品链接" min-width="50">
          <template slot-scope="scope">
            <a :href=" scope.row.fields.address" target="_blank">链接</a>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    <div class="page">
      <el-pagination
        :page-size="100"
        layout="prev, pager, next, jumper"
        :total="1000">
      </el-pagination>

      <!--勿删，待删-->
      <!--@size-change="handleSizeChange"-->
      <!--@current-change="handleCurrentChange"-->
      <!--:current-page.sync="currentPage3"-->

    </div>
  </div>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        input: '',
        responseList: [],
        selectedClassify: '选择分类',
        res:[],
      }
    },
    mounted: function () {
      this.showItemList('底妆')
    },
    methods: {
      addStu(){
        this.$http.get('http://127.0.0.1:8000/beauty/add_student?stu=' + this.input)
          .then((response) => {
            var res = response.data
            if (res.error_num === 0) {
              //  刷新，重新请求
              this.showStu()
            } else {
              this.$message.error('新增学生信息失败，请重试')
              console.log(res['msg'])
            }
          })

      },
      showStu(){
        this.$http.get('http://127.0.0.1:8000/beauty/show_student')
          .then((response) => {
            console.log("我就测测~")
            console.log(response)
            var res = response.data
            console.log(res)
            if (res.error_num === 0) {
              this.responseList = res['list']
            } else {
              this.$message.error('查询学生信息失败')
              console.log(res['msg'])
            }
          })
      },

      //---------------------------- 以上是测试----------------------

      showItemList(command){
        this.$http.get('http://127.0.0.1:8000/beauty/show_list?cmd='+command)
          .then((response) => {
            console.log(response)
            this.res = response.data  // 这里不能不用变量res缓存
            console.log(response.data)
            if (this.res.error_num === 0) {
              this.responseList = this.res['list']
            } else {
              this.$message.error('获取商品列表内容失败')
              console.log(this.res['msg'])
            }
          })
      },
      handleCommand(command) {
        this.selectedClassify = command
        this.input = ''
        this.showItemList(command)        // 点击下拉菜单，改变内容
      },
      // 简单搜索
      showSearchList() {

          // 判断搜索框是否有内容


        console.log('进入搜索方法')
        if(this.selectedClassify === '选择分类') {
          this.selectedClassify = '底妆'
        }
        console.log(this.selectedClassify)
        this.$http.get('http://127.0.0.1:8000/beauty/show_search_list?cmd='+this.selectedClassify+'&name='+this.input)
          .then((response) => {
            console.log(response)
            console.log(this.input) /// 打印搜索框内容，检测
            this.res = response.data
            console.log(this.res)
            if (this.res.error_num === 0) {
              this.responseList = this.res['list']
            } else {
              this.$message.error('获取搜索列表内容失败')
              console.log(this.res['msg'])
            }
          })
      },

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .el-dropdown-link {
    cursor: pointer;
    color: #ffffff;
  }

  .home {
    margin: 60px 10px 10px 10px;
  }

  .page {
    margin: 30px;
  }

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
</style>
