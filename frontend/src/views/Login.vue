<template>
    <div class="login-container">
        <div class="login-box">
            <h1 style="font-size:28px">实验室预约系统</h1>
            <div style="margin-top:5px;margin-bottom:20px">基于agent的智能预约系统</div>
            <el-form :model="form" label-width="auto" style="max-width:600px">
                <el-form-item>
                    <el-input size="large" v-model="form.username" placeholder="请输入用户名" :prefix-icon="User" />
                </el-form-item>
            </el-form>
            <el-form :model="form" label-width="auto" style="max-width:600px">
                <el-form-item>
                    <el-input type="password" size="large" v-model="form.password" placeholder="请输入密码" :prefix-icon="Lock" show-password />
                </el-form-item>
            </el-form>
            <div>
                <el-button type="primary" size="large" style="width:100% "@click="login" :loading="loadingValue">登录</el-button>
                <div style="text-align:right;margin-top:20px">还没有账号？请 <a style="color:var(--el-color-primary)"href="/register">注册</a></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {reactive,ref} from 'vue';
import {User,Lock} from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'
import { Login as loginApi } from '@/api/auth'
import { useUser } from '@/utils/user'

const form = reactive({
    username:'',
    password:''

})

const loadingValue = ref(false)

const router = useRouter()

const { saveLoginData } = useUser()

const login = async () => {
    loadingValue.value = true
    try {
        const res = await loginApi(form)
        if (res.code === 200) {
            saveLoginData(res.data)
            ElMessage.success('登录成功')
            router.push('/manager/home')
        } else {
            ElMessage.error(res.message || '登录失败')
        }
    } catch (e) {
        ElMessage.error('网络异常，请稍后再试')
    } finally {
        loadingValue.value = false
    }
}

</script>

<style scoped>
.login-container{
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
.login-box{
    width:380px;
    border-radius: 8px;
    box-shadow: 0 8px 12px rgba(0,0,0,0.1);
    padding: 30px;
    text-align: center;
    background-color: white;
}
</style>