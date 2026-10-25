//存储用户信息，获取token、用户信息，删除token
const TOKEN_KEY='token'
const USER_KEY='userInfo'

export function getToken(){
    return localStorage.getItem(TOKEN_KEY)
}

export function setToken(token){
    localStorage.setItem(TOKEN_KEY,token)
}

export function removeToken(){
    localStorage.removeItem(TOKEN_KEY)
}

export function getUserInfo(){
    const str=localStorage.getItem(USER_KEY)
    if(!str) return null
    try{
        return JSON.parse(str)
    }catch{
        //存储里的内容不是合法 JSON（比如旧版本写入的脏数据）
        //返回 null，避免整个应用加载时崩溃
        return null
    }
}

export function setUserInfo(user){
    localStorage.setItem(USER_KEY,JSON.stringify(user))
}

export function removeUserInfo(){
    localStorage.removeItem(USER_KEY)
}


//登出
export function logout(){
    removeToken()
    removeUserInfo()
}
