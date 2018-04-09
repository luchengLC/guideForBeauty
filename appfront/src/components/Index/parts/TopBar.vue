<template>
  <div style="margin: 0; padding: 0">
    <el-menu
      :default-active="activeIndex2"
      class="el-menu"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ff8080">
      <el-menu-item class="el-menu-item" index="1">美妆商品导购系统</el-menu-item>
      <el-menu-item class="el-menu-item" index="2">我的降价通知商品</el-menu-item>
      <el-menu-item class="el-menu-item" id="logout" index="3">{{login_out}}</el-menu-item>
      <el-menu-item class="el-menu-item" id="name-login" index="4">{{user_name}}</el-menu-item>

    </el-menu>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App',
        user_name: '登录',
        login_out: '注册',
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .el-menu {
    .el-menu-item {
      height: 30px;
      line-height: 30px;
    }

    #name-login, #logout {
      float: right;
    }

  }
</style>
