<template>
  <span>
    <!-- <el-button @click="add">添加一条信息</el-button>
    <el-button @click="confirm">确定</el-button>
    <el-button @click="onSub">提交数据</el-button> -->
    <el-table :data="tableData" style="width: 100%" :model="listD">

      <el-table-column prop="department_id" label="专业编号" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.department_id"></el-input>
          <div v-else>{{scope.row.department_id}}</div>
        </template>
      </el-table-column>

      <el-table-column prop="course_id" label="课程编号" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.course_id"></el-input>
          <div v-else>{{scope.row.course_id}}</div>
        </template>
      </el-table-column>

      <!-- <el-table-column prop="department_id" label="专业编号" width="180">  
      <el-select v-model="listD.dno" clearable placeholder="请选择专业">
        <el-option
          v-for="item in departmentvalue"
          :key="item.dno"
          :label="item.dno"
          :value="item.dno">
        </el-option>
      </el-select>
      </el-table-column>

      <el-table-column prop="course_id" label="课程编号" width="180">
      <el-select
        v-model="listD.cno"
        clearable
        collapse-tags
        style="margin-left: 20px;"
        placeholder="请选择课程">
        <el-option
          v-for="item in coursevalue"
          :key="item.cno"
          :label="item.cname"
          :value="item.cno">
        </el-option>
      </el-select>
      </el-table-column> -->

      <el-table-column prop="credit" label="学分" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.credit"></el-input>
          <div v-else>{{scope.row.credit}}</div>
        </template>
      </el-table-column>

      <el-table-column prop="teach_date" label="开课时间" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.teach_date"></el-input>
          <div v-else>{{scope.row.teach_date}}</div>
        </template>
      </el-table-column>

      <el-table-column prop="evaluation_method" label="考核方式" width="180">
        <template slot-scope="scope">
          <!-- <el-input v-if="scope.row.status" v-model="scope.row.evaluation_method"></el-input> -->
          <span v-if="scope.row.status">
            <el-radio v-model="scope.row.evaluation_method" label="考试">考试</el-radio>
            <el-radio v-model="scope.row.evaluation_method" label="考勤">考勤</el-radio>
          </span>
          <div v-else>{{scope.row.evaluation_method}}</div>
        </template>
      </el-table-column>

      <el-table-column label="操作" width="280" header-align="center">
        <template slot-scope="scope">
          <span v-show="showBtnAdd[scope.$index]">
            <el-button size="mini" @click.native="handleCancel(scope.$index, scope.row)">取消</el-button>  <!--index是行 row是数组-->
            <el-button size="mini" @click.native="handleUpdate(scope.$index, scope.row)">更新</el-button>
          </span>
          <span v-show="!showBtnAdd[scope.$index]">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" @click="handleAdd(scope.$index, scope.row)">添加</el-button>
            <el-button
              size="mini"
              type="danger"
              @click="delTeacher(scope.$index, scope.row)"
              v-show="!showBtn[scope.$index]"
            >删除</el-button>
          </span>
        </template>
      </el-table-column>
    </el-table>
    <!-- <el-col span="24">
      <div class="el-table-add-row" style="width: 99.2%;" @click="add()"><span>+ 添加</span></div>
    </el-col> -->
  </span>
</template>

  <script>
export default {
  // inject: ['reload'],      强制更新页面
  data() {
    return {
      tableData: [],
      showBtn: [], //记录当前行是否选中编辑
      showBtnAdd: [], //记录当前添加的位置
      // department_id:"",
      // course_id:"",
      // credit:"",
      // teach_date:"",
      join: [], //替代updateDate
      departmentvalue:[],
      coursevalue:[],
      listD:{
        deid:"",
        couid:"",
      }
    };
  },

  mounted() {
    this.getTeacher();
    this.getlistDepartment();
    this.getlistCourse();
  },

  methods: {
    add() {
      this.tableData.push({
        department_id: "",
        course_id: "",
        credit: "",
        teach_date: "",
        evaluation_method: "",
        status: 1,
      });
    }, //无问题

    isNumber(obj) {
      var numRe = /^[0-9]+$/;
      if (!numRe.test(obj)) {
        return true;
      }
      return false;
    }, //无问题

    checkcorrect(item) {
      //校验数据的正确性
      if (item.course_id == null) {
        return false;
      }

      // if (this.isNumber(item.department_id)) {
      //   return false;
      // }

      if (item.credit == null) {
        return false;
      }

      if (item.teach_date == null) {
        return false;
      }

      let teaName = item.course_id.trim();
      if (!(teaName.length > 0 && teaName.length < 50)) {
        return false;
      }

      return true;
    }, //checkcorrect结束   无问题

    confirm() {
      this.tableData.map((item) => {
        if (item.status) {
          if (!this.checkcorrect(item))
            return this.$message({
              message: "失败!" + item.department_id,
              type: "waring",
            });
          item.status = 0;
          let BB = new Object();
            BB.deid = item.department_id;
            BB.couid = item.course_id;
            BB.cre = item.credit;
            BB.tdate = item.teach_date;
            BB.method = item.evaluation_method
          this.join.push(BB);
        }
        return item;
      });
    }, //无问题

    handleAdd(index, row) {
      let BB = new Object();
        BB.department_id = "";
        BB.course_id = "";
        BB.credit = "";
        BB.teach_date = "";
        BB.evaluation_method = "";
        BB.status = 1;
      this.tableData.splice(index, 0, BB);
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
    }, // 无问题

    //编辑
    handleEdit(index, row) {
      // alert(index)
      // alert(row.department_id)
      // alert(row.course_id)
      // alert(row.credit)
      // alert(row.teach_date)
      let BB = new Object();
        BB.department_id = row.department_id;
        BB.course_id = row.course_id;
        BB.credit = row.credit;
        BB.teach_date = row.teach_date;
        BB.evaluation_method = row.evaluation_method;
        BB.status = 1;
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.tableData.splice(index, 1, BB);
      this.showBtn[index] = true; //找到插入点
      this.$set(this.showBtn, BB, true);
      // alert(BB.course_id)
      // this.editDialogVisible = true;
    }, //无问题
    //删除
    delTeacher(index, row) {
      // alert(index)
      // alert(row.department_id)
      // alert(row.course_id)
      // alert(row.credit)
      // alert(row.teach_date)
      var BB = new Object();
        BB.deid = row.department_id;
        BB.couid = row.course_id;
      var data = BB;
      console.log(data);
      //   http://127.0.0.1:8000/delTeacher?deid=111
      this.axios
        .post("http://127.0.0.1:8000/app4/delTeachPlan", { data })
        .then((response) => {
          if (response.data.err_num == 1) {
            this.$message({
              message: "失败!" + response.data.msg,
              type: "warning",
            });
          }
          if (response.data.err_num == 0) {
            this.$message({
              message: "删除成功!" + response.data.msg,
              type: "warning",
            });
            this.tableData.splice(index, 1);
            this.showBtn[index] = false;
            this.$set(this.showBtn, row, false);
          }
        });
    },
    handleCancel(index, row) {
      // alert(row.course_id);
      if (this.showBtnAdd[index] && !this.showBtn[index]) { 

        this.tableData.splice(index, 1);
        this.showBtn[index] = false;
        this.$set(this.showBtn, row, false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      if (this.showBtn[index] && this.showBtnAdd[index]) {
        
        row.status = 0;
        this.tableData.splice(index, 1, row);
        // alert(index);
        // alert(row.department_id);
        this.showBtn[index] = false;
        this.$set(this.showBtn, row, false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      this.getTeacher()
    },
    handleUpdate(index, row) {
      // alert(row.department_id);
      if (!this.checkcorrect(row))
      return this.$message({
        message: "添加失败! 教师姓名:" + row.department_id + row.course_id,
        type: "warning",
      });
      let BB = new Object();
        BB.deid = row.department_id;
        BB.couid = row.course_id;
        BB.cre = row.credit;
        BB.tdate = row.teach_date;
        BB.method = row.evaluation_method;

      let BBB = []
      BBB.push(BB)
      this.onSubmit(BBB);
      this.handleCancel(index, row);
      row.status = 0;
      this.tableData.splice(index, 1, row);
      // this.reload()  强制刷新页面
      this.getTeacher
    },

    getTeacher: function (event) {
      this.axios
        .get("http://127.0.0.1:8000/app4/showTeachPlans")
        .then((response) => {
          this.tableData = response.data.data;
          console.log(this.tableData);
          if (this.tableData.length == 0) {
            let obj ={
              course:"",
              department:"",
              credit:"",
              teach_date: "",
              evaluation_method:"",
              status:0,
            };
            this.tableData.push(obj);
          }
        });
    }, //无问题
    onSubmit(data) {
      // var data = this.join;
      // console.log(data);

      this.axios
        .post("http://127.0.0.1:8000/app4/addTeachPlans", {
          data,
        })
        .then((response) => {
          
          if (response.data.err_num == 1) {
            this.$message({
              message: "失败!" + response.data.msg,
              type: "warning",
            });
          }
          if (response.data.err_num == 0) {
            this.$message({
              message: "添加成功!",
              type: "warning",
            });
          }
          this.listData = response.data.data;
        });
    },
    onSub() {
      var data = this.join;
      console.log(data);

      this.axios
        .post("http://127.0.0.1:8000/app4/addTeachPlans", {
          data,
        })
        .then((response) => {
          this.listData = response.data.data;
          if (response.data.err_num == 1) {
            this.$message({
              message: "失败!" + response.data.msg,
              type: "warning",
            });
          }
          if (response.data.err_num == 0) {
            this.$message({
              message: "添加成功!",
              type: "warning",
            });
          }
        });
    },
    getlistDepartment:function (){
             this.axios.get('http://127.0.0.1:8000/app2/showDepartments').then((response)=>{
                    this.departmentvalue=response.data.data
                    // console.log(this.gradevalu)
                    })
                    .catch(function (error) {
                    console.log(error);   
                    })
    },
    getlistCourse:function (){
             this.axios.get('http://127.0.0.1:8000/app3/showCourses').then((response)=>{
                    this.coursevalue=response.data.data
                    // console.log(this.gradevalu)
                    })
                    .catch(function (error) {
                    console.log(error);   
                    })
        },
    // reset() {
    //   console.log('123')
    //   this.tableData
    // }
    // handleback(){
    //   console.log("back")
    // }
  },
};
</script>
