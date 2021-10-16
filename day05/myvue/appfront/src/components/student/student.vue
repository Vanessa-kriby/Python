<template>
  <span>
    <!-- <el-button @click="add">添加一条数据</el-button> -->
    <!-- <el-button @click="confirm(),onSubmit(updateData)">确认添加</el-button> -->
    <el-table :data="listData" style="width:100%">
      <el-table-column prop="sno" label="学生编号" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.sno"></el-input>
          <span v-else>{{scope.row.sno}}</span>
        </template>
      </el-table-column>

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

      <el-table-column prop="studentDepartment" label="学生专业" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.studentDepartment"></el-input>
          <span v-else>{{scope.row.studentDepartment}}</span>
        </template>
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="200" header-align="center">
        <template slot-scope="scope">
          <span v-show="showBtnAdd[scope.$index]">
          <el-button
            type="text"
            size="small"
            @click.native="handleUpdate(scope.$index,scope.row)"
          >更新</el-button>
          <el-button
            type="text"
            size="small"
            @click.native="handleCancel(scope.$index,scope.row)"
          >取消</el-button>
          </span>

          <span v-show="!showBtnAdd[scope.$index]">
          <el-button type="text" size="small" @click.native="handleAdd(scope.$index,scope.row)">添加</el-button>
          <el-button
              type="text"
              size="small"
              @click.native="handleEdit(scope.$index,scope.row)"
            >编辑</el-button>
            <el-button
              type="text"
              size="small"
              @click.native="handleDelete(scope.$index,scope.row)"
              v-show="!showBtn[scope.$index]"
            >删除</el-button>
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
      listData: [],
      updateData: [],
      showBtn: [],
      showBtnAdd: [],
      sno: "",
      sname: "",
      sgender: "",
      studentDepartment: "",
    };
  },
  mounted() {
    this.getStudents();
  },
  methods: {
    add() {
      this.listData.push({
        sno: "",
        sname: "",
        sgender: "",
        studentDepartment: "",
        status: 1,
      });
    },
    isNumber(obj) {
      var numreg = /^[0-9]+$/;
      if (numreg.test(obj)) {
        return true;
      }
      return false;
    },
    checkcorrect(item) {
      if (item.sname == null) {
        return false;
      }
      if (!this.isNumber(item.sno)) {
        return false;
      }
      if (!this.isNumber(item.studentDepartment)) {
        return false;
      }

      let tname = item.sname.trim();
      if (!(tname.length > 0 && tname.length < 50)) {
        return false;
      }
      return true;
    },
    confirm() {
      this.listData.map((item) => {
        if (item.status) {
          if (!this.checkcorrect(item))
            return this.$message({
              message: "失败！" + item.gno + item.gname,
              type: "warning",
            });
          item.status = 0;
          var vm = new Object();
            vm.stid = item.sno;
            vm.stname = item.sname;
            vm.stgender = item.sgender;
            vm.deid = item.studentDepartment;

          this.updateData.push(vm);
        }
        return item;
      });
    },
    onSubmit(data) {
      // var data=this.updateData;
      // console.log(data);
      // http://127.0.0.1:8000/app6/addStudents?stid=2019002&stname=邓紫琪&stgender=女&deid=06
      this.axios
        .post("http://127.0.0.1:8000/app6/addStudents", { data })
        .then((response) => {
          // this.listData = response.data.data;
          if (response.data.err_num == 1) {
            this.$message({
              message: "失败了！" + response.data.msg,
              type: "warning",
            });
          }
          if (response.data.err_num == 0) {
            this.$message({
              message: "成功了！",
              type: "warning",
            });
          }
        });
    },

    handleAdd(index, row) {
      let vm = new Object();
      vm.sno = "";
      vm.sname = "";
      vm.sgender = "";
      (vm.studentDepartment = ""), (vm.status = 1);
      this.listData.splice(index, 0, vm);
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
    },

    //取消
    handleCancel(index, row) {
      if (this.showBtnAdd[index] && !this.showBtn[index]) {
        this.listData.splice(index, 1);
        this.showBtn[index] = false;
        this.$set(this.showBtn, row, false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      if (this.showBtn[index] && this.showBtnAdd[index]) {
        row.status = 0;
        this.listData.splice(index, 1, row);
        this.showBtn[index] = false;
        this.$set(this.showBtn, row, false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      this.getStudents()
    },

    //更新
    handleUpdate(index, row) {
      if (!this.checkcorrect(row))
        return this.$message({
          message:
            "失败" + row.sno + row.sname + row.sgender + row.studentDepartment,
          type: "warning",
        });
      let vm = new Object();
      vm.stid = row.sno;
      vm.stname = row.sname;
      vm.stgender = row.sgender;
      vm.deid = row.studentDepartment;

      let vmm = [];
      vmm.push(vm);

      this.onSubmit(vmm);
      row.status=0;
      this.listData.splice(index, 1, vmm);
      this.getStudents()
      this.handleCancel(index, row);

    },

    //编辑
    handleEdit(index, row) {
      let vmm = new Object();
      vmm.sno = row.sno;
      vmm.sname = row.sname;
      vmm.sgender=row.sgender;
      vmm.studentDepartment=row.studentDepartment;
      vmm.status = 1;
      this.showBtnAdd[index]=true;
      this.$set(this.showBtnAdd,true);
      this.listData.splice(index, 1, vmm);
      this.showBtn[index] = true;
      this.$set(this.showBtn, vmm, true);
    },

    //删除
    handleDelete(index, row) {
      var vm = new Object();
      vm.stid = row.sno;
      var data = vm;
      // console.log(data);
      // http://127.0.0.1:8000/app6/delStudent?stid=2019003
      this.axios
        .post("http://127.0.0.1:8000/app6/delStudent", { data })
        .then((response) => {
          if (response.data.err_num == 1) {
            this.$message({
              message: "删除失败！" + response.data.msg,
              type: "warning",
            });
          }
            if (response.data.err_num == 0) {
              this.$message({
                message: "删除成功！",
                type: "warning",
              });
              this.listData.splice(index, 1);
              this.showBtn[index] = false;
              this.$set(this.showBtn, row, false);
            }
          });
    },


    getStudents: function (event) {
      this.axios
        .get("http://127.0.0.1:8000/app6/displayStudents")
        .then((response) => {
          this.listData = response.data.data;
          if (this.listData.length == 0) {
            let obj = {
              sno: "2019001",
              sname: "小明",
              sgender: "男",
              studentDepartment: "01",
              status: 1,
            };
            this.listData.push(obj);
          }
          // console.log(this.listData);
        });
    },
  },
};
</script> 