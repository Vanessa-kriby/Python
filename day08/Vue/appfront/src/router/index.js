import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import teachplan from '@/components/teachingarrangement/teachplan'
import showDepartment from '@/components/syssetup/showDepartment'
import showCourse from '@/components/syssetup/showCourse'
import showStudent from '@/components/syssetup/showStudent'
import showTeacher from '@/components/syssetup/showTeacher'
import studentcurriculum from '@/components/curriculumprovision/studentcurriculum'
import choiceCourse from '@/components/courseselection/choiceCourse'
import delChoice from '@/components/courseselection/delChoice'
import teachercurriculum from '@/components/curriculumprovision/teachercurriculum'

Vue.use(Router)

export default new Router({
  routes: [
    // {
      // path: '/',
      // name: 'HelloWorld',
      // component: HelloWorld
    // },
    {
      path: '/teachplan',
      name: 'teachplan',
      component: teachplan
    },
    {
      path: '/department',
      name: 'showDepartment',
      component: showDepartment
    },
    {
      path: '/course',
      name: 'showCourse',
      component: showCourse
    },
    {
      path: '/student',
      name: 'showStudent',
      component: showStudent
    },
    {
      path: '/teacher',
      name: 'showTeacher',
      component: showTeacher
    },
    {
      path: '/studentcurriculum',
      name: 'studentcurriculum',
      component: studentcurriculum
    },
    {
      path: '/choiceCourse',
      name: 'choiceCourse',
      component: choiceCourse,
    },
    {
      path: '/delChoice',
      name: 'delChoice',
      component: delChoice,
    },
    {
      path: '/teachercurriculum',
      name: 'teachercurriculum',
      component: teachercurriculum
    },
  ]
})
