<template>
    <el-form ref="form" :model="form" label-width="80px">
       
        <el-form-item label="班级编号">
        <el-input v-model="form.gid"></el-input>
        </el-form-item>

        <el-form-item label="班级名称">
        <el-input v-model="form.gname"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即修改</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
export default {
    data(){
        return{
            form:{
                gid:'',
                gname:'',
            }
        }
    },
    mounted(){

    },
    methods:{
        onSubmit(){
            console.log(this.form);
            var data=this.form
            this.axios.post('http://127.0.0.1:8000/app1/updateGrade',{
               data
            }).then((response)=>{
                this.listData=response.data.data
                console.log(response)
            })
        },
    }
}
</script>>