<template>
    <el-table
      :data="tableData"
      style="width: 100%">

      <el-table-column
        prop="course_id"
        label="课程编号"
        width="180">
      </el-table-column>

      <el-table-column
        prop="grade_id"
        label="年级"
        width="180">
      </el-table-column>

      <el-table-column
        prop="credit"
        label="学分"
        width="180">
      </el-table-column>

      <el-table-column
        prop="teach_date"
        label="开课时间"
        width="180">
      </el-table-column>

      <el-table-column
        prop="checkType"
        label="考查方式"
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
              this.getGrade()
          },
          methods: {
              getGrade: function(event){
                  this.axios.get('http://127.0.0.1:8000/app3/showTeachPlans').then((response) => {
                      this.tableData=response.data.data
                      console.log(this.tableData)
                  })
              },
          },
      }

 </script>