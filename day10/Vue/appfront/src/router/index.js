import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import showDepartment from '@/components/sysset/showDepartment'
import showCourse from '@/components/sysset/showCourse'
import showTeacher from '@/components/sysset/showTeacher'
import showStudent from '@/components/sysset/showStudent'
import teachplan from '@/components/teachingarrangement/teachplan'
import selectcourse from '@/components/courseselection/selectcourse'
import studentcurriculum from '@/components/curriculumprovision/studentcurriculum'
import teachercurriculum from '@/components/curriculumprovision/teachercurriculum'
import delselectcourse from '@/components/courseselection/delselectcourse'
import pointsscoring from '@/components/pointsscoring/pointsscoring'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
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
      path: '/teacher',
      name: 'showTeacher',
      component: showTeacher
    },
    {
      path: '/student',
      name: 'showStudent',
      component: showStudent
    },
    {
      path: '/teachplan',
      name: 'teachplan',
      component: teachplan
    },
    {
      path: '/selectcourse',
      name: 'selectcourse',
      component: selectcourse
    },
    {
      path: '/studentcurriculum',
      name: 'studentcurriculum',
      component: studentcurriculum
    },
    {
      path: '/teachercurriculum',
      name: 'teachercurriculum',
      component: teachercurriculum
    },
    {
      path: '/delselectcourse',
      name: 'delselectcourse',
      component: delselectcourse
    },
    {
      path: '/pointsscoring',
      name: 'pointsscoring',
      component: pointsscoring
    },
  ]
})
