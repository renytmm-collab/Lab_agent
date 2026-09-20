<template>
  <div class="common-layout">
    <el-container style="min-height: 100vh">
      <el-header style="display:flex;border-bottom: 1px solid #ddd;background-color: #fff;align-items: center;">
        <div style="flex:1;display:flex;align-items: center;font-size: 24px;font-weight:bold">
            <img src="@/assets/css/images/logo.png" alt="Logo" style="height: 40px; margin-right: 10px" />
            <div>智能实验室预约系统</div>
        </div>
        <div style="display:flex;align-items: center;">
            <img src="@/assets/css/images/logo.png" alt="" style="width: 30px; border-radius: 50%;" />
            <div style="margin-left: 3px;">管理员</div>
        </div>
      </el-header>
      <el-container>
        <el-aside width="220px">
            <el-menu router style="height: 100%;border-right: 1px solid #ddd" :default-active="$route.path">
                <el-menu-item index="/manager/home">
                    <el-icon><icon-menu /></el-icon>
                    <span>系统首页</span>
                </el-menu-item>
                <el-menu-item index="/manager/lab">
                    <el-icon><House /></el-icon>
                    <span>实验室管理</span>
                </el-menu-item>
                <el-menu-item index="/manager/equ">
                    <el-icon><Setting /></el-icon>
                    <span>设备列表管理</span>
                </el-menu-item>
                <el-menu-item index="/manager/user">
                    <el-icon><User /></el-icon>
                    <span>用户管理</span>
                </el-menu-item>
            </el-menu>
        </el-aside>
        <el-main>
            <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import {Document,Menu as IconMenu,Location,Setting,User,House} from '@element-plus/icons-vue'
</script>