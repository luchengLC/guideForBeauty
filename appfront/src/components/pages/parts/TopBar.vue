<template>
  <div style="margin: 0; padding: 0">
    <el-menu
      :default-active="activeIndex"
      class="el-menu"
      mode="horizontal"
      router
      background-color="#545c64"
      active-text-color="#fff"
      active-backgroud-color="#545c64"
      text-color="#fff">
      <el-menu-item class="el-menu-item" index="/">美妆商品导购系统</el-menu-item>
      <el-menu-item class="el-menu-item" index="focus">我的降价通知商品</el-menu-item>
      <el-button class="menu-btn" type="text" id="logout" @click="dialogRegisterVisible=true">{{register}}
      </el-button>
      <el-button class="menu-btn" type="text" id="name-login" @click="dialogLoginVisible=true">{{login_out}}
      </el-button>

    </el-menu>

    <!--登录 对话框-->
    <el-dialog
      title="登录"
      :visible.sync="dialogLoginVisible"
      width="500px"
      :before-close="handleLoginClose">
      <div class="el-dialog-div">
        账号：
        <el-input v-model="input_username" placeholder="手机号码..." style="width: 300px"></el-input>
      </div>
      <div class="el-dialog-div">
        密码：
        <el-input v-model="input_pw" placeholder="密码..." style="width: 300px"></el-input>
      </div>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogLoginVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogLoginVisible = false">确 定</el-button>
      </span>
    </el-dialog>

    <!--注册 对话框-->
    <el-dialog
      title="注册"
      :visible.sync="dialogRegisterVisible"
      width="500px"
      :before-close="handleRegisterClose">
      <div class="el-dialog-div">
        账 号：
        <el-input v-model="input_username" placeholder="手机号码..." style="width: 300px"></el-input>
      </div>
      <div class="el-dialog-div">
        昵 称：
        <el-input v-model="input_name" placeholder="昵称..." style="width: 300px"></el-input>
      </div>
      <div class="el-dialog-div">
        密 码：
        <el-input v-model="input_pw" placeholder="密码..." style="width: 300px"></el-input>
      </div>
      <div class="el-dialog-div">
        邮 箱：
        <el-input v-model="input_email" placeholder="邮箱..." style="width: 300px"></el-input>
      </div>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogRegisterVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogRegisterVisible = false">确 定</el-button>
      </span>
    </el-dialog>

  </div>


</template>

<script>
  import ElButton from "../../../../node_modules/element-ui/packages/button/src/button";
  export default {
    components: {ElButton},
    props: ["actives"],
    data () {
      return {
        input_username: '',
        input_name: '',
        input_pw: '',
        input_email: '',
        dialogLoginVisible: false,
        dialogRegisterVisible: false,
        msg: 'Welcome to Your Vue.js App',
        register: '注册',
        login_out: '登录',
        activeIndex: '',
      }
    },
    mounted: function() {
      this.$nextTick(function () {
        this.activeIndex = this.actives;
        console.log(this.activeIndex);
      })
    },
    methods: {
      handleLoginClose(done) {
        this.dialogLoginVisible = false
//        this.$confirm('确认关闭？')
//          .then(_ => {
//            done();
//          })
//          .catch(_ => {});
      },

      handleRegisterClose(done) {
        this.dialogRegisterVisible = false
      }
    },

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .el-menu {
    .el-menu-item {
      height: 30px;
      line-height: 30px;
    }
    .menu-btn {
      height: 30px;
      line-height: 0;
      margin: 0 20px 0 5px;
    }

    #name-login, #logout {
      float: right;
    }
  }

  .el-dialog-div {
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>
