import axios from "axios";
import { getToken } from "./auth";

console.log('VITE_API_BASE_URL',import.meta.env.VITE_API_BASE_URL)

const service =axios.create({
    baseURL:import.meta.env.VITE_API_BASE_URL,
    timeout:30000  //30秒
})

service.interceptors.request.use(config=>{
    const token=getToken()
    if(token){
        config.headers.Authorization=`Bearer ${token}`
    }
    return config
})

service.interceptors.response.use(
    res => {
        console.log('响应成功:', {
            status: res.status,
            code: res.data?.code,
            message: res.data?.message,
        })
        return res.data
    },
    error => {
        console.error('请求失败:', {
            code: error.code,
            status: error.response?.status,
            message: error.response?.data?.message || error.message,
        })
        return Promise.reject(error)
    }
)

export default service
