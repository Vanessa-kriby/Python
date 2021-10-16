<template>
  <span>
    <el-button @click="add">添加学生信息</el-button>
    <el-button @click="confirm(),onSubmit(updateData)">确认添加</el-button>
    <!-- <el-button @click="update">修改学生信息</el-button> -->
    <!-- <el-button @click="onSubmit">保存</el-button> -->
    <el-table :data="listData" style="width: 100%">
      <el-table-column prop="sno" label="学号" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.sno"></el-input>
          <span v-else>{{scope.row.sno}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="sname" label="姓名" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.sname"></el-input>
          <span v-else>{{scope.row.sname}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="gender" label="性别" width="180">
        <template slot-scope="scope">
          <!-- <el-input v-if="scope.row.status" v-model="scope.row.gender"></el-input> -->
          <span v-if="scope.row.status">
            <el-radio v-model="scope.row.gender" label="男">男</el-radio>
            <el-radio v-model="scope.row.gender" label="女">女</el-radio>
          </span>
          <span v-else>{{scope.row.gender}}</span>
        </template>
      </el-table-column>

      <el-table-column fixed="right" label="操作" width="200" header-align="center">
        <template slot-scope="scope">
          <span v-show="showBut[scope.$index]">
            <el-button type="text" size="small" @click.native="handleUpdate(scope.$index, scope.row)">更新</el-button>
            <el-button type="text" size="small" @click.native="handleCancel(scope.$index, scope.row)">取消</el-button>
          </span>
          <span v-show="!showBut[scope.$index]">
            <el-button type="text" size="small" @click.native="handleCreate(scope.$index, scope.row)">添加</el-button>
            <el-button type="text" size="small" @click.native="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button type="text" size="small" @click.native="handleDelete(scope.$index, scope.row)" v-if="!showBtn[scope.$index]">删除</el-button>
          </span>
        </template>
      </el-table-column>

      <!-- <el-table-column label="操作"> -->
      <!-- <template slot-scope="scope"> -->
      <!-- <el-button -->
      <!-- size="mini" -->
      <!-- @click="handleEdit(scope.$index, scope.row)">编辑</el-button> -->
      <!-- <el-button -->
      <!-- size="mini" -->
      <!-- type="danger" -->
      <!-- @click="handleDelete(scope.$index, scope.row)">删除</el-button> -->
      <!-- </template> -->
      <!-- </el-table-column> -->
    </el-table>
  </span>
</template>

<script>
export default {
  data() {
    return {
      // showEdit: [], //显示编辑框
      showBut: [], //记录当前添加数据的位置
      showBtn: [], //记录当前行是否选中编辑
      // showBtnOrdinary: true,

      listData: [],
      updateData: []
      // sid: "",
      // stName: "",
      // stGender: ""
    };
  },

  mounted() {
    this.getstudent();
  },
  methods: {
    add() {
      this.listData.push({
        sno: "",
        sname: "",
        gender: "",
        status: 1
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

    checkcorrect(item) {
      // var iscorrect=true
      //  数据正确性校验
      if (item.sno == null) {
        return false;
      }
      if (!this.isNumber(item.sno)) {
        return false;
      }
      if (item.sname == null) {
        return false;
      }
      let tname = item.sname.trim();
      if (!(tname.length > 0 && tname.length < 50)) {
        return false;
      }
      if (item.sname == null) {
        return false;
      }
      let sgender = item.gender.trim();
      if (!(sgender.length > 0 && sgender.length < 10)) {
        return false;
      }
      return true;
    },

    confirm() {
      this.listData.map((item) => {
        if (item.status) {
          if (!this.checkcorrect(item))
            return this.$message({
              message: "请修改你的数据 ！！！" + item.sno + item.sname + item.gender,
              type: "warning"
            });
          item.status = 0;

          let brand = new Object();
          // var brand = new Object();
          brand.sid = item.sno;
          brand.stName = item.sname;
          brand.stGender = item.gender;

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
        .post("http://127.0.0.1:8000/app5/addStudents", { data, })
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

    getstudent: function(event) {
      this.axios
        .get("http://127.0.0.1:8000/app5/showStudents")
        .then(response => {
          this.listData = response.data.data;
          // console.log(this.listData);
          if(this.listData.length == 0) {
            let obj = {
              sno:"",
              sname:"添加新数据",
              gender:"",
              status: 0,
            };
            this.listData.push(obj);
          }
        });
    },
    //点击添加
    handleCreate(index, row) {
      let brand = new Object();
      brand.sno = "";
      brand.sname = "";
      brand.gender = "";
      brand.status = 1;
      this.listData.splice(index, 0, brand);
      this.showBut[index] = true;
      this.$set(this.showBut, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
    },
    //点击编辑学生
    handleEdit(index, row) {
      let brand = new Object();
      brand.sno = row.sno;
      brand.sname = row.sname;
      brand.gender = row.gender;
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
          message: "失败！" + row.sno + row.sname + row.gender,
          type: "warning"
        });
      let brand = new Object();
      brand.sid = row.sno;
      brand.stName = row.sname;
      brand.stGender = row.gender;

      let bran = [];
      bran.push(brand);


      this.onSubmit(bran);
      this.listData.splice(index,1,row)
      this.handleCancel(index, row);
      row.status=0;
      this.listData.splice(index, 0, row )
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
      brand.stid = row.sno;

      var data = brand;
      console.log(data);
      //       http://127.0.0.1:8000/addStudents?sid=001&stName=邓紫棋&stGender=女
      this.axios
        .post("http://127.0.0.1:8000/app5/delStudent", { data })
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