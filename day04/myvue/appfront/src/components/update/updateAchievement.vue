<template>

<el-form ref="form" :model="listData" label-width="80px">

<el-form-item label="学生">
     <el-select v-model="listData.sid" placeholder="请选择学生">
    <el-option
      v-for="item in studentvalue"
      :key="item.sno"
      :label="item.sname"
      :value="item.sno">
    </el-option>
    </el-select>
</el-form-item>

<el-form-item label="课程">
     <el-select v-model="listData.cid" placeholder="请选择课程">
    <el-option
      v-for="item in coursevalue"
      :key="item.cno"
      :label="item.cname"
      :value="item.cno">
    </el-option>
    </el-select>
</el-form-item>

<el-form-item label="获得学分">
    <el-input v-model="listData.sco"></el-input>
</el-form-item>

<el-form-item label="获得日期">
    <el-input v-model="listData.gaindata"></el-input>
</el-form-item> 

<el-form-item>
    <el-button type="primary" @click="onSubmit">立即修改</el-button>
    <el-button>取消</el-button>
</el-form-item>

</el-form>

</template>

<script>
  export default {
    data() {
      return {
        studentvalue:[],
        coursevalue:[],
        listData:{
          sid:"",
          cid:"",
          sco:"",
          gaindata:"",
        }
      }
    },
    mounted(){
      this.getlistStudent()
      this.getlistCourse()
    },
    methods: {
      onSubmit:function(){
        var _this=this
        var data=_this.listData
        console.log(data)
        this.axios.post('http://127.0.0.1:8000/app6/updateAchievement',{
            data
        }).then((response)=>{
        })
        .catch(function(error){
          console.log(error);
        });
      
      },
      getlistStudent:function(){
        this.axios.get('http://127.0.0.1:8000/app5/showStudents')
        .then((response)=>{
          this.studentvalue=response.data.data
        })
        .catch(function(error){
          console.log(error);
        })
      },
      getlistCourse:function(){
        this.axios.get('http://127.0.0.1:8000/app2/showCourses')
        .then((response)=>{
          this.coursevalue=response.data.data
        })
        .catch(function(error){
          console.log(error);
        })
      },
    }
  }
</script>