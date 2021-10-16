<template>
  <span>
    <!-- <el-button @click="add">添加一条</el-button>
    <el-button @click="confirm">确认增加</el-button>
    <el-button @click="onSubmit(updateData)">保存</el-button> -->
    <el-table :data="listData" style="width: 100%">
      <el-table-column prop="teacher_id" label="老师编号" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.teacher_id"></el-input>
          <span v-else>{{scope.row.teacher_id}}</span>
        </template>
      </el-table-column>

      <el-table-column prop="curriculum_id" label="课程编号" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.curriculum_id"></el-input>
          <span v-else>{{scope.row.curriculum_id}}</span>
        </template>
      </el-table-column>

      <el-table-column prop="textbook" label="授课教材" width="180">
        <template slot-scope="scope">
          <el-input v-if="scope.row.status" v-model="scope.row.textbook"></el-input>
          <span v-else>{{scope.row.textbook}}</span>
        </template>
      </el-table-column>

      <el-table-column fixed="right" label="操作" width="200" header-align="center">
        <template slot-scope="scope">
          <span v-show="showBtnAdd[scope.$index]">
            <el-button type="text" size="small" @click.native="handleUpdate(scope.$index, scope.row)" >更新</el-button>
            <el-button type="text" size="small" @click.native="handleCancel(scope.$index, scope.row)" >取消</el-button>
          </span>

          <span v-show="!showBtnAdd[scope.$index]">
            <el-button type="text" size="small" @click.native="handleAdd(scope.$index, scope.row)" >增加</el-button>
            <el-button type="text" size="small" @click.native="handleEdit(scope.$index, scope.row)" >编辑</el-button>
            <el-button type="text" size="small" @click.native="handleDelete(scope.$index, scope.row)" v-if="!showBtn[scope.$index]" >删除</el-button>
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
    };
  },
  mounted() {
    this.getTeaching();
  },
  methods: {
    add() {
      this.listData.push({
        curriculum_id: "",
        teacher_id: "",
        textbook: "",
        status: 1,
      });
    },
    // isNumber(obj) {
    //   var reg = /^[\u2E80-\u9FFF]+$/.test("中国");
    //   if (!reg.test(obj)) {
    //     alert("格式不正确");
    //     return false;
    //   }
    //   return true;
    // },

    checkcorrect(item) {
      let tebook=item.textbook
      if (!(tebook.length>0&&tebook.length<50)) {
        return false;
      }
      return true;
    },
    confirm() {
      this.listData.map((item) => {
        if (item.status) {
          if (!this.checkcorrect(item))
            return this.$message({
              message: "添加失败",
              type: "warning",
            });
          item.status = 0;
          let ww = new Object();
          ww.teid = item.teacher_id;
          ww.couid = item.curriculum_id;
          ww.tbook = item.textbook;
          this.updateData.push(ww);
        }
        return item;
      });
    },
    onSubmit(data) {
      this.axios
        .post("http://127.0.0.1:8000/app7/addTeachings", {
          data,
        })
        .then((response) => {
          if (response.data.err_num == 1) 
          {
            this.$message({
              message: "修改失败 ！",
              type: "warning",
            });
          }
          if (response.data.err_num == 0) 
          {
            this.$message({
              message: "修改成功 ！",
              type: "warning",
            });
          }
          this.listData=response.data.data;
        });
        
    },

    getTeaching(event) {
      this.axios
        .get("http://127.0.0.1:8000/app7/displayTeachings")
        .then((response) => {
          this.listData = response.data.data;
          if(this.listData.length==0){
            let obj={
              teacher_id :"",
              curriculum_id : "",
              textbook : "",
              status : 0,
            };
            this.listData.push(obj);
          }
        });
    },

    //点击添加 
    handleAdd(index, row) {
      let ww = new Object();
        ww.teacher_id = "";
        ww.curriculum_id = "";
        ww.textbook = "";
        ww.status = 1;
      this.listData.splice(index, 0, ww);
      this.showBtnAdd[index] = true;
      this.$set(this.showBtnAdd, true);
      this.showBtn[index] = false;
      this.$set(this.showBtn, row, false);
    },

    //点击编辑
    handleEdit(index, row) { 
      let ww = new Object();
        ww.teacher_id = row.teacher_id;
        ww.curriculum_id = row.curriculum_id;
        ww.textbook = row.textbook;
        ww.status = 1;
      this.showBtnAdd[index]=true;
      this.$set(this.showBtnAdd, true);
      this.listData.splice(index, 1, ww);
      this.showBtn[index] = true;
      this.$set(this.showBtn, ww, true);
    },
    //取消编辑
    handleCancel(index, row) {
      if (this.showBtnAdd[index] && !this.showBtn[index]) {          //判断入口
        this.listData.splice(index, 1);//删除数据元素编辑模式
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
      if (this.showBtn[index] && this.showBtnAdd[index]) {
        row.status = 0;
        this.listData.splice(index, 1, row);//是替换为编辑模式
        this.showBtn[index] = false;
        this.$set(this.showBtn, row ,false);
        this.showBtnAdd[index] = false;
        this.$set(this.showBtnAdd, false);
      }
    },

    //点击更新
    handleUpdate(index, row) {
      if (!this.checkcorrect(row))
        return this.$message({
          message: "更新失败",
          type: "warning",
        });
      let ww = new Object();
        ww.teid = row.teacher_id;
        ww.couid = row.curriculum_id;
        ww.tbook = row.textbook;

      let www = []
      www.push(ww);
      this.onSubmit(www);
      this.handleCancel(index, row);
      row.status = 0;
      this.listData.splice(index, 1, ww)
    },

    //点击删除
    handleDelete(index, row) {
      var ne = new Object();
      ne.teid = row.teacher_id;
      ne.couid = row.curriculum_id;
      ne.tbook=row.textbook
      var data = ne;
      console.log(data);
      this.axios
        .post("http://127.0.0.1:8000/app7/delTeaching", { data })
        .then((response) => {
          if (response.data.err_num == 1) {
            this.$message({
              message: "删除失败 ！",
              type: "warning",
            });
          }
          if (response.data.err_num == 0) {
            this.$message({
              message: "删除成功 ！",
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