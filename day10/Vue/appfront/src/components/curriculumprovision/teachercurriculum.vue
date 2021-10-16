<template>
    <div>
        <table border="0" align="center" v-show="!ifSuccess">
            <tr>
                <td><span>第一步</span></td>
                <td><el-input v-model="tno" placeholder="请输入您的工号"></el-input></td>
            </tr>
            <tr>
                <td colspan="2" align="center"><el-button type="primary" @click="onSubmit()">提交</el-button></td>
            </tr>
        </table>

        <span v-show="ifSuccess">
            <el-header style="text-algin:center; font-size: 12px">
                    <i class="el-icon-setting" style="margin-right: 15px"></i>
                    <span><h3 style="display:inline-block;">{{teachers.tname}}</h3>欢迎前来查看课程结果！</span>
                </el-header>
            <el-table :data="teachList" stripe style="width: 100%">
                <!-- <el-table-column prop="teachPlan__teacher__tno" label="教师工号" width="180"></el-table-column> -->
                <!-- <el-table-column prop="teachPlan__teacher__tname" label="教师姓名" width="180"></el-table-column> -->
                <el-table-column prop="teachPlan__course__cname" label="所教课程" width="180"></el-table-column>
                <el-table-column prop="teachPlan__department__dname" label="所教专业" width="180"></el-table-column>
                <el-table-column prop="teachPlan__teach_date" label="开课日期" width="180"></el-table-column>
                <el-table-column prop="teachPlan__credit" label="学分" width="180"></el-table-column>
                <el-table-column prop="student__sname" label="选课学生" width="180"></el-table-column>
            </el-table>
        </span>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                tno:"",
                ifSuccess:false,
                teachList:[],
                teachers:{},
            };
        },
        methods:{
            teachcourseFilter(){
            
                let tno=this.tno;
                this.axios
                    .get("http://127.0.0.1:8000/app3/teachCourse",{
                        params:{tno},
                    })
                    .then((response)=>{
                        // console.log(response.data.err_num);
                        if(response.data.err_num==0){
                            this.teachList=response.data.data
                        }else{
                            this.$message.warning("错误");
                        }
                    })
                    .catch(function(error){
                        console.log(error)
                    });
                
            },
            isNumber(obj){
                var numreg=/^[0-9]+$/;
                if (numreg.test(obj)){
                    return true;
                }
                return false
            },
            checkcorrect(item){
                if(item==null){
                    return false;
                }
                if(!this.isNumber(item)){
                    return false;
                }
                let tname=item.trim();
                if(!(tname.length>0 && tname.length<20)){
                    return false;
                }
                return true;
            },
            onSubmit(){
                if(this.checkcorrect(this.tno)){
                    let tno=this.tno;
                    this.axios
                    .get("http://127.0.0.1:8000/app3/retrieveTeacher",{
                        params:{tno},
                    })
                    .then((response)=>{
                        if(response.data.err_num==0){
                            this.ifSuccess=true;
                            this.teachers = response.data.data
                            this.teachcourseFilter();
                        }else{
                            this.$message.warning("请输入正确的工号");
                            this.tno="";
                        }
                    })
                    .catch(function(error){
                        console.log(error)
                    });
                }else{
                    this.$message.warning("错误！");
                }
            },
        },
    };

</script>