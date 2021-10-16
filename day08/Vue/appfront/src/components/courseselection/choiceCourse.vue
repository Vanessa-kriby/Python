<template>
  <div>
    <table border="0" align="center" v-show="!ifSuccess">
      <tr>
        <td>
          <span>第一步:</span>
        </td>
        <td>
          <el-input v-model="sno" placeholder="输入你的学号"></el-input>
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
        <el-header style="text-algin:center; font-size: 12px">
          <i class="el-icon-setting" style="margin-right: 15px"></i>
          <span>
            <h3 style="display:inline-block;">{{students.sname}}</h3>欢迎选课!
          </span>
        </el-header>

        <el-table :data="teachPlanList" border stripe style="width: 100%">
          <el-table-column prop="tpno" label="教学计划编号" width="200"></el-table-column>
          <!-- <el-table-column prop="course__cno" label="课程编号" width="200"></el-table-column> -->
          <el-table-column prop="course__cname" label="课程名字" width="200"></el-table-column>
          <!-- <el-table-column prop="teacher__tno" label="教师编号" width="200"></el-table-column> -->
          <el-table-column prop="teacher__tname" label="教师名字" width="200"></el-table-column>
          <el-table-column prop="credit" label="学分" width="200"></el-table-column>
          <el-table-column prop="teach_date" label="开课时间" width="200"></el-table-column>
          <el-table-column prop="evaluation_method" label="考核方式" width="200"></el-table-column>

          <!-- <el-table-column label="操作" width="280" header-align="center">
                      <el-button type="primary" @click="Submit">确定选择</el-button>
                      <el-button type="primary" @click="ondelete">删除选择</el-button>
          </el-table-column>-->
        </el-table>

        <table border="0" align="center" v-show="ifSuccess">
          <tr>
            <td>
              <span>第二步:</span>
            </td>
            <td>
              <el-input v-model="tpno" placeholder="输入你选择的教学计划编号"></el-input>
            </td>
          </tr>
          <tr>
            <td colspan="2" align="center">
              <el-button type="primary" @click="onSubmitPlan()">提交</el-button>
            </td>
          </tr>
        </table>

        <el-main>
          <el-row type="flex" justify="center" align>
            <el-transfer
              style="text-align: left; display: inline-block"
              filterable
              v-model="resultData"
              :data="selectCourse"
              :titles="['可选课程', '所选课程']"
              :button-texts="['移动到可选','移动到所选']"
            ></el-transfer>
          </el-row>
          <el-row>
            <el-row type="flex" justify="center" align>
              <el-button type="info" @click="submitCourse()" round>提交</el-button>
            </el-row>
            <p>由于模型问题，一个学生只能加一门课,一门课只能被一个人选</p>
          </el-row>
        </el-main>
      </el-container>
      <!--到这里无问题-->
      <!-- <el-transfer v-model="resultData" :data="dataList"></el-transfer> -->
    </span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sno: "",
      teachPlanNum: "",
      tpno: "",
      ifSuccess: false,
      dataList: [], //筛选的课程
      resultData: [], //双向绑定表单信息
      students: {}, //存入后端的学生信息
      teachPlanList: [], //存入教学计划信息
    };
  },
  computed: {
    selectCourse() {
      const data = [];
      this.dataList.forEach((item, i) => {
        console.log(this.dataList);
        data.push({
          key: i,
          label: `${item.course__cno} ${item.course__cname}`,
          disabled: false,
        });
      });
      return data;
    },
    selectTeachPlan() {},
  },
  mounted() {
    // this.getInventory();
    // this.getCourse();
    // this.getTeacher();
    this.getTeachPlan();
    // this.jump();
    // this.getdepartment();
  },
  methods: {
    getTeachPlan() {
      this.axios
        .get("http://127.0.0.1:8000/app1/showTeachPlans")
        .then((response) => {
          this.teachPlanList = response.data.data;
          console.log(this.teachPlanList);
        });
    },
    submitCourse() {
        // alert(this.teachPlanNum.tpno)
        // alert(this.teachPlanNum.teacher_id)
      let tdata = [];
      this.resultData.forEach((i) => {
          
        // console.log(this.dataList[i].cno)
        tdata.push(this.dataList);
        // alert(this.dataList.teaher__tno)
      });
      console.log(tdata+'1');
      let data = {
        sno: "",
        tpnos: "",
        tno: "",
      };
      data.sno = this.students.sno;
      data.tpnos = this.teachPlanNum.tpno;
      data.tno = this.teachPlanNum.teacher_id;
      this.axios
        .post("http://127.0.0.1:8000/app5/postStudentCourse", { data })
        .then((response) => {
          // this.listData = response.data.data;
          if (response.data.err_num == 0) {
            //   this.ifSuccess =true;
            //   this.students=response.data.data;
            //   this.courseFilter();
            this.$message.success("选课成功!");
          } else {
            this.$message.warning("错误！");
            this.sno = "";
          }
        })
        .catch((error) => {
          this.$message.warning(error);
        });
    },
    courseFilter() {
      let tpno = this.tpno;
      this.axios
        .get("http://127.0.0.1:8000/app5/retriveCourses", { params: { tpno } })
        .then((response) => {
          //   this.dataList = response.data.data;
          if (response.data.err_num == 0) {
            this.dataList = response.data.data;
            // alert(this.dataList.course__cname);
            console.log(this.dataList);
          } else {
            this.$message.warning("错误！+");
          }
        })
        .catch((error) => {
          this.$message.warning("error");
        });
    },
    isNumber(z_check_value) {
      var z_reg = /^(([0-9])|([1-9]([0-9]+)))$/;
      if (z_reg.test(z_check_value)) {
        return true;
      }
      return false;
    },
    checkcorrect(item) {
      // var iscorrect=true
      //  数据正确性校验
      if (item == null) {
        return false;
      }
      if (!this.isNumber(item)) {
        return false;
      }
      let tname = item.trim();
      if (!(tname.length > 0 && tname.length < 20)) {
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
            // this.listData = response.data.data;
            if (response.data.err_num == 0) {
              this.ifSuccess = true;
              this.students = response.data.data;
              console.log(this.students);
            //   this.courseFilter();
            } else {
              this.$message.warning("错误！");
              this.tpno = "";
            }
          })
          .catch((error) => {
            // this.$message.warning(error);
            console.log(error);
          });
      } else {
        this.$message.warning("错误！");
      }
    },
    onSubmitPlan() {
      if (!this.checkcorrect(this.tpno)) {
        let tpno = this.tpno;
        this.axios
          .get("http://127.0.0.1:8000/app4/retriveTeachPlan", {
            params: { tpno },
          })
          .then((response) => {
            // this.listData = response.data.data;
            if (response.data.err_num == 0) {
              this.ifSuccess = true;
              this.teachPlanNum = response.data.data;
              console.log(this.teachPlanNum);
                this.courseFilter();
            } else {
              this.$message.warning("错误！233");
              this.sno = "";
            }
          })
          .catch((error) => {
            // this.$message.warning(error);
            console.log(error);
          });
      } else {
        this.$message.warning("错误！123");
      }
    },
  },
};
</script>

<style >
</style>