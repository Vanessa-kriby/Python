<template>
  <div>
    <table border="0" align="center" v-show="!ifSuccess">
      <tr>
        <td>
          <span>第一步</span>
        </td>
        <td>
          <el-input v-model="sno" placeholder="请输入你的学号"></el-input>
        </td>
      </tr>
      <tr>
        <td colspan="2" align="center">
          <el-button type="primary" @click="onSubmit()">提交</el-button>
        </td>
      </tr>
    </table>
    <span v-show="ifSuccess">
      <el-container>
        <el-header style="text-align:center;font-size:12px">
          <!-- <i class="el-icon-setting" style="margin-right:15px"></i> -->
          <span>
            <h3 style="display:inilne-block;">{{students.sname}}</h3>欢迎前来查看课程！
          </span>
          <span v-show="ifSuccess">
              <el-table :data="dataList" stripe style="width:100%">
                  <el-table-column prop="student__sno" label="学号"></el-table-column>
                  <el-table-column prop="student__sname" label="姓名"></el-table-column>
                  <el-table-column prop="teachPlan__course__cno" label="所上课程编号"></el-table-column>
                  <el-table-column prop="teachPlan__course__cname" label="所上课程名称"></el-table-column>
                  <el-table-column prop="teacher__tname" label="授课教师"></el-table-column>
                  <el-table-column prop="teachPlan__credit" label="学分"></el-table-column>
                  <el-table-column prop="teachPlan__teach_date" label="开课时间"></el-table-column>
                  <el-table-column prop="teachPlan__evaluation_method" label="考察方式"></el-table-column>

              </el-table>
          </span>
        </el-header>
      </el-container>
    </span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sno: "",
      ifSuccess: false,
      dataList: [],
      students: {},
    };
  },
  mounted() {
  },
  methods: {
    isNumber(obj) {
      var numreg = /^[0-9]+$/;
      if (numreg.test(obj)) {
        return true;
      }
      return false;
    },
    checkcorrect(item) {
      if (item == null) {
        return false;
      }
      if (!this.isNumber(item)) {
        return false;
      }

      let tname = item.trim();
      if (!(tname.length > 0 && tname.length < 50)) {
        return false;
      }
      return true;
    },
    onSubmit() {
      if (this.checkcorrect(this.sno)) {
        let sno = this.sno;
        this.axios
          .get("http://127.0.0.1:8000/app5/retriveStudents", {
            params: { sno },
          })
          .then((response) => {
            if (response.data.err_num == 0) {
              this.ifSuccess = true;
              this.students = response.data.data;
              this.coursecurriculum();
            } else {
              this.$message.warning("错误，请重新输入");
              this.sno = "";
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      } else {
        this.$message.console.warning("错误！");
      }
    },
    coursecurriculum(){
        let sno=this.sno;
        this.axios
            .get(" http://127.0.0.1:8000/app5/showStudentCourse",{
                params: { sno },
            })
            .then((response) => {
              if (response.data.err_num == 0) {
            this.dataList = response.data.data;
          } else {
            this.$message.warning("错误!");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    
  },
};
</script>