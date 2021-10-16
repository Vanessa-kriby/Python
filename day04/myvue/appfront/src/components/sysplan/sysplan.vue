<template>
    <span>
        <button @click="addme">添加</button>
        <el-table :data="tableData" border stripe style="width :100%">
            <el-table-column prop="cno" label="课程编号"  width="240">
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

            <el-table-column prop="gno" label="班级编号"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-select v-model="scope.row.gno" placeholder="请选择班级">
                                <el-option v-for="item in gradeList" :key="item.gno" :label="item.gname" :value="item.gno"></el-option>
                            </el-select>
                        </span>
                        <span v-else>
                            <span>{{scope.row.grade__gname}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.grade__gname}}</span>
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

            <el-table-column prop="checkType"  label="考察方式"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                    <el-input v-model="scope.row.checkType" placeholder="请输入内容"></el-input>
                    </span>
                    <span v-else>
                        <span>{{scope.row.checkType}}</span>
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
            myisedit:false,
            btntype: false,
            tableData: [],
            courseList: [],
            gradeList: [],
            tno:"",
            tgno:"",
            tchecktype:"",
            tteach_date:"",
            tcredit:"",
        }
    },
    mounted() {
        this.getGrade();
        this.getCourse();
        this.getTeachPlan();
    },
    methods: {
        handledelete(row,index){
            if (this.myisedit) {
                this.$message.warning("请先处理完正在编辑的内容！")
                return;
            }
            this.ondelete(row.course__cno,row.grade__gno)
            this.myisedit=false
            this.getTeachPlan();
        },
        editrecord(row,index){
            if(this.myisedit){
                this.$message.warning("请先处理完正在编辑的内容！")
                return; 
            }
            let temp = {
                cno: row.course__cno,
                gno: row.grade__gno,
                course__cname: row.course__cname,
                grade__gname: row.grade__gname,
                credit: row.credit,
                checkType: row.checkType,
                teach_date: row.teach_date,
                isstatus: 1,
            };
            this.tableData.splice(index,1,temp);
            this.myisedit = true;
            this.btntype = true;
        },
        handleupdate(row, index) {
            if (!this.btntype) {
                let temp = [];
                temp.push(row)
                this.onSubmit(temp);
            } else{
                let temp = [];
                temp.push(row)
                this.onUpdate(temp);
            }
            this.myisedit = false;
            this.btntype = false;
            row.isstatus = 0;
            // this.tableData.splice(index,1,row)
            this.getTeachPlan();
        },
        handlecancel(row, index) {
            this.myisedit = false;
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
        addrecord() {
            if (this.myisedit) {
                this.$message.success("请先处理完正在编辑的内容！")
                return; 
            }
            this.addme();
            this.myisedit = true;
            this.btntype = false;
            
        },
        addme() {
            let temp = {
                cno: "",
                gno:"",
                credit: "2.0",
                checkType: "考试",
                teach_date:"2020-08-16",
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
        getGrade() {
            this.axios.get('http://127.0.0.1:8000/app1/showGrades').then((response)=>{
                this.gradeList=response.data.data
                console.log(this.gradeList)
            });
        },
        getTeachPlan() {
            this.axios.get('http://127.0.0.1:8000/app3/showTeachPlans').then((response) => {
                this.tableData=response.data.data
                console.log(this.tableData)
            })
        },
        onSubmit(data) {
            this.axios
            .post("http://127.0.0.1:8000/app3/addTeachPlans", { data, })
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
        },
        onUpdate(data) {
            this.axios
            .post("http://127.0.0.1:8000/app3/updateTeachPlan", { data, })
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
            this.getTeachPlan();
        },
        ondelete(cno,gno) {
            let data={cno:cno,gno:gno}
            this.axios
            .post("http://127.0.0.1:8000/app3/delTeachPlan", { data, })
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
        },

    }
}
</script>