<template>
  <span>
    <!-- <el-button @click="add">添加一条数据</el-button> -->
    <!-- <el-button @click="confirm(),onSubmit(updateData)">确认添加</el-button> -->
    <el-table :data="listData" style="width:100%">
        <el-table-column prop="studentDepartment__dno" label="专业" width="180">
        <template slot-scope="scope">
            <span v-if="scope.row.status">
                <span v-if=" !btntype">
            <el-select v-model="scope.row.studentDepartment__dno" placeholder="请选择">
          <el-option v-for="item in departmentlist" :key="item.dno" :label="item.dname" :value="item.dno"></el-option>
          </el-select>
          </span>
          <span v-else>
              <span>{{scope.row.studentDepartment__dname}}</span>
              </span>
              </span>
              <span v-else>
              <span>{{scope.row.studentDepartment__dname}}</span>
              </span>
        </template>
      </el-table-column>

       
        <el-table-column prop="sno" label="学生编号" width="180">
        <template slot-scope="scope">
            <span v-if="scope.row.status">
                <span v-if=" !btntype">
           <el-input v-if="scope.row.status" v-model="scope.row.sno"></el-input>
          </span>
          <span v-else>
              <span>{{scope.row.sno}}</span>
              </span>
              </span>
              <span v-else>
              <span>{{scope.row.sno}}</span>
              </span>
        </template>
      </el-table-column>

      <!-- <el-table-column prop="sno" label="学生编号" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.sno"></el-input>
          <span v-else>{{scope.row.sno}}</span>
        </template>
      </el-table-column> -->

      <el-table-column prop="sname" label="学生名称" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.sname"></el-input>
          <span v-else>{{scope.row.sname}}</span>
        </template>
      </el-table-column>

      <el-table-column prop="sgender" label="学生性别" width="180">
        <template slot-scope="scope">
          <span v-if="scope.row.status">
            <el-radio v-model="scope.row.sgender" label="男">男</el-radio>
            <el-radio v-model="scope.row.sgender" label="女">女</el-radio>
          </span>
          <div v-else>{{scope.row.sgender}}</div>
        </template>
      </el-table-column>

        <el-table-column label="操作" width="400">
          <template slot-scope="scope">
              <span v-if="!scope.row.status">
        <el-button size="small" type="primary" round @click.native="addrecord()">添加</el-button>
       <el-button size="small" type="info" round @click.native="editrecord(scope.row,scope.$index)">编辑</el-button>
       <el-button size="small" type="warning" round @click.native="handledelete(scope.row,scope.$index)">删除</el-button>
              </span>
         <span v-else>
       <el-button size="small" type="info" round @click="handleupdate(scope.row,scope.$index)">更新</el-button>
       <el-button size="small" type="warning" round @click.native="handlecancel(scope.row,scope.$index)">取消</el-button>
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
      myisedit: false,
      btntype: false,
      listData: [],
      updateData: [],
      showBtn: [],
      showBtnAdd: [],
      departmentlist:[],
      studentDepartment__dno: "",
      sno: "",
      sname: "",
      sgender: "",
    };
  },
  mounted() {
    this.getStudent();
    this.getDepartment();
  },
  methods: {

     isNumber(obj) {
      var numreg = /^[0-9]+$/;
      if (numreg.test(obj)) {
        return true;
      }
      return false;
    },
    checkcorrect(item) {
      if (item.studentDepartment__dname == " ") {
        return false;
      }
      if (item.sname == " ") {
        return false;
      }
      if (item.sno == " ") {
        return false;
      }
      
      if (!this.isNumber(item.sno)) {
        return false;
      }
      let sgen = item.sgender.trim();
      if (!(sgen.length > 0 && sgen.length < 50)) {
        return false;
      }

      let sname = item.sname.trim();
      if (!(sname.length > 0 && sname.length < 50)) {
        return false;
      }
      return true;
    },

     handledelete(row, index) {
        if(this.myisedit) {
            this.$message.success("请处理所编辑的内容!");
            return;
        };
        this.ondelete(row.sno)
        this.myisedit=false
        this.getStudent();
    },
    

    editrecord(row, index){
        if(this.myisedit){
            this.$message.success("请处理所编辑的内容!");
            return;
        };
        
        let temp = {
            studentDepartment__dno:row.studentDepartment__dno,
            studentDepartment__dname:row.studentDepartment__dname,
            sno:row.sno,
            sname:row.sname,
            sgender:row.sgender,
            
            status:1,
        };
        this.listData.splice(index, 1, temp);
        this.myisedit = true;
        this.btntype = true;
    },
    
    handleupdate(row, index) {
       this.myisedit = false;
      if (!this.checkcorrect(row))
        return this.$message({
          message: "失败" + row.sno + row.sname+row.sgender,
          type: "warning",
        });
        if(!this.btntype) {
            let temp = [];
            temp.push(row);
            this.onSubmit(temp);
        } else {
            let temp = [];
            temp.push(row);
            this.onUpdate(temp);
        }
        this.myisedit = false;
        this.btntype = false;
        row.status = 0;
        this.getStudent();

     },
    

    handlecancel(row, index) {
        this.myisedit = false;
        row.status = 0;
        if(!this.btntype) {
            this.listData.splice(index, 1);
        }
        if(this.btntype) {
            this.listData.splice(index,1,row);
        }
        this.btntype=false;
        row.status = 0;
        this.getStudent();
    },

    addrecord() {
        if(this.myisedit) {
            this.$message.success("请处理所编辑的内容!");
            return;
        }
        this.addme();
        this.myisedit = true;
        this.btntype = false;
        
    },
        addme() {
            let temp = {
                    studentDepartment__dno: "",
                    sno: "",
                    sname: "",
                    sgender: "",
                    status: 1,
            };
            this.listData.push(temp);
            
        
    },

    getDepartment:function(event){
                this.axios.get('http://127.0.0.1:8000/app2/showDepartments')
                .then((response) => {
                    this.departmentlist = response.data.data;
                    console.log(this.departmentlist);
                });
                
            },
             
   
    getStudent() {
      this.axios
        .get("http://127.0.0.1:8000/app5/showStudents")
        .then((response) => {
          this.listData = response.data.data;
          console.log(this.listData);
          if(this.listData.length == 0) {
            this.addme();
          }
        });
    }, 

     onSubmit:function(data){
            
            this.axios.post('http://127.0.0.1:8000/app5/addStudents', {data})
            .then(response =>{
              this.$message.success("成功!")
            })
            .catch(function (error) {
            console.log(error);
            });
        //      this.axios
        // .post("http://127.0.0.1:8000/app5/addStudents", { data })
        // .then((response) => {
        //   this.listData = response.data.data;
        //   if (response.data.err_num == 1) {
        //     this.$message({
        //       message: "失败！" + response.data.msg,
        //       type: "warning",
        //     });
        //   }
        //   if (response.data.err_num == 0) {
        //     this.$message({
        //       message: "成功！",
        //       type: "warning",
        //     });
        //   }
        // });
           this.getStudent();
        },

        ondelete(sno){
            let data={sno:sno}
            this.axios.post("http://127.0.0.1:8000/app5/delStudent", {data})
            .then((response) => {
                this.$message.success("删除成功!")
                this.listData=response.data.data
            })
            .catch(function (error){
                console.log(error)
            });
          this.getStudent();
        
     },

     onUpdate(data){
            
            this.axios.post("http://127.0.0.1:8000/app5/updateStudent", {data})
            .then((response) => {
                this.$message.success("更新成功!")
               
            })
            .catch(function (error){
                console.log(error)
            });
          this.getStudent();
        
     },

  }
};

  
</script>   

