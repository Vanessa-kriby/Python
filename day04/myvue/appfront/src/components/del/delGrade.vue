<template>
    <el-form ref="from" :model="listData" label-width="80px">
        <el-form-item  label="班级">
            <el-select v-model="listData.gid" placeholder="请选择要删除的班级">
                <el-option
                    v-for="item in gradevalue"
                    :key="item.gno"
                    :label="item.gname"
                    :value="item.gno">
                </el-option>
            </el-select>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即删除</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
export default {
    data(){
        return{
            listData:[],
            gradevalue:[],
            listData:{
                gid:"",
            }
        }
    },
    mounted(){
        this.getlistGrade()
    },
    methods:{
        onSubmit:function(){
            var data=this.listData
            console.log(data);
            //   http://127.0.0.1:8000/delStudent?sid=2019001
            this.axios.post('http://127.0.0.1:8000/app1/delGrade',{data})
            .then((response)=>{
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getlistGrade:function (){
             this.axios.get('http://127.0.0.1:8000/app1/showGrades').then((response)=>{
                    this.gradevalue=response.data.data
                    })
                    .catch(function (error) {
                    console.log(error);   
                    })
        },
    },
}
</script>>
    
    