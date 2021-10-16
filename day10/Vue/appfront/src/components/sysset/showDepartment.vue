<template>
  <span>
    <!-- <el-button @click="add">添加一条数据</el-button> -->
    <!-- <el-button @click="confirm(),onSubmit(updateData)">确认添加</el-button> -->
    <!-- <el-button @click="onSubmit">提交数据</el-button> -->
    <el-table :data="listData" style="width:100%">
        
      <el-table-column prop="dno" label="专业编号" width="180">
            <template slot-scope="scope">
                <el-input v-if="scope.row.status" v-model="scope.row.dno"></el-input>
                <span v-else>{{scope.row.dno}}</span>
            </template>
      </el-table-column>

      <el-table-column prop="dname" label="专业名称" width="180">
            <template slot-scope="scope">
                <el-input v-if="scope.row.status" v-model="scope.row.dname"></el-input>
                <span v-else>{{scope.row.dname}}</span>
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
      listData: [],
      updateData: [],
      showEdit: [], //显示编辑框
      showBtn: [],
      showBtnAdd: [],
      dno:"",
      dname:"",
    };
  },
  mounted() {
    this.getDepartments();
  },

  methods: {
    add() {
      this.listData.push({
        dno: "",
        dname: "",
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
      if (item.dname == null) {
        return false;
      }
      if (!this.isNumber(item.dno)) {
        return false;
      }

      let tname = item.dname.trim();
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
              message: "失败！" + item.dno + item.dname,
              type: "warning",
            });
          item.status = 0;
          var vm = new Object();
          vm.dno = item.dno;
          vm.dname = item.dname;

          this.updateData.push(vm);
        }
        return item;
      });
    },
    onSubmit(data) {
      // var data=this.updateData;
      // console.log(data);
      this.axios
        .post("http://127.0.0.1:8000/app1/addDepartments", {data})
        .then((response) => {
          // this.listData = response.data.data;
          if (response.data.err_num == 1) {
            this.$message({
              message: "添加失败！" + response.data.msg,
              type: "warning",
            });
          }
          if (response.data.err_num == 0) {
            this.getDepartments()
            this.$message({
              message: "添加成功！",
              type: "warning",
            });
          }
        });
    },
    getDepartments: function (event) {
      this.axios
        .get("http://127.0.0.1:8000/app1/showDepartments")
        .then((response) => {
          this.listData = response.data.data;
          if(this.listData.length==0){
            let obj={
              dno:"",
              dname:"",
              status:1,

            }
            this.listData.push(obj);
          }
          // console.log(this.listData);
        });
    },

    //添加
    handleAdd(index, row) {
       if(this.myisedit) {
            this.$message.success("请处理所编辑的内容!");
            return;
        }
      let vm = new Object();
      vm.dno = "";
      vm.dname = "";
      vm.status = 1;
      this.listData.splice(index, 0, vm);
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
      this.myisedit = true;
    },

    //编辑
    handleEdit(index, row) {
      if(this.myisedit) {
            this.$message.success("请处理所编辑的内容!");
            return;
        }
      let vmm = new Object();
      vmm.dno = row.dno;
      vmm.dname = row.dname;
      vmm.status = 1;
      this.showBtnAdd[index]=true;
      this.$set(this.showBtnAdd,true);
      this.listData.splice(index, 1, vmm);
      this.showBtn[index] = true;
      this.$set(this.showBtn, vmm, true)
      this.myisedit = true;
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
        this.listData.splice(index, 1, row);
        this.showBtn[index]=false;
        this.$set(this.showBtn,row,false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
       this.getDepartments()
    },

    //更新
    handleUpdate(index, row) {
       this.myisedit = false;
      if (!this.checkcorrect(row))
        return this.$message({
          message: "失败" + row.dno + row.dname,
          type: "warning",
        });
      let vm = new Object();
      vm.dno = row.dno;
      vm.dname = row.dname;

      let vmm = []
      vmm.push(vm)

      this.onSubmit(vmm);
      row.status = 0;
      this.handleCancel(index, row);
      row.status = 0;
      this.getDepartments()
      this.listData.splice(index,1, row);
      
    },

    //点击删除
    handleDelete(index,row){
        if(this.myisedit) {
            this.$message.success("请处理所编辑的内容!");
            return;
        }
      var xx=new Object();
      xx.dno=row.dno;
      var data=xx;
      this.axios
          .post("http://127.0.0.1:8000/app1/delDepartment",{data})
          .then((response) =>{
            if(response.data.err_num==1){
              this.$message({
                message:"删除失败！"+response.data.msg,
                type:"warning"
              });
            }
            if(response.data.err_num==0){
              this.getDepartments();
              this.$message({
                message:"删除成功！",
                type:"success",
              });
              this.listData.splice(index,1);
              this.showBtn[index]=false;
              this.$set(this.showBtn,row,false);
            }
           
          });
    },
  
  },
};
</script> 