<template>
  <div class="home">


    <h1><strong>美妆商品导购系统</strong></h1>

    <el-row style="margin:30px 0 20px 0">
      <el-dropdown @command="handleCommand"
                   style="display:inline-table; float:left"
                   split-button type="primary">
        <span class="el-dropdown-link">
          分类选择
        </span>
        <el-dropdown-menu slot="dropdown" style="width: 170px">
          <el-dropdown-item command="0" divided>底妆</el-dropdown-item>
          <el-dropdown-item command="1" divided>古龙水</el-dropdown-item>
          <el-dropdown-item command="2" divided>香精</el-dropdown-item>
          <el-dropdown-item command="3" divided>唇妆</el-dropdown-item>
          <el-dropdown-item command="4" divided>香水套装</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-button type="primary" style="float:right; margin: 2px;" disabled>搜索(未实现)</el-button>
      <el-input v-model="input" placeholder="搜索..." style="display:inline-table; width: 30%; float:right"></el-input>
    </el-row>
    <el-row>
      <el-table :data="stuList" style="width: 100%" border stripe>
        <el-table-column prop="id" label="名称" min-width="100">
          <template scope="scope"> {{ scope.row.fields.name }} </template>
        </el-table-column>
        <el-table-column prop="book_name" label="价格" min-width="50">
          <template scope="scope"> {{ scope.row.fields.price }} </template>
        </el-table-column>
        <el-table-column prop="add_time" label="品牌" min-width="80">
          <template scope="scope">{{ scope.row.fields.brand }}</template>
        </el-table-column>
        <el-table-column prop="add_time" label="产地" min-width="60">
          <template scope="scope">{{ scope.row.fields.produce_address }}</template>
        </el-table-column>
        <el-table-column prop="add_time" label="商品链接" min-width="50">
          <template scope="scope">
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
        classifyID: 0,
        input: '',
        stuList: [],
      }
    },
    mounted: function () {
//      this.showStu()
      this.showitemList(0)
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
              this.stuList = res['list']
            } else {
              this.$message.error('查询学生信息失败')
              console.log(res['msg'])
            }
          })
      },
      showitemList(classifyID){
        this.$http.get('http://127.0.0.1:8000/beauty/show_list?cID='+classifyID)
          .then((response) => {
            console.log(response)
            var res = response.data
            console.log(res)
            if (res.error_num === 0) {
              this.stuList = res['list']
            } else {
              this.$message.error('获取商品列表内容失败')
              console.log(res['msg'])
            }
          })
      },
      handleCommand(command) {
        this.$message(command+ "我很想给你展示这部分信息，但是我卡死在python局部变量...");
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .el-dropdown-link {
    cursor: pointer;
    color: #ffffff;
  }

  .el-icon-arrow-down {
    font-size: 12px;
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
