<template>
    <el-form ref="from" :model="listData" label-width="80px">
        <el-form-item  label="课程">
            <el-select v-model="listData.couid" placeholder="请选择要删除的课程">
                <el-option
                    v-for="item in coursevalue"
                    :key="item.cno"
                    :label="item.cname"
                    :value="item.cno">
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
            coursevalue:[],
            listData:{
                couid:"",
                
            }
        }
    },
    mounted(){
        this.getlistCourse()
    },
    methods:{
        onSubmit:function(){
            var data=this.listData
            console.log(data);
            //   http://127.0.0.1:8000/delCourse?couid=001
            this.axios.post('http://127.0.0.1:8000/app2/delCourse',{data})
            .then((response)=>{
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getlistCourse:function (){
             this.axios.get('http://127.0.0.1:8000/app2/showCourses').then((response)=>{
                    this.coursevalue=response.data.data
                    // console.log(this.gradevalu)
                    })
                    .catch(function (error) {
                    console.log(error);   
                    })
        },
    },
}
</script>>
    