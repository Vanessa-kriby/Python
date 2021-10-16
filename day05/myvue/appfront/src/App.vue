<template>
  <div id="app">
    <img src="./assets/logo.png">
    <navbar/>
    <router-view/>
  </div>
</template>

<script>
import consequence from '@/components/consequence/consequence'
import navbar from '@/components/navbar'
export default {
  name: 'App',
      data () {
   return {
      msg: 'Welcome to Your Vue.js App'
   }
 },
 components: {
   consequence,
   navbar, 
 }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
