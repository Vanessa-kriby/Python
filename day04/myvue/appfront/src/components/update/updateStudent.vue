<template>

    <el-form ref="form" :model="listData" label-width="80px">

        <el-form-item label="学号">
          <el-input v-model="listData.sid"></el-input>
        </el-form-item>

        <el-form-item label="姓名">
          <el-input v-model="listData.stName"></el-input>
        </el-form-item>

        <el-form-item label="性别">
          <el-input v-model="listData.stGender"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即修改</el-button>
            <el-button>取消</el-button>
        </el-form-item>

    </el-form>

</template>

<script>
  export default {
    data() {
      return {
        listData: {
        sid: '',
        stName: '',
        stGender: '',
        
        }
      }
    },
    mounted() {
    },
    methods: {
        onSubmit:function() {
        var data=this.listData
            console.log(data)
            //       http://127.0.0.1:8000/updateStudent?sid=001&stName=林允儿&stGender=女
            this.axios.post('http://127.0.0.1:8000/app5/updateStudent',{data})
            .then(response => {
            })
            .catch(function  (error) {
                console.log(error);
            })   
        },
    }
  }
</script>