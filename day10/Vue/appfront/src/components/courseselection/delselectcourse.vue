<template>
    <div>
        <table border="0" align="center" v-show="!ifSuccess">
            <tr>
                <td>
                    <span>第一步:</span>
                </td>
                <td>
                    <el-input v-model="sno" placeholder="输入你的学号"></el-input>
                </td>
            </tr>
            <tr>
                <td colspan="2" align="center">
                    <el-button type="primary" @click="onSubmit()">提交</el-button>
                </td>
            </tr>
        </table>

        <span v-show="ifSuccess">
                <el-header style="text-algin:center; font-size: 12px">
                    <i class="el-icon-setting" style="margin-right: 15px"></i>
                    <span><h3 style="display:inline-block;">{{students.sname}}</h3>欢迎前来查看课程结果！</span>
                </el-header>
                <el-table :data="dataList" stripe style="width: 100%">
                    <el-table-column prop="ino" label="清单编号"></el-table-column>
                    <el-table-column prop="teachPlan__course__cname" label="专业课程"></el-table-column>
                    <el-table-column prop="teachPlan__teacher__tname" label="任课教师"></el-table-column>
                    <el-table-column prop="teachPlan__teach_date" label="开课日期"></el-table-column>
                    <el-table-column prop="teachPlan__credit" label="学分"></el-table-column>
                    <el-table-column prop="teachPlan__evaluation_method" label="考察方式"></el-table-column>

                    <el-table-column label="操作"  width="400">
                        <template slot-scope="scope">
                            <span>
                                <el-button size="small" type="warning" round  @click.native="ondelete(scope.row,scope.$index)">删除</el-button>
                            </span>
                        </template>
                    </el-table-column>
                </el-table>
        </span>
    </div>
</template>

<script>
export default {
    data() {
        return {
            sno:"",
            ifSuccess:false,
            dataList:[],
            // resultData:[],
            students:{},
            // ino:"",
        }
    },
    methods:{
        onSubmit() {
            // if(this.checkcorrect(this.sno)) {
                let sno = this.sno;
                this.axios
                    .get("http://127.0.0.1:8000/app5/retriveStudent", {
                        params: {  sno },
                    })
                    .then(response => {
                          // this.listData = response.data.data;
                          if (response.data.err_num == 0) {
                              this.ifSuccess = true;
                              this.students = response.data.data
                              this.coursecurriculum();
                          } else {
                              this.$message.warning("请输入正确的学号并再次尝试，谢谢！");
                              this.sno = "";
                          }
                        })
                        .catch((error) => {
                            // this.$message.warning(error);
                            console.log(error)
                        });
            // } else {
            //     this.$message.warning("错误！");
            // }                       
        },
        coursecurriculum(){
        let sno=this.sno;
        this.axios
            .get(" http://127.0.0.1:8000/app5/showStudentCourse",{
                params: { sno },
            })
            .then((response) => {
              if (response.data.err_num == 0) {
            this.dataList = response.data.data;
          } else {
            this.$message.warning("错误!");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
        },
        ondelete(ino) {
            let data =ino
            this.axios
            .post("http://127.0.0.1:8000/app5/delStudentCourse", { data })
            .then(response => {
              if (response.data.err_num == 1) {
                this.$message({
                  message: "失败！" + response.data.msg,
                  type: "warning"
                });
              }
              if (response.data.err_num == 0) {
                this.$message({
                  message: "删除成功！",
                  type: "success"
                });
              }
              this.coursecurriculum();
            }); 
        },
    },
}
</script>