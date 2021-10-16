import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
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

import addTeacher from '@/components/add/addTeacher'
import showTeacher from '@/components/show/showTeacher'
import delTeacher from '@/components/del/delTeacher'
import updateTeacher from '@/components/update/updateTeacher'

import showStudent from '@/components/show/showStudent'
import addStudent from '@/components/add/addStudent'
import updateStudent from '@/components/update/updateStudent'
import delStudent from '@/components/del/delStudent'
import sysplan from '@/components/sysplan/sysplan'
import systeach from '@/components/sysplan/systeach'
import syschoiceCourse from '@/components/syschoice/syschoiceCourse'

// import showAchievement from '@/components/show/showAchievement'
// import addAchievement from '@/components/add/addAchievement'
// import updateAchievement from '@/components/update/updateAchievement'
// import delAchievement from '@/components/del/delAchievement'

Vue.use(Router)

export default new Router({
  routes: [
    // {
      // path: '/',
      // name: 'HelloWorld',
      // component: HelloWorld
    // },
    {
      path:'/grade',
      name:'showGrade',
      component:showGrade
    },
    {
      path:'/addgrade',
      name:'addGrade',
      component:addGrade
    },
    {
      path:'/delgrade',
      name:'delGrade',
      component:delGrade
    },
    {
      path:'/updategrade',
      name:'updateGrade',
      component:updateGrade
    },
    {
      path:'/course',
      name:'showCourse',
      component:showCourse
    },
    {
      path:'/addcourse',
      name:'addCourse',
      component:addCourse
    },  
    {
      path:'/delcourse',
      name:'delCourse',
      component:delCourse
    },
    {
      path:'/updatecourse',
      name:'updateCourse',
      component:updateCourse
    },
    {
      path: '/teachplan',
      name: 'showTeachPlan',
      component: showTeachPlan
    },
    {
      path: '/addteachplan',
      name: 'addTeachPlan',
      component: addTeachPlan
    },
    {
      path: '/updateteachplan',
      name: 'updateTeachPlan',
      component: updateTeachPlan
    },
    {
      path: '/delteachplan',
      name: 'delTeachPlan',
      component: delTeachPlan
    },
    {
      path:'/teacher',
      name:'showTeacher',
      component:showTeacher
    },
    {
      path:'/addteacher',
      name:'addTeacher',
      component:addTeacher
    },
    {
      path:'/delteacher',
      name:'delTeacher',
      component:delTeacher
    },
    {
      path:'/updateteacher',
      name:'updateTeacher',
      component:updateTeacher
    },
    {
      path: '/student',
      name: 'showStudent',
      component: showStudent
    },
    {
      path: '/addStudent',
      name: 'addStudent',
      component: addStudent
    },
    {
      path: '/updateStudent',
      name: 'updateStudent',
      component: updateStudent
    },
    {
      path: '/delStudent',
      name: 'delStudent',
      component: delStudent
    },
    {
      path: '/sysgrade',
      name: 'sysgrade',
      component: showGrade
    },
    {
      path: '/syscourse',
      name: 'syscourse',
      component: showCourse,
    },
    {
      path: '/systeacher',
      name: 'systeacher',
      component: showTeacher,
    },
    {
      path: '/sysstudent',
      name: 'sysstudent',
      component: showStudent,
    },
    {
      path: '/sysplan',
      name: 'sysplan',
      component: sysplan,
    },
    {
      path: '/systeach',
      name: 'systeach' ,
      component: systeach,
    },
    {
      path: '/syschoiceCourse',
      name: 'syschoiceCourse' ,
      component: syschoiceCourse,
    }
  ]
})
