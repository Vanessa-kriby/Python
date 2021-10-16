import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

import consequence from '@/components/consequence/consequence'
import Department from '@/components/department/Department'
import Course from '@/components/course/Course'
import teachPlan from '@/components/teachplan/teachPlan'
import student from '@/components/student/student'
import teacher from '@/components/teacher/teacher'
import teaching from '@/components/teaching/teaching'
Vue.use(Router)

export default new Router({
  routes: [
    // {
      // path: '/',
      // name: 'HelloWorld',
      // component: HelloWorld
    // }
    {
      path: '/consequence',
      name: 'consequence',
      component:consequence
    },
    {
      path:'/department',
      name: 'Department',
      component: Department
    },
    {
      path: '/course',
      name: 'Course',
      component: Course
    },
    {
      path:'/teachplan',
      name:'teachPlan',
      component:teachPlan
    },
    {
      path:'/student',
      name:'student',
      component:student
    },
    {
      path:'/teacher',
      name:'teacher',
      component:teacher
    },
    {
      path: '/teaching',
      name: 'teaching',
      component: teaching
    },
  ]
})
