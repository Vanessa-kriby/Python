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
            name:"系统设置",
            submenuitem:[{
              path:"/sysgrade",
              name:'班级基本信息',
            },
            {
              path:'/syscourse',
              name:'课程基本信息'
            },
            {
              path:'/systeacher',
              name:'教师基本信息'
            },
            {
              path:'/sysstudent',
              name:'学生基本信息'
            },
            ]   //submenuitem  结束
          },
          {
            id:2,
            name:"教学中心",
            submenuitem: [
              {
                path: "/sysplan",
                name:"教学计划"
              },
              {
                path: "/systeach",
                name:"教学任务"
              }
            ]
          },
          {
            id:3,
            name:"网上选课",
            submenuitem: [
              {
                path: "/syschoiceCourse",
                name: "学生选课"
              }
            ]
          }
        ]     //menudatalist  结束
      };
    },
    methods: {
       handleSelect(key, keyPath) {
        // console.log(key, keyPath);
        console.log(typeof(key))
        if(key=="showStudent"){
            this.showStudent()
        }
        else if(key=="showTeacher"){
            this.showteacher()
          }
        else if(key=="showAchievement"){
            this.showAchievement()
        }
        else if(key=="showGrade"){
            this.showgrade()
        }
        else if(key=="showCourse"){
            this.showcourse()
        }
        else if(key=="showTeachPlan"){
            this.showteachPlan()
        }
        
      },
    }
  }
</script>