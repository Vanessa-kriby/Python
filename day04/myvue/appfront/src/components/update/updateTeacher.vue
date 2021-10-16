<template>
        <el-form ref="form" :model="form" label-width="80px">

        <el-form-item label="教师编号">
            <el-input v-model="form.teid"></el-input>
        </el-form-item>

        <el-form-item label="教师名字">
            <el-input v-model="form.teName"></el-input>
        </el-form-item>

        <el-form-item label="教师性别">
            <el-input v-model="form.teGender"></el-input>
        </el-form-item>

        <el-form-item label="教师职称">
            <el-input v-model="form.tejobTitle"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建/修改</el-button>
            <el-button>取消</el-button>
        </el-form-item>
        </el-form>
  </template>


<script>
export default {
    data(){
        return{
            form:{
                teid:'',
                teName:'',
                teGender:'',
                tejobTitle:'',

            }
        }
    },
    mounted(){

    },
    methods:{
        onSubmit(){
            console.log(this.form);
            var data=this.form
            this.axios.post('http://127.0.0.1:8000/app4/addTeachers',{
                data
            }),then((response)=>{
                this.listData=response.data.data
                console.log(response)
            })
        },
    }
}
</script>