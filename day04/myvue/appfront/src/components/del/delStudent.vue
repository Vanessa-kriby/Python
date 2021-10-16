<template>

    <el-form ref="form" :model="listData" label-width="80px">

        <el-form-item label="学生">
          <!-- <el-input v-model="form.stu"></el-input> -->
          <el-select v-model="listData.stid" placeholder="请选择学生">
            <el-option
                  v-for="item in studentvalue"
                  :key="item.sno"
                  :label="item.sname"
                  :value="item.sno">
            </el-option>
         </el-select>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即删除</el-button>
            <el-button>取消</el-button>
        </el-form-item>

    </el-form>

</template>

<script>
  export default {
    data() {
      return {
        listData:[],
            studentvalue:[],
            listData: {
            stid: '', 
        }
      }
    },
    mounted() {
        this.getlistStudent()
    },
    methods: {
        onSubmit:function(){
            var data=this.listData
            console.log(data)
            //      http://127.0.0.1:8000/delStudent?stid=001
            this.axios.post('http://127.0.0.1:8000/app5/delStudent',{data})
            .then(response => {

            })
            .catch(function  (error) {
                console.log(error);
            })
        },
        getlistStudent:function(){
            this.axios.get('http://127.0.0.1:8000/app5/showStudents')
            .then(response => {
                this.studentvalue = response.data.data
            })
            .catch(function (error) {
                console.log(error);
            })
        },      

    }
  }
</script>