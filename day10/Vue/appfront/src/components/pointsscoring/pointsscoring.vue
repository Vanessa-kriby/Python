<template>
    <span>
        <button @click="handleadd">添加</button>
        <el-table :data="tableData" border stripe style="width :100%">

            <el-table-column prop="ino"  label="清单编号"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-select v-model="scope.row.ino" placeholder="请选择课程">
                                <el-option v-for="item in InventoryList" :key="item.ino" :label="item.ino" :value="item.ino"></el-option>
                            </el-select>
                        </span>
                        <span v-else>
                            <span>{{scope.row.ino}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.ino}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="cno" label="课程"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                            <span v-if="!btntype">
                                <el-select v-model="scope.row.teachPlan__course__cno" placeholder="请选择课程">
                                    <el-option v-for="item in InventoryList" :key="item.teachPlan__course__cno" :label="item.teachPlan__course__cname" :value="item.teachPlan__course__cno"></el-option>
                                </el-select>
                            </span>
                        <span v-else>
                            <span>{{scope.row.teachPlan__course__cname}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.teachPlan__course__cname}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="dno" label="专业"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-select v-model="scope.row.teachPlan__department__dno" placeholder="请选择专业">
                                <el-option v-for="item in InventoryList" :key="item.teachPlan__department__dno" :label="item.teachPlan__department__dname" :value="item.teachPlan__department__dno"></el-option>
                            </el-select>
                        </span>
                        <span v-else>
                            <span>{{scope.row.teachPlan__department__dname}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.teachPlan__department__dname}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="sno" label="学生"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-select v-model="scope.row.student__sno" placeholder="请选择学生">
                                <el-option v-for="item in InventoryList" :key="item.student__sno" :label="item.student__sname" :value="item.student__sno"></el-option>
                            </el-select>
                        </span>
                        <span v-else>
                            <span>{{scope.row.student__sname}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.student__sname}}</span>
                    </span>
                </template>
            </el-table-column>

            <el-table-column prop="score" label="分数"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                    <el-input-number v-model="scope.row.score" :precision="2" :step="0.5"   :max="100"></el-input-number>
                    </span>
                    <span v-else>
                        <span>{{scope.row.score}}</span>
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

            <el-table-column prop="tno" label="阅卷教师"  width="240">
                <template slot-scope="scope">
                    <span v-if="scope.row.isstatus">
                        <span v-if="!btntype">
                            <el-select v-model="scope.row.tno" placeholder="请选择阅卷教师">
                                <el-option v-for="item in teacherList" :key="item.tno" :label="item.tname" :value="item.tno"></el-option>
                            </el-select>
                        </span>
                        <span v-else>
                            <span>{{scope.row.tname}}</span>
                        </span>
                    </span>
                    <span v-else>
                        <span>{{scope.row.tname}}</span>
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
            teacherList: [],
            InventoryList:[],
        }
    },
    mounted() {
        this.getInventory();
        this.getTeacher();
    },
    methods: {
        handledelete(row,index){
            if (this.isedit) {
                this.$message.warning("请先处理完正在编辑的内容！")
                return;
            }
            this.ondelete(row.ino)
            this.isedit=false
            this.getInventory();
        },
        handleupdate(row, index) {
            if(!this.checkcorrect(row))
                return this.$message({
                    message: "失败！" + row.ino + row.teachPlan__course__cno + row.tno + row.teachPlan__department__dname + row.credit + row.teach_date + row.evaluation_method,
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
            this.getInventory();
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
            this.getInventory();
        },
        editrecord(row,index){
            if(this.isedit){
                this.$message.warning("请先处理完正在编辑的内容！")
                return; 
            }
            let temp = {
                ino: row.ino,
                teachPlan__course__cno: row.teachPlan__course__cno,
                teacher__tno: row.teacher__tno,
                student__sno:row.student__sno,
                teachPlan__department__dname: row.teachPlan__department__dname,
                teachPlan__course__cname: row.teachPlan__course__cname,
                teacher__tname: row.teacher__tname,
                score:row.score,
                credit:row.credit,
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
        checkcorrect(item) {
          var iscorrect=true
        //    数据正确性校验
          if(item.ino == "") {
              return false;
          }
          if (!this.isNumber(item.ino)) {
            return false;
          }
          if (item.student__sno == "") {
            return false;
          }
          if (!this.isNumber(item.student__sno)) {
            return false;
          }
          if (item.score < "0.0") {
            return false;
          }
          if (!this.isNumber(item.score)) {
            return false;
          }
          if (item.credit < "0.0") {
            return false;
          }
          if (!this.isNumber(item.credit)) {
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
                ino: "",
                inventory__teachPlan__course__cno: "",
                teacher__tno: "",
                student__sno:"",
                inventory__teachPlan__department__dno:"",
                score:"",
                credit: "",
                isstatus:1

            };
            this.tableData.push(temp)
        },       
        getInventory() {
            this.axios.get('http://127.0.0.1:8000/app6/showInventorys').then((response)=>{
                this.InventoryList=response.data.data
                console.log(this.InventoryList)
            });
        },
        getTeacher() {
            this.axios.get('http://127.0.0.1:8000/app3/showTeachers').then((response)=>{
                this.teacherList=response.data.data
                console.log(this.teacherList)
            });
        },
        // getDepartment() {
            // this.axios.get('http://127.0.0.1:8000/app1/showDepartments').then((response)=>{
            //     this.departmentList=response.data.data
            //     console.log(this.departmentList)
        //     });
        // },
        onSubmit(data) {
            this.axios
            .post("http://127.0.0.1:8000/app7/addPointsScorings", { data, })
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
                  type: "success"
                });
              }
            });
            this.getInventory()
        },
        onUpdate(data) {
            this.axios
            .post("http://127.0.0.1:8000/app7/updatePointsScoring", { data, })
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
                  type: "success"
                });
              }
            });
            this.getInventory()
        },
        ondelete(ino) {
            let data={ino}
            this.axios
            .post("http://127.0.0.1:8000/app7/delPointsScoring", { data, })
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
            this.getInventory();
        },
    }
}
</script>