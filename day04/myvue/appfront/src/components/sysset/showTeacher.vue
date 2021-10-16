<template>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="tno"
        label="工号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="tname"
        label="老师名字"
        width="180">
      </el-table-column>
      <el-table-column
        prop="gender"
        label="老师性别"
        width="180">
      </el-table-column>
      <el-table-column
        prop="jobTitle"
        label="老师职称"
        width="180">
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      data() {
        return {
          tableData:[],

        }
      },
      mounted() {
          this.getTeacher()
      },
      
      methods: {
          getTeacher: function (event) {
              this.axios.get('http://127.0.0.1:8000/app4/showTeachers').then((response) =>{ 
                this.tableData=response.data.data
                console.log(this.tableData)
              })
          },
      },
    }
  </script>
