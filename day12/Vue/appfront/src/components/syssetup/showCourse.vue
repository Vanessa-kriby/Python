
<template>
  <span>
    <!-- <el-button @click="add">添加一条数据</el-button> -->
    <!-- <el-button @click="confirm(),onSubmit(updateData)">确认添加</el-button> -->
    <!-- <el-button @click="onSubmit">提交数据</el-button> -->
    <el-table :data="listData" style="width:100%">
     <el-table-column prop="cno" label="课程编号" width="180">
        <template slot-scope="scope">
            <span v-if="scope.row.status">
                <span v-if=" !btntype">
           <el-input v-if="scope.row.status" v-model="scope.row.cno"></el-input>
          </span>
          <span v-else>
              <span>{{scope.row.cno}}</span>
              </span>
              </span>
              <span v-else>
              <span>{{scope.row.cno}}</span>
              </span>
        </template>
      </el-table-column>
      <el-table-column prop="cname" label="课程名称" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.cname"></el-input>
          <span v-else>{{scope.row.cname}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="textBook" label="教材名称" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.textBook"></el-input>
          <span v-else>{{scope.row.textBook}}</span>
        </template>
      </el-table-column>

       <el-table-column prop="category" label="类别" width="180">
        <template slot-scope="scope">
          <span v-if="scope.row.status">
            <el-radio v-model="scope.row.category" label="必修">必修</el-radio>
            <el-radio v-model="scope.row.category" label="选修">选修</el-radio>
          </span>
          <div v-else>{{scope.row.category}}</div>
        </template>
      </el-table-column>

      <el-table-column label="操作" width="400">
          <template slot-scope="scope">
              <span v-if="!scope.row.status">
        <el-button size="small" type="primary" round @click.native="handleAdd(scope.$index,scope.row)">添加</el-button>
       <el-button size="small" type="info" round @click.native="handleEdit(scope.$index,scope.row)">编辑</el-button>
       <el-button size="small" type="warning" round @click.native="handleDelete(scope.$index,scope.row)" v-if="!showBtn[scope.$index]">删除</el-button>
              </span>
         <span v-else>
       <el-button size="small" type="info" round @click="handleUpdate(scope.$index,scope.row)">更新</el-button>
       <el-button size="small" type="warning" round @click.native="handleCancel(scope.$index,scope.row)">取消</el-button>
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
      showEdit: [], //显示编辑框
      showBtn: [],
      showBtnAdd: [],
      cno: "",
      cname: "",
      textBook: "",
      category:"",
    };
  },
  mounted() {
    this.getCourse();
  },
  methods: {
    add() {
      this.listData.push({
        cno: "",
        cname: "",
        textBook: "",
        category: "",
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
      if (item.cname == null) {
        return false;
      }
      if (!this.isNumber(item.cno)) {
        return false;
      }

      let tname = item.cname.trim();
      if (!(tname.length > 0 && tname.length < 100)) {
        return false;
      }
      let tbook = item.textBook.trim();
      if (!(tbook.length > 0 && tbook.length < 100)) {
        return false;
      }
      return true;
    },
    confirm() {
      this.listData.map((item) => {
        if (item.status) {
          if (!this.checkcorrect(item))
            return this.$message({
              message: "失败！" + item.cno + item.cname + item.textBook + item.category,
              type: "waring",
            });
          item.status = 0;
          var vm = new Object();
          vm.cno = item.cno;
          vm.cname = item.cname;
          vm.textBook = item.textBook;
          vm.category = item.category;
          this.updateData.push(vm);
        }
        return item;
      });
    },
    onSubmit(data) {
      // var data = this.updateData;
      // console.log(data);
      this.axios
        .post("http://127.0.0.1:8000/app4/addCourses", { data })
        .then((response) => {
          // this.listData = response.data.data;
          if (response.data.err_num == 1) {
            this.$message({
              message: "失败！" + response.data.msg,
              type: "warning",
            });
          }
          if (response.data.err_num == 0) {
            this.getCourse()
            this.$message({
              message: "成功！",
              type: "warning",
            });
          }
        });
    },
    handleAdd(index, row) {
      if(this.myisedit) {
            this.$message.success("请处理所编辑的内容!");
            return;
        }
      let vm = new Object();
      vm.cno = "";
      vm.cname = "";
      vm.textBook="";
      vm.category="";
      vm.status = 1;
      this.listData.splice(index, 0, vm);
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
      this.myisedit = true;
    },
    handleEdit(index, row) {
      if(this.myisedit) {
            this.$message.success("请处理所编辑的内容!");
            return;
        }
      let vmm = new Object();
      vmm.cno = row.cno;
      vmm.cname = row.cname;
      vmm.textBook=row.textBook;
      vmm.category=row.category;
      vmm.status = 1;
      this.showBtnAdd[index]=true;
      this.$set(this.showBtnAdd,true);
      this.listData.splice(index, 1, vmm);
      this.showBtn[index] = true;
      this.$set(this.showBtn, vmm, true);
      this.myisedit = true;
      this.btntype = true;
    },

    getCourse: function (event) {
      this.axios
        .get("http://127.0.0.1:8000/app4/showCourses")
        .then((response) => {
          this.listData = response.data.data; 
        if(this.listData.length==0){
            let obj={
              cno:"",
              cname:"",
              textBook:"",
              category:"",
              status:1,

            }
            this.listData.push(obj);
          }
          
          // console.log(this.listData);
        });
    },

    //取消
    handleCancel(index, row) {
       this.myisedit = false;
      if (this.showBtnAdd[index] && !this.showBtn[index]) {
        this.listData.splice(index, 1);
        this.showBtn[index]=false;
        this.$set(this.showBtn,row,false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      if (this.showBtn[index] && this.showBtnAdd[index]) {
        row.status = 0;
        this.listData.splice(index, 1,row);
        this.showBtn[index]=false;
        this.$set(this.showBtn,row,false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      this.btntype=false;
      this.getCourse()
    },

   



    //更新
    handleUpdate(index, row) {
       this.myisedit = false;
      if (!this.checkcorrect(row))
        return this.$message({
          message: "失败" + row.cno + row.cname+row.textBook+row.category,
          type: "warning",
        });
      let vm = new Object();
      vm.cno = row.cno;
      vm.cname = row.cname;
      vm.textBook = row.textBook;
      vm.category = row.category;

      let vmm = []
      vmm.push(vm)

    //   this.onSubmit(vmm);
    //   this.handleCancel(index, row);
      this.onSubmit(vmm);
      row.status = 0;
      this.handleCancel(index, row);
      row.status = 0;
      this.getCourse()
      this.listData.splice(index,1, row);
      this.myisedit = false;
      this.btntype = false;
    },

     //删除
    handleDelete(index, row) {
      if(this.myisedit) {
            this.$message.success("请处理所编辑的内容!");
            return;
        }
      var vm = new Object();
      vm.cno = row.cno;
      var data = vm;
      // console.log(data);
      // http://127.0.0.1:8000/app6/delStudent?stid=2019003
      this.axios
        .post("http://127.0.0.1:8000/app4/delCourse", { data })
        .then((response) => {
          if (response.data.err_num == 1) {
            this.$message({
              message: "删除失败！" + response.data.msg,
              type: "warning",
            });
          }
            if (response.data.err_num == 0) {
              this.getCourse()
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
  },
};
</script>    