<template>
  <span>
    <!-- <el-button @click="add">添加一条数据</el-button> -->
    <!-- <el-button @click="confirm(),onSubmit(updateData)">确认添加</el-button> -->
    <el-table :data="listData" style="width:100%">
      <el-table-column prop="tno" label="教师编号" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.tno"></el-input>
          <span v-else>{{scope.row.tno}}</span>
        </template>
      </el-table-column>

      <el-table-column prop="tname" label="教师名称" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.tname"></el-input>
          <span v-else>{{scope.row.tname}}</span>
        </template>
      </el-table-column>

      <el-table-column prop="tgender" label="教师性别" width="180">
        <template slot-scope="scope">
          <span v-if="scope.row.status">
            <el-radio v-model="scope.row.tgender" label="男">男</el-radio>
            <el-radio v-model="scope.row.tgender" label="女">女</el-radio>
          </span>
          <div v-else>{{scope.row.tgender}}</div>
        </template>
      </el-table-column>

      <el-table-column prop="jobtitle" label="教师职称" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.jobtitle"></el-input>
          <span v-else>{{scope.row.jobtitle}}</span>
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
      tno: "",
      tname: "",
      tgender: "",
      jobtitle: "",
    };
  },
  mounted() {
    this.getTeachers();
  },
  methods: {
      add() {
      this.listData.push({
        tno: "",
        tname: "",
        tgender: "",
        jobtitle: "",
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
      if (item.tname == null) {
        return false;
      }
      if (!this.isNumber(item.tno)) {
        return false;
      }
      let tejob = item.jobtitle.trim();
      if (!(tejob.length > 0 && tejob.length < 50)) {
        return false;
      }

      let tname = item.tname.trim();
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
              message: "失败！" + item.tno + item.tname+item.tgender+item.jobtitle,
              type: "warning",
            });
          item.status = 0;
          var vm = new Object();
            vm.teid = item.tno;
            vm.tename = item.tname;
            vm.tegender = item.tgender;
            vm.tejob= item.jobtitle;

          this.updateData.push(vm);
        }
        return item;
      });
    },
    onSubmit(data) {
      // var data=this.updateData;
      // console.log(data);
      // http://127.0.0.1:8000/app5/addTeachers?teid=005&tename=王俊凯&tegender=男&tejob=教授
      this.axios
        .post("http://127.0.0.1:8000/app5/addTeachers", { data })
        .then((response) => {
          this.listData = response.data.data;
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
      vm.tno = "";
      vm.tname = "";
      vm.tgender="";
      vm.jobtitle="";
      vm.status = 1;
      this.listData.splice(index, 0, vm);
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
    },

    //更新
    handleUpdate(index, row) {
      if (!this.checkcorrect(row))
        return this.$message({
          message: "失败" + row.tno + row.tname+row.tgender+row.jobtitle,
          type: "warning",
        });
      let vm = new Object();
      vm.teid = row.tno;
      vm.tename = row.tname;
      vm.tegender = row.tgender;
      vm.tejob=row.jobtitle;

      let vmm = []
      vmm.push(vm)

      this.onSubmit(vmm);
      row.status=0;
      this.listData.splice(index, 0, vmm);
      this.getTeachers()
      
      this.handleCancel(index, row);
    },

    //删除
    handleDelete(index, row) {
      var vm = new Object();
      vm.teid = row.tno;
      var data = vm;
      // console.log(data);
      // http://127.0.0.1:8000/app5/delTeacher?teid=001
      this.axios
        .post("http://127.0.0.1:8000/app5/delTeacher", { data })
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

    handleEdit(index, row) {
      let vmm = new Object();
      vmm.tno = row.tno;
      vmm.tname = row.tname;
      vmm.tgender=row.tgender;
      vmm.jobtitle=row.jobtitle;
      vmm.status = 1;
      this.showBtnAdd[index]=true;
      this.$set(this.showBtnAdd,true);
      this.listData.splice(index, 1, vmm);
      this.showBtn[index] = true;
      this.$set(this.showBtn, vmm, true);
    },


    //取消
    handleCancel(index, row) {
      if (this.showBtnAdd[index] && !this.showBtn[index]) {
        this.listData.splice(index, 1);
        this.showBtn[index]=false;
        this.$set(this.showBtn,row,false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      if (this.showBtn[index] && this.showBtnAdd[index]) {
        row.status = 0;
        this.listData.splice(index, 1, row);
        this.showBtn[index]=false;
        this.$set(this.showBtn,row,false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
    },

    getTeachers: function (event) {
      this.axios
        .get("http://127.0.0.1:8000/app5/displayTeachers")
        .then((response) => {
          this.listData = response.data.data;
          // console.log(this.listData);
          if (this.listData.length == 0) {
            let obj = {
              tno: "001",
              tname: "小明",
              tgender: "男",
              jobtitle: "教授",
              status: 1,
            };
            this.listData.push(obj);
          }
          // console.log(this.listData);
        });
    },
  },
}
</script>>