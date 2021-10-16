<template>
   <el-menu :default-active="activeIndex" router class="el-menu-demo" mode="horizontal" @select="handleSelect">
     <el-submenu v-for="(data,i) in menudatalist" :key="data.id" :index="i+''">
       <template slot="title">{{data.name}}</template>
       <el-menu-item v-for="(item,j) in data.submenuitem" :key="i*4+j" :index="item.path">{{item.name}}</el-menu-item>
     </el-submenu>

</el-menu>

</template>

<script>
  export default {
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        menudatalist:[
          {
            id:1,
            name:"教务管理",
            submenuitem:[{
              path:"/consequence",
              name:'成绩管理',
            },
            {
              path: "/department",
              name:"专业",
            },
            {
              path: "/course",
              name:"课程",
            },
            {
              path: "/teachplan",
              name: "教学计划",
            },
            {
              path:"/student",
              name:"学生信息管理中心",
            },
            {
              path:"/teacher",
              name:"师资队伍",
            },
            {
              path: '/teaching',
              name: '教学安排',
            },
            ]   //submenuitem  结束
          },
          {
            id:2,
            name:"教师登录入口",
            submenuitem:[{
              path:"/showteacher",
              name:'教师个人信息查询',
            },
            ]   //submenuitem  结束
          },
          {
            id:3,
            name:"学生登录入口",
            submenuitem:[{
              path:"/showstudent",
              name:'学生个人信息查询',
            },
            ]   //submenuitem  结束
          },
        ]     //menudatalist  结束
      };
    },
    methods: {
        consequence(){
        },
       handleSelect(key, keyPath) {
        // console.log(key, keyPath);
        console.log(typeof(key))
        if(key=="consequence"){
            this.consequence()
        }
        // else if(key=="showTeacher"){
            // this.showteacher()
        //   }
        // else if(key=="showAchievement"){
            // this.showAchievement()
        // }
        // else if(key=="showGrade"){
            // this.showgrade()
        // }
        // else if(key=="showCourse"){
            // this.showcourse()
        // }
        // else if(key=="showTeachPlan"){
            // this.showteachPlan()
        // }
        
      },
    }
  }
</script>