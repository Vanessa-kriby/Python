<template>
    <el-form ref="form" :model="form" label-width="80px">
       
        <el-form-item label="课程编号">
        <el-input v-model="form.couid"></el-input>
        </el-form-item>

        <el-form-item label="课程名称">
        <el-input v-model="form.couname"></el-input>
        </el-form-item>

        <el-form-item label="教材名称">
        <el-input v-model="form.coubook"></el-input>
        </el-form-item>


        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
export default {
    data(){
        return{
            form:{
                couid:'',
                couname:'',
                coubook:'',
        
            }
        }
    },
    mounted(){

    },
    methods:{
         onSubmit(){
            console.log(this.form);
            var data=this.form
            //   http://127.0.0.1:8000/app1/addCourses?couid=001&couname=高等数学1&coubook=xxx
            this.axios.post(' http://127.0.0.1:8000/app2/addCourses',{
               data
            }).then((response)=>{
                this.listData=response.data.data
                console.log(response)
            })
        },
    }
}
</script>>
    
