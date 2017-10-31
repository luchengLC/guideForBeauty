<template>
  <div class="home">
    <el-row display="margin-top:10px">
      <el-input v-model="inputName" placeholder="姓名" style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" style="float:left; margin: 2px;">add</el-button>
    </el-row>
    <el-row>
      <el-table :data="stuList" style="width: 100%" border>
        <el-table-column prop="id" label="学号" min-width="100">
          <template scope="scope"> {{ scope.row.pk }} </template>
        </el-table-column>
        <el-table-column prop="book_name" label="姓名" min-width="100">
          <template scope="scope"> {{ scope.row.fields.sname }} </template>
        </el-table-column>
        <el-table-column prop="add_time" label="备注" min-width="100">
          <template scope="scope"> {{ scope.row.fields.smark }} </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        inputName: '',
        stuList: [],
      }
    },
    mounted: function () {
      this.showStu()
    },
    methods: {
      addStu(){
        this.$http.get('http://127.0.0.1:8000/beauty/add_student?stu=' + this.inputName)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num === 0) {
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
            console.log(response)
            var res = JSON.parse(response)
            console.log(res)
            if (res.error_num === 0) {
              this.stuList = res['list']
            } else {
              this.$message.error('查询学生信息失败')
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
