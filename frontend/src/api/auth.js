import request from '@/utils/request'

export function Register(data) {
    return request({
        url: '/api/auth/register',
        method: 'post',
        data,
    })
}

//登录请求
export function Login(data){
    return request ({
        url:'/api/auth/login',
        method:'post',
        data
    })
}
