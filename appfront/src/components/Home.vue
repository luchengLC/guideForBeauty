<template>
  <div class="home">
    <h1>部分列表 前50条</h1>
    <el-row display="margin-top:10px">
      <!--<el-input v-model="input" placeholder="学号" style="display:inline-table; width: 30%; float:left"></el-input>-->
      <!--<el-button type="primary" style="float:left; margin: 2px;">add</el-button>-->
    </el-row>
    <el-row>
      <el-table :data="stuList" style="width: 100%" border stripe>
        <el-table-column prop="id" label="名称" min-width="100">
          <template scope="scope"> {{ scope.row.fields.name }} </template>
        </el-table-column>
        <el-table-column prop="book_name" label="价格" min-width="100">
          <template scope="scope"> {{ scope.row.fields.price }} </template>
        </el-table-column>
        <el-table-column prop="add_time" label="商品链接" min-width="100">
          <template scope="scope">{{ scope.row.fields.address }}</template>
        </el-table-column>
        <el-table-column prop="add_time" label="产地" min-width="100">
          <template scope="scope">{{ scope.row.fields.produce_address }}</template>
        </el-table-column>
        <el-table-column prop="add_time" label="品牌" min-width="100">
          <template scope="scope">{{ scope.row.fields.brand }}</template>
        </el-table-column>
      </el-table>
    </el-row>
    <div class="page">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage3"
        :page-size="100"
        layout="prev, pager, next, jumper"
        :total="1000">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        input: '',
        stuList: [],
      }
    },
    mounted: function () {
//      this.showStu()
      this.showitemList()
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
      showitemList(){
        this.$http.get('http://127.0.0.1:8000/beauty/show_baseMakeup')
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
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
