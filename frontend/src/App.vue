<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <el-header class="header">
      <h1 class="title">GoodReader</h1>
      <p class="brief">Never bother to read the full text any more! Time to free your eyes!</p>
    </el-header>
    <el-container class='container'>
      <el-aside class='aside'>
        <select-part></select-part>
      </el-aside>
      <el-main class='main'>
        <display-part></display-part>
      </el-main>
    </el-container>
    <!-- <router-view/> -->
  </div>
</template>

<script>
import selectPart from './components/aside.vue'
import displayPart from './components/display.vue'
import global_ from './components/global'

export default {
  name: 'App',
  components: {
    selectPart,
    displayPart
  },
  computed: {
    resData () {
      console.log(global_.getData());
      return global_.getData();
    }
  }
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.container {
  width: 80%;
  margin: 30px 10%;
}

.header {
  text-align: center;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;

}

.title {
  margin-top: 0px !important;
  margin-bottom: 0px !important;  
}

.brief {
  font-style: italic;
  font-weight: 600;
  margin-top: 0px;
  margin-bottom: 0px;
}

.aside {
  width: 33% !important;
  height: 400px;
  background-color: antiquewhite;
}

.main {
  margin-left: 10px;
  background-color: bisque;
}
</style>
