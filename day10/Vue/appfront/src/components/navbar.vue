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
                submenuitem:[
                    {
                        path: "/department",
                        name:"专业基本信息"
                    },
                    {
                        path: "/course",
                        name:"课程基本信息",
                    },
                    {
                        path: "/student",
                        name:"学生基本信息"
                    },
                    {
                        path: "/teacher",
                        name:"教师基本信息"
                    },
                ]
            },
            {
                id:2,
                name:"教学安排",
                submenuitem:[{
                    path: "/teachplan",
                    name:"教学计划"
                }] 
            },
            {
                id:3,
                name:"网上选课",
                submenuitem:[
                    {
                      path: "/selectcourse",
                      name: "学生选课",
                    },
                    {
                      path: "/delselectcourse",
                      name: "取消选课",
                    },
                ] 
            },
            {
                id:4,
                name:"课程查询",
                submenuitem:[{
                    path:"/studentcurriculum",
                    name:"学生课程查询",
                },
                {
                path: '/teachercurriculum',
                name: '教师任课信息查询',
                }] 
            },
            {
                id:5,
                name:"教师评分",
                submenuitem:[{
                    path:"/pointsscoring",
                    name:"教师评分",
                }] 
            },
        ]  //menudatalist  结束
       } 
    },
    methods: {
        handleSelect(key,keyPath) {
            // console.log(key, keyPath);
            console.log(typeof(key))
        }
    }
}
</script>