import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import showadvance from '@/components/advance/showadvance'
import showDepartment from '@/components/syssetup/showDepartment'
import showCourse from '@/components/syssetup/showCourse'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/advance',
      name: 'showadvance',
      component: showadvance
    },
    {
      path:'/department',
      name: 'showDepartment',
      component: showDepartment
    },
    {
      path: '/course',
      name: 'showCourse',
      component: showCourse
    },
  ]
})
