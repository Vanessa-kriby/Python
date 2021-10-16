<template>
    <el-form ref="from" :model="listData" label-width="80px">
        <el-form-item  label="选课清单">
            <el-select v-model="listData.ino" placeholder="请选择要删除的选课结果">
                <el-option
                    v-for="item in Inventoryvalue"
                    :key="item.ino"
                    :label="item.ino"
                    :value="item.ino">
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
    data(){
        return{
            listData:[],
            Inventoryvalue:[],
            listData:{
                ino:"",
            }
        }
    },
    mounted(){
        this.getInventory()  
    },
    methods:{
        onSubmit:function(){
            var data=this.listData  //deid
            console.log(data);
            //   http://127.0.0.1:8000/delTeacher?teid=111
            this.axios.post('http://127.0.0.1:8000/app6/delInventory',{data})
            .then((response)=>{
                if (response.data.err_num == 1) {
                this.$message({
                    message: "失败！" + response.data.msg,
                    type: "warning",
                    });
                }
                if (response.data.err_num == 0) {
                    this.$message({
                        message: "删除成功！",
                        type: "success",
                    });
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        },


        getInventory:function (){
             this.axios.get("http://127.0.0.1:8000/app6/showInventorys").then((response)=>{
                    this.Inventoryvalue=response.data.data
                    // console.log(this.gradevalu)
                    })
                    .catch(function (error) {
                    console.log(error);   
                    })
        },
    },
}
</script>
    