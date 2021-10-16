<template>
    <span>
        <el-button @click="add">添加一条</el-button>
        <el-button @click="confirm()">确认</el-button>
        <el-button @click="onSubmit(updateData)">提交数据</el-button>
        <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="cno" label="课程编号" width="180">
                <template slot-scope="scope">
                    <el-input v-if="scope.row.status" v-model="scope.row.cno"></el-input>
                    <span v-else>{{scope.row.cno}}</span>
                    </template>
                    </el-table-column>

            <el-table-column prop="cname" label="课程名称" width="180">
                <template slot-scope="scope">
                    <el-input v-if="scope.row.status" v-model="scope.row.cname"></el-input>
                    <span v-else>{{scope.row.cname}}</span>
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
      cno: "",
      cname: "",
     
    };
  },
     mounted() {
    this.getCourse();
  },
  methods: {
    add() {
      this.tableData.push({
        cno: "",
        cname: "",
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
      if (item.cname == null) {
        return false;
      }

      if (!this.isNumber(item.cno)) {
        return false;
      }
      let couname = item.cname.trim();
      if (!(couname.length > 0 && couname.length < 50)) {
        return false;
      }
      return true;
    },
     confirm() {
          this.tableData.map((item) =>{
                   if(item.status) {
                     if(!this.checkcorrect(item))
                     return this.$message({
                       message: "失败" + item.cno +item.cname,
                       type: "warning",
                     });
                       item.status = 0;
                       var AA = new Object();
                         AA.couid = item.cno;
                         AA.couname = item.cname; 
                       this.updateData.push(AA);
                   }
                   return item;
               });
     },
     onSubmit(data) {
      // var data = this.updateData;
      // console.log(data);
      // http://127.0.0.1:8000/app3/addCourses?couid=100&couname=高等数学1
      this.axios
        .post("http://127.0.0.1:8000/app3/addCourses", { data })
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
     getCourse: function(event) {
      // http://127.0.0.1:8000/app3/showCourses  
      this.axios
        .get("http://127.0.0.1:8000/app3/showCourses")
        .then((response) => {
          this.tableData = response.data.data;
          if(this.tableData.length==0){
            let obj={
              cno: "添加新数据",
              cname: "",
             
              status: 0,
            }
            this.tableData.push(obj);
          }
          console.log(this.tableData);
        });
    },
      handleAdd(index, row) {
      let AA = new Object();
      AA.cno = "";
      AA.cname = "";
      AA.status = 1;
      this.tableData.splice(index, 0, AA);
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
    },

    handleEdit(index, row) {
     
      let AA = new Object();
      AA.cno = row.cno;
      AA.cname = row.cname;
      
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
      this.getCourse()
    },

    handleUpdate(index, row) {
    
        if (!this.checkcorrect(row))
        return this.$message({
          message: "失败!" + row.cno + row.cname ,
          type: "warning",
        });
      let AA = new Object();
      AA.couid = row.cno;
      AA.couname= row.cname;
     
      let AAA = []
      AAA.push(AA)
      this.onSubmit(AAA);
      this.handleCancel(index,row);
      row.status = 0;
      this.tableData.splice(index,1,row);
       
    },

    handleDelete(index, row) {
      var AA = new Object();
      AA.couid= row.cno;
      
      var data = AA;
      console.log(data);
      // http://127.0.0.1:8000/app3/delCourse?couid=xxx
      this.axios
        .post("http://127.0.0.1:8000/app3/delCourse", { data })
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