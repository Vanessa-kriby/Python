<template>
    <div>
        <span type="padding-left:10px;">
            <el-button type="primary" round @click="addAllRecord()">更新所有</el-button>
        </span>
        <el-table :data="tableData" border style="width: 100%">
        <el-table-column prop="tno" label="工号" width="320"></el-table-column>
            <el-table-column prop="teachCourse__cname" label="所教课程" width="180">
                <template slot-scope="scope">
                    <el-select v-model="scope.row.teachCourse__cno" placeholder="请选择课程">
                        <el-option v-for="item in courseList" :key="item.cno" :label="item.cname" :value="item.cno"></el-option>
                    </el-select>
                </template>
            </el-table-column>

            <el-table-column>
                <template slot-scope="scope">
                    <el-button size="small" type="info" round @click.native="editrecord(scope.row,scope.$index)">编辑</el-button>
                    <el-button size="small" type="warning" round @click.native="handledelete(scope.row,scope.$index)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            tableData: [],
            courseList: [],
            teacherList: [],
            tableUpdate: [],
        };
    },
    mounted() {
        this.getCourse();
        this.getTeachCourse();
    },
    methods: {
        addAllRecord() {
            this.tableUpdate=[]
            this.tableData.forEach(item => {
                if(item.teachCourse__cno!=null) {
                    this.tableUpdate.push(item)
                }
            })
            // console.log(this.tableUpdate)
            this.addTeacher(this.tableUpdate)
            this.getTeachCourse()
        },
        addrecord() {
        },
        editrecord(row, index) {    
            let brand =[];
            brand.push(row)
            this.onUpdate(brand)
            this.getTeachCourse()
        },
        handledelete(row, index) {
                var brand = new Object();
                brand.tno = row.tno;
                brand.teachCourse__cno = row.teachCourse__cno;

                var data = brand;
                // console.log(data);
                this.axios
                  .post("http://127.0.0.1:8000/app4/delTeachCourse", { data })
                  .then(response => {
                    // this.listData = response.data.data;
                    if (response.data.err_num == 1) {
                      this.$message({
                        message: "失败！" + response.data.msg,
                        type: "warning"
                      });
                    } else {
                      this.$message({
                        message: "删除成功！",
                        type: "warning"
                      });
                    }
                  });
            this.getTeachCourse()
        },
        getCourse() {
            this.axios.get('http://127.0.0.1:8000/app2/showCourses').then((response)=>{
                this.courseList=response.data.data
                // console.log(this.courseList);
            })
        },
        getTeachCourse() {
            this.axios.get('http://127.0.0.1:8000/app4/getTeachCourse').then((response) =>{ 
                this.tableData=response.data.data
                // console.log(this.tableData)
            })
        },
        addTeacher(data) {
            this.axios.post('http://127.0.0.1:8000/app4/addTeachCourse',{data}).then((response) =>{
                this.tableData=response.data.data
                // console.log(this.tableData)
            })
        },
        onUpdate(data) {
            this.axios.post('http://127.0.0.1:8000/app4/updateTeachCourse',{data}).then((response) =>{
                this.tableData=response.data.data
                // console.log(this.tableData)
            })
        }
    }
}
</script>