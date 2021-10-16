<template>
    <span>
        <el-button @click="add">添加一条</el-button>
        <el-button @click="confirm()">确认</el-button>
        <el-button @click="onSubmit(updateData)">提交数据</el-button>
        <el-table :data="tableData" style="width: 100%">
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


        <el-table-column fixed="right" label="操作" width="200" header-align="center">
            <template slot-scope="scope">
                <span v-show="showBtnAdd[scope.$index]">
                    <el-button type="text"
                    size="small"
                    @click.native="handleUpdate(scope.$index, scope.row)">更新</el-button>
                     <el-button type="text"
                    size="small"
                    @click.native="handleCancel(scope.$index, scope.row)">取消</el-button>
                    </span>
                <span v-show="!showBtnAdd[scope.$index]">
            <el-button
              type="text"
              size="small"
              @click.native="handleAdd(scope.$index, scope.row)"
            >添加</el-button>
            <el-button
              type="text"
              size="small"
              @click.native="handleEdit(scope.$index, scope.row)"
            >编辑</el-button>
            <el-button
              type="text"
              size="small"
              @click.native="handleDelete(scope.$index, scope.row)"
              v-if="!showBtn[scope.$index]"
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
      showBtn: [],
      showBtnAdd: [],
      tableData: [],
      showEdit:[],
      updateData: [],
      dno: "",
      dname: "",
     
    };
  },
     mounted() {
    this.getDepartment();
  },
  methods: {
    add() {
      this.tableData.push({
        dno: "",
        dname: "",
        status: 1
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
      let dename = item.dname.trim();
      if (!(dename.length > 0 && dename.length < 50)) {
        return false;
      }
      return true;
    },
     confirm() {
          this.tableData.map((item) =>{
                   if(item.status) {
                     if(!this.checkcorrect(item))
                     return this.$message({
                       message: "失败" + item.dno +item.dname,
                       type: "warning",
                     });
                       item.status = 0;
                       var AA = new Object();
                         AA.deid = item.dno;
                         AA.dename = item.dname; 
                       this.updateData.push(AA);
                   }
                   return item;
               });
     },
     onSubmit(data) {
      // var data = this.updateData;
      // console.log(data);
      //  http://127.0.0.1:8000/app2/addDepartments?deid=01&dename=计算机科学与技术
      this.axios
        .post("http://127.0.0.1:8000/app2/addDepartments", { data })
        .then((response) => {
          // this.tableData = response.data.data;
          // console.log(this.tableData);
          if (response.data.err_num == 1) {
            this.$message({
              message: "失败!" + response.data.msg,
              type: "warning"
            });
          }
          if (response.data.err_num == 0) {
            this.$message({
              message: "添加成功",
              type: "warning"
        });
      }
   });
},
     getDepartment: function(event) {
      //   http://127.0.0.1:8000/app2/showDepartments
      this.axios
        .get("http://127.0.0.1:8000/app2/showDepartments")
        .then((response) => {
          this.tableData = response.data.data;
          if(this.tableData.length==0){
            let obj={
              dno: "添加新数据",
              dname: "",
             
              status: 0,
            }
            this.tableData.push(obj);
          }
          console.log(this.tableData);
        });
    },
      handleAdd(index, row) {
      let AA = new Object();
      AA.dno = "";
      AA.dname = "";
      AA.status = 1;
      this.tableData.splice(index, 0, AA);
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
    },

    handleEdit(index, row) {
     
      let AA = new Object();
      AA.dno = row.dno;
      AA.dname = row.dname;
      
      AA.status = 1;
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.tableData.splice(index, 1, AA);
      this.showBtn[index] = true;
      this.$set(this.showBtn, AA, true);
     
    
    },

    handleCancel(index, row) {
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
        this.showBtn[index] = false;
        this.$set(this.showBtn, row, false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      this.getDepartment()
    },

    handleUpdate(index, row) {
    
        if (!this.checkcorrect(row))
        return this.$message({
          message: "失败!" + row.dno + row.dname ,
          type: "warning",
        });
      let AA = new Object();
      AA.deid = row.dno;
      AA.dename = row.dname; 
      let AAA = []
      AAA.push(AA)
      this.onSubmit(AAA);
      this.handleCancel(index,row);
      row.status = 0;
      this.tableData.splice(index,0,row);
     
       
    },

    handleDelete(index, row) {
      var AA = new Object();
      AA.deid= row.dno;
      
      var data = AA;
      console.log(data);
      //  http://127.0.0.1:8000/app2/delDepartment?deid=xxx
      this.axios
        .post("http://127.0.0.1:8000/app2/delDepartment", { data })
        .then(response => {
          if (response.data.err_num == 1) {
            this.$message({
              message: "失败!" + response.data.msg,
              type: "warning"
            });
          }
          if (response.data.err_num == 0) {
            this.$message({
              message: "删除成功",
              type: "warning"
            });
            this.tableData.splice(index, 1);
            this.showBtn[index] = false;
            this.$set(this.showBtn, row, false);
          }
        });
    }
  }
};
</script>