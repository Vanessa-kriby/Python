<template>
  <span>
    <!-- <el-button @click="add">添加学生信息</el-button> -->
    <!-- <el-button @click="confirm(),onSubmit(updateData)">确认添加</el-button> -->
    <el-table :data="listData" stripe style="width: 100%" >
    <!-- <el-button @click="update">修改学生信息</el-button> -->
    <!-- <el-button @click="onSubmit">保存</el-button> -->
    
       <el-table-column prop="cno" label="课程" width="240">
          <template slot-scope="scope">
              <span v-if="scope.row.status">
                  <span v-if="!showBut">
                      <el-select v-model="scope.row.cno" placeholder="请选择课程">
                        <el-option
                          v-for="item in coursevalue"
                          :key="item.cno"
                          :label="item.cname"
                          :value="item.cno">
                        </el-option>
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
    
        <el-table-column prop="sno" label="学生" width="240">
          <template slot-scope="scope">
              <span v-if="scope.row.status">
                  <span v-if="!showBut">
                      <el-select v-model="scope.row.sno" placeholder="请选择学生">
                        <el-option
                          v-for="item in studentvalue"
                          :key="item.sno"
                          :label="item.sname"
                          :value="item.sno">
                        </el-option>
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
      
      <el-table-column prop="score" label="分数" width="240">
        <template slot-scope="scope">
          <span v-if="scope.row.status">
              <el-input-number v-model="scope.row.score" :precision="2" :step="0.1"   :max="10"></el-input-number>
          </span>
          <span v-else>
              <span>{{scope.row.score}}</span>
          </span>
        </template>
      </el-table-column>

      <el-table-column prop="gain_date" label="结课时间" width="180">
        <template slot-scope="scope">
          <span v-if="scope.row.status">
              <el-date-picker 
                  v-model="scope.row.gain_date" 
                  format="yyyy-MM-dd"
                  value-format="yyyy-MM-dd"
                  type="date" 
                  placeholder="选择日期"></el-date-picker>
          </span>
          <span v-else>
              <span>{{scope.row.gain_date}}</span>
          </span>
        </template>
      </el-table-column>

      <el-table-column fixed="right" label="操作" width="500" header-align="center">
        <template slot-scope="scope">
          <span v-if="!scope.row.status">
            <el-button type="primary" size="small" round @click.native="handleCreate(scope.$index, scope.row)">添加</el-button>
            <el-button type="info" size="small" round @click.native="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button type="warning" size="small" round @click.native="handleDelete(scope.$index, scope.row)" v-if="!showBtn[scope.$index]">删除</el-button>
          </span>

          <span v-else>
            <el-button type="info" size="small" round @click.native="handleUpdate(scope.$index, scope.row)">更新</el-button>
            <el-button type="info" size="small" round @click.native="handleCancel(scope.$index, scope.row)">取消</el-button>
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
      // showEdit: [], //显示编辑框
      showBut: false, //记录当前添加数据的位置
      showBtn: false, //记录当前行是否选中编辑
      // showBtnOrdinary: true,

      listData: [],
      updateData: [],
      tableData:{
        //   couid:"",
        //   stid:"",
      },
      coursevalue:[],
      studentvalue:[],
      // sid: "",
      // stName: "",
      // stGender: ""
    };
  },

  mounted() {
    this.getconsequence();
    this.getlistCourse();
    this.getlistStudent();
  },
  methods: {
    add() {
      this.listData.push({
        cno: "",
        sno: "",
        score: "",
        gain_date: "",
        status:1
      });
    },
    // isNumber(obj) {
    //  return typeof obj === 'number' && isFinite(obj)
    // },
    isNumber(z_check_value) {
      var z_reg = /^(([0-9])|([1-9]([0-9]+)))$/;
      if (z_reg.test(z_check_value)) {
        return true;
      }
      return false;
    },
    // isNumber(obj) {
    // var reg= /^[0-9]+.?[0-9]*$/;
    // if (reg.test(obj)) {
    // return true;
    // }
    // return false;
    // },
    isDate(d_check_value) {
        var d_reg =/^((((1[6-9]|[2-9]\d)\d{2})-(0?[13578]|1[02])-(0?[1-9]|[12]\d|3[01]))|(((1[6-9]|[2-9]\d)\d{2})-(0?[13456789]|1[012])-(0?[1-9]|[12]\d|30))|(((1[6-9]|[2-9]\d)\d{2})-0?2-(0?[1-9]|1\d|2[0-8]))|(((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))-0?2-29))$/;
        if(d_reg.test(d_check_value)) {
            return true;
        }
        return false;
    },

    checkcorrect(item) {
      var iscorrect=true
    //    数据正确性校验
    //   if (item.cno == null) {
        // return false;
    //   }
    //   if (!this.isNumber(item.cno)) {
        // return false;
    //   }
    //   if (item.sno == null) {
        // return false;
    //   }
    //   if (!this.isNumber(item.sno)) {
        // return false;
    //   }
      if (item.score == null) {
        return false;
      }
      if (!this.isNumber(item.score)) {
        return false;
      }
      if (item.gain_date == null) {
        return false;
      }
      if (!this.isDate(item.gain_date)) {
        return false;
      }
        return true;
    },

    confirm() {
      this.listData.map((item) => {
        if (item.status) {
          if (!this.checkcorrect(item))
            return this.$message({
              message: "请修改你的数据 ！！！" + item.cno + item.sno + item.score +item.gain_date,
              type: "warning"
            });
          item.status = 0;

          let brand = new Object();
          // var brand = new Object();
          brand.couid = item.cno;
          brand.stid= item.sno;
          brand.sco = item.score;
          brand.gdate = item.gain_date;

          this.updateData.push(brand);
        }
        return item;
      });
    },
    onSubmit(data) {
      // var data = this.updateData;
      // console.log(data);
      //       http://127.0.0.1:8000/addStudents?sid=001&stName=邓紫棋&stGender=女
      this.axios
        .post("http://127.0.0.1:8000/app1/addConsequences", { data, })
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

    getconsequence: function(event) {
      this.axios
        .get("http://127.0.0.1:8000/app1/displayConsequences")
        .then(response => {
          this.listData = response.data.data;
          // console.log(this.listData);
          if(this.listData.length == 0) {
            let obj = {
              subject:"",
              student:"",
              gender:"",
              status: 0,
            };
            this.listData.push(obj);
          }
        });
    },
    getlistCourse:function(){
        this.axios.get('http://127.0.0.1:8000/app3/showCourses')
        .then(response => {
            this.coursevalue = response.data.data
        })
        .catch(function (error) {
            console.log(error);
        })
    },
    getlistStudent:function(){
        this.axios.get('http://127.0.0.1:8000/app6/displayStudents')
        .then(response => {
            this.studentvalue = response.data.data
        })
        .catch(function (error) {
            console.log(error);
        })
    },    
    //点击添加
    handleCreate(index, row) {
      let brand = new Object();
      brand.cno = "";
      brand.sno = "";
      brand.score = "";
      brand.gain_date="";
      brand.status = 1;
      this.listData.splice(index, 0, brand);
      this.showBut[index] = true;
      this.$set(this.showBut, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
    },
    //点击编辑
    handleEdit(index, row) {
      let brand = new Object();
      brand.cno = row.cno;
      brand.sno = row.sno;
      brand.score = row.score;
      brand.gain_date =row.gain_date;
      brand.status = 1;
      this.showBut[index] = true;
      this.$set(this.showBut, true);
      this.listData.splice(index, 1, brand);
    

      //  this.showEdit[index] = true;
      //  this.showBtn[index] = true;
      //  this.$set(this.showEdit,row,true)
      this.showBtn[index] = true;
      this.$set(this.showBtn, brand, true);
    },
    //取消编辑
    handleCancel(index ,row) {

      if (this.showBut[index] && !this.showBtn[index]) {   //create的取消
        this.listData.splice(index, 1);
        this.showBtn[index] = false;
        this.$set(this.showBtn, row, false);
        this.showBut[index] = false;
        this.$set(this.showBut, false);
      }
      if (this.showBtn[index] && this.showBut[index] ) {    //edit的取消
        row.status = 0;
        this.listData.splice(index, 1, row);
        // console.log(row)
        this.showBtn[index] = false;
        this.$set(this.showBtn, row, false);
        this.showBut[index] = false;
        this.$set(this.showBut, false);
      }
    },
    //点击更新
    handleUpdate(index, row) {
      if (!this.checkcorrect(row))
        return this.$message({
          message: "失败！" + row.cno + row.sno + row.score +row.gain_date,
          type: "warning"
        });
      let brand = new Object();
      brand.couid = row.cno;
      brand.stid = row.sno;
      brand.sco = row.score;
      brand.gdate = row.gain_date; 

      let bran = [];
      bran.push(brand);


      this.onSubmit(bran);
      // this.listData.splice(index,1,row)
      this.handleCancel(index, row);
      row.status=0;
      this.listData.splice(index, 1, row )
      // console.log(row)
      // if(this.onSubmit(bran))  {
      // row.status=0;
      // this.listData.splice(index, 1,row);
      // this.showBtn[index] =false;
      // this.$set(this.showBtn,row,false);
      // }
    },
    //点击删除
    handleDelete(index, row) {
      var brand = new Object();
      brand.couid = row.cno;
      brand.stid =row.sno;

      var data = brand;
      console.log(data);
      //       http://127.0.0.1:8000/addStudents?sid=001&stName=邓紫棋&stGender=女
      this.axios
        .post("http://127.0.0.1:8000/app1/delConsequence", { data })
        .then(response => {
          // this.listData = response.data.data;
          if (response.data.err_num == 1) {
            this.$message({
              message: "失败！" + response.data.msg,
              type: "warning"
            });
          }
          if (response.data.err_num == 0) {
            this.$message({
              message: "删除成功！",
              type: "warning"
            });
            this.listData.splice(index, 1);
            this.showBtn[index] = false;
            this.$set(this.showBtn, row, false);
          }
        });
    }
  }
};
</script>