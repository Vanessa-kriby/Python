<template>
    <el-table
      :data="listData"
      style="width: 100%">
      <el-table-column
        prop="student_id"
        label="学生编号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="course_id"
        label="课程编号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="score"
        label="获得学分"
        width="180">
      </el-table-column>
      <el-table-column
        prop="gain_date"
        label="获得日期"
        width="180">
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      data() {
        return {
          listData:[],
        }
      },
      mounted(){
        this.getAchievement()
      },
      methods:{
        getAchievement:function(event){
         this.axios.get('http://127.0.0.1:8000/app6/showAchievements').then((response) => {
           this.listData=response.data.data
           console.log(this.listData)
            })
        },
      },
    }
  </script>