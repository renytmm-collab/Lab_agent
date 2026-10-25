<template>
    <div>欢迎您{{ userInfo?.name }}</div>
</template>

<script setup>
import {useUser} from '@/utils/user'
const {userInfo}=useUser()
</script>