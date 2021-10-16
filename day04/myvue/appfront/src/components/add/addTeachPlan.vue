<template>
<el-form ref="form" :model="listData" label-width="80px">
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

    <el-form-item label="班级">
        <el-select v-model="listData.gra" placeholder="请选择班级">
            <el-option
            v-for="item in gradevalue"
            :key="item.gno"
            :label="item.gname"
            :value="item.gno">
            </el-option>
        </el-select>

    </el-form-item>

    <el-form-item label="学分">
        <el-input v-model="listData.cri"></el-input>
        </el-form-item>
        <!-- </el-form-item> -->

    <el-form-item label="开课时间">
        <el-input v-model="listData.teadate"></el-input>
        </el-form-item>

    <el-form-item label="考查方式">
        <el-input v-model="listData.checktype"></el-input>
        </el-form-item>
        
    <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
        </el-form-item>
        </el-form>
   </template>
<script>
    export default {
        data() {
            return {
                listData:[],
                coursevalue:[],
                gradevalue:[],
                listData:{
                    cid:"",
                    gra:"",
                    cri:"",
                    teadate:"",
                    checktype:"",
                }
            }
        },
        mounted() {
            this.getlistCourse()
            this.getlistGrade()
        },
        methods: {
            onSubmit:function(){
            var data=this.listData
            console.log(data)
            this.axios.post('http://127.0.0.1:8000/app3/addTeachPlans', {data})
            .then(response =>{

            })
            .catch(function (error) {
                    console.log(error);
            });
            },
            getlistCourse:function(){
                this.axios.get('http://127.0.0.1:8000/app2/showCourses')
                .then(response => {
                    this.coursevalue = response.data.data
                })
                .catch(function (error) {
                    console.log(error);
                })
            },
             getlistGrade:function(){
                this.axios.get('http://127.0.0.1:8000/app1/showGrades')
                .then(response => {
                    this.gradevalue = response.data.data
                })
                .catch(function (error) {
                    console.log(error);
                })
            },
        },
    }
    </script>
