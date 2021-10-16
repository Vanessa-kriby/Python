<template>
  <div id="app">
    <img src="./assets/logo.png">
    <navbar/>
    <router-view/>
    <!-- <showStudent/> -->
    <!-- <addStudent/> -->
    <!-- <updateStudent/> -->
    <!-- <delStudent/> -->
    
  </div>
</template>

<script>
import showGrade from '@/components/show/showGrade'
import addGrade from '@/components/add/addGrade'
import delGrade from '@/components/del/delGrade'
import updateGrade from '@/components/update/updateGrade'

import showCourse from '@/components/show/showCourse'
import addCourse from '@/components/add/addCourse'
import delCourse from '@/components/del/delCourse'
import updateCourse from '@/components/update/updateCourse'

import showTeachPlan from '@/components/show/showTeachPlan'
import addTeachPlan from '@/components/add/addTeachPlan'
import updateTeachPlan from '@/components/update/updateTeachPlan'
import delTeachPlan from '@/components/del/delTeachPlan'

import showTeacher from '@/components/show/showTeacher'
import addTeacher from '@/components/add/addTeacher'
import delTeacher from '@/components/del/delTeacher'
import updateTeacher from '@/components/update/updateTeacher'

import showStudent from '@/components/show/showStudent'
import addStudent from '@/components/add/addStudent'
import updateStudent from '@/components/update/updateStudent'
import delStudent from '@/components/del/delStudent'

import addAchievement from '@/components/add/addAchievement'
import showAchievement from '@/components/show/showAchievement'
import updateAchievement from '@/components/update/updateAchievement'
import delAchievement from '@/components/del/delAchievement'

import navbar from '@/components/sysset/navbar'
export default {
  name: 'App',
    data () {
   return {
      msg: 'Welcome to Your Vue.js App'
   }
 },
 components: {
   showGrade,
   addGrade,
   delGrade,
   updateGrade,

   showCourse,
   addCourse,
   delCourse,
   updateCourse,
   
   showTeachPlan,
   addTeachPlan,
   delTeachPlan,
   updateTeachPlan,

   showTeacher,
   addTeacher,
   delTeacher,
   updateTeacher,

   showStudent,
   addStudent,
   updateStudent,
   delStudent,

   addAchievement,
   showAchievement,
   delAchievement,
   updateAchievement,
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
