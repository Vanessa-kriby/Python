 <template>
    <el-table
      :data="listData"
      style="width: 100%">
      <el-table-column
        prop="gno"
        label="班级编号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="gname"
        label="班级名称"
        width="180">
      </el-table-column>
    </el-table>
  </template>

  <script>
        export default {
            data() {
            return {
                 listData: [],
                 gno:"",
                 gname:"",
                
            }
         },
            mounted(){
                this.getCourse()
            },
            methods:{
            getCourse: function (event){
                this.axios.get('http://127.0.0.1:8000/app1/showGrades').then((response)=>{
                    this.listData=response.data.data
                    console.log(this.listData)
                })
            },
        },
    }
    </script>    