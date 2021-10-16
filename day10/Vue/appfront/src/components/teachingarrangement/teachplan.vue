<template>
    <span>
        <button @click="handleadd">添加</button>
        <el-table :data="tableData" border stripe style="width :100%">

            <el-table-column prop="tpno"  label="计划编号"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-input v-model="scope.row.tpno" placeholder="请输入计划编号"></el-input>
                        </span>
                        <span v-else>
                            <span>{{scope.row.tpno}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.tpno}}</span>
                    </span>

                </template>
            </el-table-column>

            <el-table-column prop="cno" label="课程"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                            <span v-if="!btntype">
                                <el-select v-model="scope.row.cno" placeholder="请选择课程">
                                    <el-option v-for="item in courseList" :key="item.cno" :label="item.cname" :value="item.cno"></el-option>
                                </el-select>
                            </span>
                        <span v-else>
                            <span>{{scope.row.course__cname}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.course__cname}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="tno" label="教师"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-select v-model="scope.row.tno" placeholder="请选择任课教师">
                                <el-option v-for="item in teacherList" :key="item.tno" :label="item.tname" :value="item.tno"></el-option>
                            </el-select>
                        </span>
                        <span v-else>
                            <span>{{scope.row.teacher__tname}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.teacher__tname}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="dno" label="专业"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-select v-model="scope.row.dno" placeholder="请选择专业">
                                <el-option v-for="item in departmentList" :key="item.dno" :label="item.dname" :value="item.dno"></el-option>
                            </el-select>
                        </span>
                        <span v-else>
                            <span>{{scope.row.department__dname}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.department__dname}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="credit" label="学分"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                    <el-input-number v-model="scope.row.credit" :precision="2" :step="0.1"   :max="10"></el-input-number>
                    </span>
                    <span v-else>
                        <span>{{scope.row.credit}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="teach_date"  label="开课时间"  width="320">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                    <el-date-picker 
                        v-model="scope.row.teach_date" 
                        format="yyyy-MM-dd"
                        value-format="yyyy-MM-dd"
                        type="date" 
                        placeholder="选择日期"></el-date-picker>
                    </span>
                    <span v-else>
                        <span>{{scope.row.teach_date}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="evaluation_method"  label="考察方式"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <el-radio v-model="scope.row.evaluation_method" label="考试">考试</el-radio>
                        <el-radio v-model="scope.row.evaluation_method" label="考察">考察</el-radio>
                    </span>
                    <span v-else>
                        <span>{{scope.row.evaluation_method}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column label="操作"  width="400">
                <template slot-scope="scope">
                    <span v-if="!scope.row.isstatus">
                        <el-button size="small" type="primary" round @click.native="addrecord()">添加</el-button>
                        <el-button size="small" type="info" round @click.native="editrecord(scope.row,scope.$index)">编辑</el-button>
                        <el-button size="small" type="warning" round  @click.native="handledelete(scope.row,scope.$index)">删除</el-button>
                    </span>
                    <span v-else>
                      <el-button size="small" type="info" round @click.native="handleupdate(scope.row,scope.$index)">更新</el-button>
                      <el-button size="small" type="info" round @click.native="handlecancel(scope.row,scope.$index)">取消</el-button>  
                    </span>
                </template>
            </el-table-column>

        </el-table>
    </span>
</template>

<script>
export default {
    data() {
        return {
            isedit:false,
            btntype: false,
            tableData: [],
            courseList: [],
            teacherList: [],
            departmentList: [],
        }
    },
    mounted() {
        this.getCourse();
        this.getTeacher();
        this.getDepartment();
        this.getTeachPlan();
    },
    methods: {
        handledelete(row,index){
            if (this.isedit) {
                this.$message.warning("请先处理完正在编辑的内容！")
                return;
            }
            this.ondelete(row.tpno)
            this.isedit=false
            this.getTeachPlan();
        },
        handleupdate(row, index) {
            if(!this.checkcorrect(row))
                return this.$message({
                    message: "失败！" + row.tpno + row.cno + row.tno + row.dno + row.credit + row.teach_date + row.evaluation_method,
                    type: "warning"
                })
            if (!this.btntype) {
                let temp = [];
                temp.push(row)
                this.onSubmit(temp);
            } else{
                let temp = [];
                temp.push(row)
                this.onUpdate(temp);
            }
            this.isedit = false;
            this.btntype = false;
            row.isstatus = 0;
            this.tableData.splice(index,1,row)
            this.getTeachPlan();
        },
        handlecancel(row, index) {
            this.isedit = false;
            row.isstatus = 0;
            //需要判断从哪里来的
            if　(!this.btntype) {
                this.tableData.splice(index, 1);
            }
            if (this.btntype) {
                this.tableData.splice(index, 1, row);
            }
            this.btntype = false;
            this.getTeachPlan();
        },
        editrecord(row,index){
            if(this.isedit){
                this.$message.warning("请先处理完正在编辑的内容！")
                return; 
            }
            let temp = {
                tpno: row.tpno,
                cno: row.course__cno,
                tno: row.teacher__tno,
                dno: row.department__dno,
                course__cname: row.course__cname,
                department__dname: row.department__dname,
                teacher__tname: row.teacher__tname,
                credit: row.credit,
                evaluation_method: row.evaluation_method,
                teach_date: row.teach_date,
                isstatus: 1,
            };
            this.tableData.splice(index,1,temp);
            this.isedit = true;
            this.btntype = true;
        },
        // isNumber(z_check_value) {
        //   var z_reg = /^(([0-9])|([1-9]([0-9]+)))$/;
        //   if (z_reg.test(z_check_value)) {
            // return true;
        //   }
        //   return false;
        // },
        isNumber(obj) {
        var reg= /^[0-9]+.?[0-9]*$/;
        if (reg.test(obj)) {
        return true;
        }
        return false;
        },
        isDate(d_check_value) {
            var d_reg =/^((([0-9]{2})(0[48]|[2468][048]|[13579][26]))|((0[48]|[2468][048]|[13579][26])00)-02-29)|([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))$/;
            if(d_reg.test(d_check_value)) {
                return true;
            }
            return false;
        },
        checkcorrect(item) {
          var iscorrect=true
        //    数据正确性校验
          if(item.tpno == "") {
              return false;
          }
          if (!this.isNumber(item.tpno)) {
            return false;
          }
        //   if (item.sno == null) {
            // return false;
        //   }
        //   if (!this.isNumber(item.sno)) {
            // return false;
        //   }
          if (item.credit == "0.0") {
            return false;
          }
          if (!this.isNumber(item.credit)) {
            return false;
          }
          if (item.teach_date == null) {
            return false;
          }
          if (item.evaluation_method == "") {
            return false;
          }
          if (!this.isDate(item.teach_date)) {
            return false;
          }
            return true;
        },
        addrecord() {
            if (this.isedit) {
                this.$message.success("请先处理完正在编辑的内容！")
                return; 
            }
            this.handleadd();
            this.isedit = true;
            this.btntype = false;
            
        },
        handleadd() {
            let temp = {
                tpno: "",
                cno: "",
                tno: "",
                dno:"",
                credit: "",
                evaluation_method: "",
                teach_date:"",
                isstatus:1

            };
            this.tableData.push(temp)
        },       
        getCourse() {
            this.axios.get('http://127.0.0.1:8000/app2/showCourses').then((response)=>{
                this.courseList=response.data.data
                console.log(this.courseList)
            });
        },
        getTeacher() {
            this.axios.get('http://127.0.0.1:8000/app3/showTeachers').then((response)=>{
                this.teacherList=response.data.data
                console.log(this.teacherList)
            });
        },
        getDepartment() {
            this.axios.get('http://127.0.0.1:8000/app1/showDepartments').then((response)=>{
                this.departmentList=response.data.data
                console.log(this.departmentList)
            });
        },
        getTeachPlan() {
            this.axios.get('http://127.0.0.1:8000/app4/showTeachPlans').then((response) => {
                this.tableData=response.data.data
                console.log(this.tableData)
                // if(this.tableData.length == 0) {
                //   let obj = {
                    // tpno: "",
                    // cno: "",
                    // tno: "",
                    // dno:"添加新数据",
                    // credit: "",
                    // evaluation_method: "",
                    // teach_date:"",
                    // isstatus:1
                //   };
                //   this.tableData.push(obj);
                // }
            })
        },
        onSubmit(data) {
            this.axios
            .post("http://127.0.0.1:8000/app4/addTeachPlans", { data, })
            .then(response => {
              // this.listData = response.data.data;
              // console.log(this.listData)
              if (response.data.err_num == 1) {
                this.$message({
                  message: "失败！" + response.data.msg,
                  type: "warning"
                });
              }
              if (response.data.err_num == 0) {
                this.$message({
                  message: "添加成功！",
                  type: "warning"
                });
              }
            });
            this.getTeachPlan()
        },
        onUpdate(data) {
            this.axios
            .post("http://127.0.0.1:8000/app4/updateTeachPlan", { data, })
            .then(response => {
              // this.listData = response.data.data;
              // console.log(this.listData)
              if (response.data.err_num == 1) {
                this.$message({
                  message: "失败！" + response.data.msg,
                  type: "warning"
                });
              }
              if (response.data.err_num == 0) {
                this.$message({
                  message: "添加成功！",
                  type: "warning"
                });
              }
            });
            this.getTeachPlan()
        },
        ondelete(tpno) {
            let data={tpno}
            this.axios
            .post("http://127.0.0.1:8000/app4/delTeachPlan", { data, })
            .then(response => {
              // this.listData = response.data.data;
              // console.log(this.listData)
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
            }); 
            this.getTeachPlan();
        },
    }
}
</script>