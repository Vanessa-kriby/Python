<template>
    <div>
        <table border="0" align="center" v-show="!ifSuccess">
            <tr>
                <td>
                    <span>第一步:</span>
                </td>
                <td>
                    <el-input v-model="studentNum" placeholder="输入你的学号"></el-input>
                </td>
            </tr>
            <tr>
                <td colspan="2" align="center">
                    <el-button type="primary" @click="onSubmit()">提交</el-button>
                </td>
            </tr>
        </table>

        <span v-show="ifSuccess">
            <el-container>
                <el-header style="text-algin:center; font-size: 12px">
                    <i class="el-icon-setting" style="margin-right: 15px"></i>
                    <span><h3 style="display:inline-block;">{{students.sname}}</h3>欢迎选课!</span>
                </el-header>

                <el-main>
                    <el-row type="flex" justify="center" align>
                        <el-transfer
                        style="text-align: left; display: inline-block"
                        filterable
                        v-model="resultData"
                        :data="selectCourse"
                        :titles="['可选课程', '所选课程']"
                        :button-texts="['移动到可选','移动到所选']">
                        </el-transfer>
                    </el-row>
                    <el-row>
                        <el-row type="flex" justify="center" align>
                            <el-button type="info" @click="submitCourse()" round>提交</el-button>
                        </el-row>
                    </el-row>
                </el-main>
            </el-container>
            <!-- <el-transfer v-model="resultData" :data="dataList"></el-transfer> -->
        </span>
    </div>
</template>

<script>
export default {
    data() {
        return {
            studentNum:"",
            ifSuccess:false,
            dataList:[],
            resultData:[],
            students:{},
        }
    },
    computed:{
        selectCourse() {
            const data=[];
            this.dataList.forEach((item,i) =>{
                data.push({
                    key:i,
                    label: `${item.cno} ${item.cname} ${item.teacher__tname}   ${item.teachplan__credit}`,
                    disabled:false,
                });
            });
            return data;
        }
    },
    methods: {
        submitCourse() {
            let tdata=[]
            this.resultData.forEach((i) => {
                // console.log(this.dataList[i].cno)
                tdata.push(this.dataList[i].cno)
            })
            console.log(tdata);
            let data = {
                sno:'',
                cons:[],
            }
            data.sno=this.students.sno
            data.cons=tdata
            this.axios
                    .post("http://127.0.0.1:8000/app5/postStudentCourse", { data })
                    .then(response => {
                      // this.listData = response.data.data;
                      if (response.data.err_num == 0) {
                        //   this.ifSuccess =true;
                        //   this.students=response.data.data;
                        //   this.courseFilter();
                        this.$message.success("选课成功!")
                      } else {
                          this.$message.warning("错误！");
                          this.studentNum = "";
                      }
                    })
                    .catch((error) => {
                        this.$message.warning(error);
                    });
        },
        courseFilter() {
            let studentNum = this.studentNum;       
            this.axios
                .get("http://127.0.0.1:8000/app5/retriveCourse",{ params: {  studentNum },})
                .then((response) => {
                  // this.listData = response.data.data;
                  if (response.data.err_num == 0) {
                      this.dataList = response.data.data;
                  } else {
                      this.$message.warning("错误！");
                  }
                })
                .catch((error) => {
                    this.$message.warning("error");
                });
        },
        isNumber(z_check_value) {
            var z_reg = /^(([0-9])|([1-9]([0-9]+)))$/;
            if (z_reg.test(z_check_value)) {
              return true;
            }
            return false;
        },
        checkcorrect(item) {
            // var iscorrect=true
            //  数据正确性校验
            if (item == null) {
              return false;
            }
            if (!this.isNumber(item)) {
              return false;
            }
            let tname = item.trim();
            if (!(tname.length > 0 && tname.length < 20)) {
                return false;
            }
            return true;
        },
        onSubmit() {
            if(this.checkcorrect(this.studentNum)) {
                let studentNum = this.studentNum;
                this.axios
                    .get("http://127.0.0.1:8000/app5/retriveStudent", {
                        params: {  studentNum },
                    })
                    .then(response => {
                          // this.listData = response.data.data;
                          if (response.data.err_num == 0) {
                              this.ifSuccess = true;
                              this.students = response.data.data
                              this.courseFilter();
                          } else {
                              this.$message.warning("错误！");
                              this.studentNum = "";
                          }
                        })
                        .catch((error) => {
                            // this.$message.warning(error);
                            console.log(error)
                        });
            } else {
                this.$message.warning("错误！");
            }
        }
    }
}
</script>

<style >

</style>