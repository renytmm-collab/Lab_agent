import request from '@/utils/request'

//登录请求
export function Login(data){
    return request ({
        url:'/api/auth/login',
        method:'post',
        data
    })
}