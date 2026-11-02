<template>
    <div class="register-container">
        <div class="register-box">
            <h1 style="font-size:28px;margin-bottom:30px">欢迎注册实验室预约系统</h1>
            <el-form ref="formRef" :rules="rules" :model="form" label-width="0px" style="width:100%">
                <el-form-item prop="username">
                    <el-input size="large" v-model="form.username" placeholder="请输入用户名" :prefix-icon="User" />
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" size="large" v-model="form.password" placeholder="请输入密码" :prefix-icon="Lock" show-password />
                </el-form-item>
                <el-form-item prop="confirmPassword">
                    <el-input type="password" size="large" v-model="form.confirmPassword" placeholder="请确认密码" :prefix-icon="Lock" show-password />
                </el-form-item>
            </el-form>
            <div>
                <el-button type="primary" size="large" :loading="loadingValue" style="width:100%" @click="register">注册</el-button>
                <div style="text-align:right;margin-top:20px">已有账号？请 <router-link style="color:var(--el-color-primary)" to="/login">登录</router-link></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {reactive, ref} from 'vue';
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'
import {User,Lock} from '@element-plus/icons-vue'
import {Register} from '@/api/auth'

const formRef = ref(null);
const router = useRouter()

const form = reactive({
    username:'',
    password:'',
    confirmPassword:''
})

const loadingValue = ref(false)

const validatePassword = (rule, value, callback) => {
    if (new TextEncoder().encode(value).length > 72) {
        callback(new Error('密码不能超过72字节（中文通常占3字节）'))
    } else {
        callback()
    }
}

const validatePass=(rule,value,callback)=>{
    if(value==''){
        callback(new Error('请确认密码'))
    }else{
        if(value!==form.password){
            callback(new Error('两次输入的密码不一致'))
        }else{
            callback()
        }
    }
}

const rules={
    username: [
        { required: true, whitespace: true, message: '请输入账号', trigger: 'blur' },
        { max: 50, message: '账号不能超过50个字符', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { validator: validatePassword, trigger: 'blur' }
    ],
    confirmPassword: [
        {validator:validatePass,trigger:'blur'}
    ]
}

const register = async () => {
    if (loadingValue.value) return
    const valid=await formRef.value.validate().catch(()=>false)
    if(!valid){return}
    loadingValue.value = true
    try {
        const res = await Register({
            username: form.username,
            password: form.password,
        })
        if (res.code === 200) {
            ElMessage.success('注册成功')
            router.push('/login')
        } else {
            ElMessage.error(res.message || '注册失败')
        }
    } catch (e) {
        ElMessage.error(e.response?.data?.message || '网络异常，请稍后再试')
    } finally {
        loadingValue.value = false
    }
}

</script>

<style scoped>
.register-container{
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
.register-box{
    width:380px;
    border-radius: 8px;
    box-shadow: 0 8px 12px rgba(0,0,0,0.1);
    padding: 30px;
    text-align: center;
    background-color: white;
}
</style>
