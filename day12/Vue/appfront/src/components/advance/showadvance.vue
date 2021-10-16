<template>
    <span>
        <button @click="handleadd">添加</button>
        <el-table :data="tableData" border stripe style="width :100%">

            <el-table-column prop="ano"  label="预排课程编号"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-input v-model="scope.row.ano" placeholder="请输入预排课程编号"></el-input>
                        </span>
                        <span v-else>
                            <span>{{scope.row.ano}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.ano}}</span>
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

            <el-table-column prop="crno" label="教室"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-select v-model="scope.row.crno" placeholder="请选择教室">
                                <el-option v-for="item in classroomList" :key="item.crno" :label="item.crno" :value="item.crno"></el-option>
                            </el-select>
                        </span>
                        <span v-else>
                            <span>{{scope.row.classroom__crno}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.classroom__crno}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="starttime" label="课程开始时间"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                    <el-time-picker
                        arrow-control
                        v-model="scope.row.starttime"
                        :picker-options="{
                          selectableRange: '00:00:00 - 24:00:00'
                        }"
                        placeholder="任意时间点">
                    </el-time-picker>
                    </span>
                    <span v-else>
                        <span>{{scope.row.starttime}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="endtime"  label="课程结束时间"  width="320">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                    <el-date-picker 
                        v-model="scope.row.endtime" 
                        format="yyyy-MM-dd"
                        value-format="yyyy-MM-dd"
                        type="date" 
                        placeholder="选择日期"></el-date-picker>
                    </span>
                    <span v-else>
                        <span>{{scope.row.endtime}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="week"  label="星期"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <el-radio v-model="scope.row.week" label="考试">考试</el-radio>
                        <el-radio v-model="scope.row.week" label="考察">考察</el-radio>
                    </span>
                    <span v-else>
                        <span>{{scope.row.week}}</span>
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
            classroomList: [],
        }
    },
    mounted() {
        this.getCourse();
        this.getTeacher();
        this.getClassroom();
        this.getAdvance();
    },
    methods: {
        handledelete(row,index){
            if (this.isedit) {
                this.$message.warning("请先处理完正在编辑的内容！")
                return;
            }
            this.ondelete(row.ano)
            this.isedit=false
            this.getAdvance();
        },
        handleupdate(row, index) {
            if(!this.checkcorrect(row))
                return this.$message({
                    message: "失败！" + row.ano + row.cno + row.tno + row.crno + row.starttime + row.endtime + row.week,
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
            this.getAdvance();
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
            this.getAdvance();
        },
        editrecord(row,index){
            if(this.isedit){
                this.$message.warning("请先处理完正在编辑的内容！")
                return; 
            }
            let temp = {
                ano: row.ano,
                cno: row.course__cno,
                tno: row.teacher__tno,
                crno: row.classroom__crno,
                course__cname: row.course__cname,
                classroom__crno: row.classroom__crno,
                teacher__tname: row.teacher__tname,
                starttime: row.starttime,
                week: row.week,
                endtime: row.endtime,
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
          if(item.ano == "") {
              return false;
          }
          if (!this.isNumber(item.ano)) {
            return false;
          }
        //   if (item.sno == null) {
            // return false;
        //   }
        //   if (!this.isNumber(item.sno)) {
            // return false;
        //   }
          if (item.starttime == "") {
            return false;
          }
        //   if (!this.isNumber(item.starttime)) {
        //     return false;
        //   }
          if (item.endtime == null) {
            return false;
          }
          if (item.week == "") {
            return false;
          }
        //   if (!this.isDate(item.endtime)) {
        //     return false;
        //   }
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
                ano: "",
                cno: "",
                tno: "",
                crno:"",
                starttime: "",
                week: "",
                endtime:"",
                isstatus:1

            };
            this.tableData.push(temp)
        },       
        getCourse() {
            this.axios.get('http://127.0.0.1:8000/app4/showCourses').then((response)=>{
                this.courseList=response.data.data
                console.log(this.courseList)
            });
        },
        getTeacher() {
            this.axios.get('http://127.0.0.1:8000/app5/showTeachers').then((response)=>{
                this.teacherList=response.data.data
                console.log(this.teacherList)
            });
        },
        getClassroom() {
            this.axios.get('http://127.0.0.1:8000/app3/showclassrooms').then((response)=>{
                this.classroomList=response.data.data
                console.log(this.classroomList)
            });
        },
        getAdvance() {
            this.axios.get('http://127.0.0.1:8000/app1/showAdvance').then((response) => {
                this.tableData=response.data.data
                console.log(this.tableData)
                // if(this.tableData.length == 0) {
                //   let obj = {
                    // ano: "",
                    // cno: "",
                    // tno: "",
                    // crno:"添加新数据",
                    // starttime: "",
                    // week: "",
                    // endtime:"",
                    // isstatus:1
                //   };
                //   this.tableData.push(obj);
                // }
            })
        },
        onSubmit(data) {
            this.axios
            .post("http://127.0.0.1:8000/app1/addAdvance", { data, })
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
            this.getAdvance()
        },
        onUpdate(data) {
            this.axios
            .post("http://127.0.0.1:8000/app1/updateAdvance", { data, })
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
            this.getAdvance()
        },
        ondelete(ano) {
            let data={ano}
            this.axios
            .post("http://127.0.0.1:8000/app1/delAdvance", { data, })
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
            this.getAdvance();
        },
    }
}
</script>