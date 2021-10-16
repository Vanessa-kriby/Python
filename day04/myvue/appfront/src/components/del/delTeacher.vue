<template>
    <el-form ref="from" :model="listData" label-width="80px">
        <el-form-item  label="教师">
            <el-select v-model="listData.teid" placeholder="请选择要删除的教师">
                <el-option
                    v-for="item in teachervalue"
                    :key="item.tno"
                    :label="item.tname"
                    :value="item.tno">
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
            teachervalue:[],
            listData:{
                teid:"",
            }
        }
    },
    mounted(){
        this.getlistTeacher()
    },
    methods:{
        onSubmit:function(){
            var data=this.listData
            console.log(data);
            //   http://127.0.0.1:8000/delTeacher?teid=111
            this.axios.post('http://127.0.0.1:8000/app4/delTeacher',{data})
            .then((response)=>{
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getlistTeacher:function (){
             this.axios.get('http://127.0.0.1:8000/app4/showTeachers').then((response)=>{
                    this.teachervalue=response.data.data
                    // console.log(this.gradevalu)
                    })
                    .catch(function (error) {
                    console.log(error);   
                    })
        },
    },
}
</script>
    