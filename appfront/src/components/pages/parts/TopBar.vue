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
      <el-button class="menu-btn" type="text" id="logout" @click="dialogRegisterVisible=true">{{btn_register}}
      </el-button>
      <el-button class="menu-btn" type="text" id="name-login" @click="dialogLoginVisible=true">{{btn_login}}
      </el-button>

    </el-menu>

    <!--登录 对话框-->
    <el-dialog
      title="登录"
      :visible.sync="dialogLoginVisible"
      width="500px"
      :before-close="handleLoginCansel">
      <el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="90px">
        <el-form-item label="账号" prop="username">
          <el-input v-model="loginForm.username" placeholder="手机号码..."></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="loginForm.password" placeholder="密码..."></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="handleLoginCansel">取 消</el-button>
        <el-button type="primary" @click="handleLoginSubmit">确 定</el-button>
      </span>
    </el-dialog>

    <!--注册 对话框-->
    <el-dialog
      title="注册"
      :visible.sync="dialogRegisterVisible"
      width="500px"
      :before-close="handleRegisterCansel">
      <el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="90px">
        <el-form-item label="账号" prop="username">
          <el-input v-model="loginForm.username" placeholder="手机号码..."></el-input>
        </el-form-item>
        <el-form-item label="昵称" prop="name">
          <el-input v-model="loginForm.name" placeholder="昵称..."></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="loginForm.password" placeholder="密码..."></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="loginForm.email" placeholder="邮箱..."></el-input>
        </el-form-item>

      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="handleRegisterCansel">取 消</el-button>
        <el-button type="primary" @click="handleRegisterSubmit(loginForm)">确 定</el-button>
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
        dialogLoginVisible: false,
        dialogRegisterVisible: false,
        msg: 'Welcome to Your Vue.js App',
        btn_register: '注册',
        btn_login: '登录',
        activeIndex: '',
        loginForm: {
          username: '',
          password: '',
          name: '',
          email: '',
        },
        registerForm: {},
        rules: {
          username: [
            {required: true, message: '请输入账号（手机号码）', trigger: 'blur'},
            {pattern: /^0?(13[0-9]|[15[7-9]|153|156|18[7-9])[0-9]{8}$/, message: '请正确地输入账号（手机号码）', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'},
            {min: 6, max: 30, message: '长度在 6 到 30 个字符', trigger: 'blur'},
            {pattern: /^(\w){6,20}$/, message: '只能输入6-20个字母、数字、下划线', trigger: 'blur'}
          ],
          name: [
            {required: true, message: '请输入昵称', trigger: 'blur'},
          ],
          email: [
            {required: true, message: '请输入邮箱', trigger: 'blur'},
            {
              pattern: /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$ /,
              message: '请输入正确的邮箱地址',
              trigger: 'blur'
            }
          ]
        },
      }
    },
    mounted: function () {
      this.$nextTick(function () {
        this.activeIndex = this.actives;
        console.log(this.activeIndex);
      })
    },
    methods: {
      handleLoginCansel(done) {  //登录
        this.dialogLoginVisible = false;
        this.$refs['loginForm'].resetFields();  // 清空
//        this.$confirm('确认关闭？')
//          .then(_ => {
//            done();
//          })
//          .catch(_ => {});
      },
      handleRegisterCansel(done) {  // 注册
        //
        this.dialogRegisterVisible = false;
        this.$refs['loginForm'].resetFields();  // 清空
      },
      handleLoginSubmit(){  //登录

        // 处理
        this.$refs['loginForm'].validate((valid) => {
          if (valid) {
            console.log('submit!!');

            this.$http.post('http://127.0.0.1:8000/beauty/user/login', {
              username: this.loginForm.username,
              password: this.loginForm.password,
            })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });


            this.dialogLoginVisible = false;
            this.$refs['loginForm'].resetFields();  // 清空
          } else {
            console.log('error submit!!');
            return false;
          }
        });


//        this.$refs['loginForm'].resetFields();  // 清空

      },
      handleRegisterSubmit(form){  // 注册
        // 处理
        this.dialogLoginVisible = false;
        this.$refs['loginForm'].resetFields();  // 清空
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
