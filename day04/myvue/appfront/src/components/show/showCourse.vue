<template>
    <el-table
      :data="listData"
      style="width: 100%">
      <el-table-column
        prop="cno"
        label="课程编号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="cname"
        label="课程名称"
        width="180">
      </el-table-column>
      <el-table-column
        prop="textBook"
        label="课程教材名称"
        width="180">
      </el-table-column>
    </el-table>
  </template>

  <script>
        export default {
            data() {
            return {
                 listData: [],
                 cno:"",
                 cname:"",
                 textBook:"",
            }
         },
            mounted(){
                this.getCourse()
            },
            methods:{
            getCourse: function (event){
                this.axios.get('http://127.0.0.1:8000/app2/showCourses').then((response)=>{
                    this.listData=response.data.data
                    console.log(this.listData)
                })
            },
        },
    }
    </script>    