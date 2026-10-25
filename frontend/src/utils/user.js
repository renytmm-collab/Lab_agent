//仅供setup函数使用

import {ref} from 'vue'
import {getUserInfo,setToken,setUserInfo,removeToken,removeUserInfo} from './auth'

const userInfo=ref(getUserInfo()) //响应式对象 随时更新最新的值

export function useUser(){
    //登录成功后调用：存token、存用户信息、更新响应式状态
    function saveLoginData(data){
        setToken(data.token)
        setUserInfo(data.user)
        userInfo.value=data.user
    }

    //修改资料后调用
    function updateUser(user){
        setUserInfo(user)
        userInfo.value=user
    }

    //从localStorage重新读取（比如其它地方改了存储）
    function reloadUser(){
        userInfo.value=getUserInfo()
    }

    //退出登录：清存储 + 清响应式状态（只清存储的话界面不会变）
    function clearUser(){
        removeToken()
        removeUserInfo()
        userInfo.value=null
    }

    return {
        userInfo,
        saveLoginData,
        updateUser,
        reloadUser,
        clearUser
    }
}
