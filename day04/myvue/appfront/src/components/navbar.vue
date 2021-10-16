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
            name:"学生管理中心",
            submenuitem:[{
              path:"/student",
              name:'学生',
            },
            {
              path:'5-2',
              name:'学生信息添加'
            },
            {
              path:'5-3',
              name:'学生信息修改'
            },
            {
              path:'5-2',
              name:'学生信息删除'
            },
            ]   //submenuitem  结束
          },
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