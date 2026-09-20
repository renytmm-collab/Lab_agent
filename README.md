# 实验室预约与管理系统

## 📖 项目简介
跟随B站UP主程序员青戈敲的项目，视频教程请看https://www.bilibili.com/video/BV13hbP6zEUd/?spm_id_from=333.788.videopod.sections&vd_source=61f18de49336dedc8394c25c018863f0，目前做到第二节后续持续更新

## 📂 项目目录结构说明

```text
lab_agent/
├── frontend/                  # 前端工程目录
│   ├── public/                # 公共静态文件（网站图标等）
│   ├── src/
│   │   ├── assets/            # 全局样式（global.css）及图片静态资源
│   │   ├── layouts/           # 页面骨架布局（Layout.vue 顶部栏与侧边导航）
│   │   ├── router/            # 路由配置文件（index.js 嵌套路由定义）
│   │   ├── views/             # 各业务页面（Home.vue 首页、Lab.vue 实验室管理等）
│   │   ├── App.vue            # 根组件（全局顶级路由视图出口）
│   │   └── main.js            # 入口文件（挂载 Vue、Router、Element Plus 等）
│   ├── package.json           # 前端依赖与脚本命令配置
│   └── vite.config.js         # Vite 构建工具与路径别名配置（@ 映射至 src）
├── Backend/                   # 后端工程预留目录
├── .gitignore                 # Git 版本控制忽略项配置
└── README.md                  # 项目说明文档
```

---

## 🚀 本地运行与开发指南

### 1. 环境准备
* 运行环境：[Node.js](https://nodejs.org/)（推荐版本 `^22.18.0` 或 `>=24.12.0`）
* 包管理工具：`npm`

### 2. 获取源码
```bash
git clone https://github.com/renytmm-collab/Lab_agent.git
cd Lab_agent
```

### 3. 启动前端服务
进入前端子工程目录：
```bash
cd frontend
```

安装依赖：
```bash
npm install
```

启动本地开发服务器（支持实时热更新）：
```bash
npm run dev
```
服务启动后，使用浏览器访问 `http://localhost:5173/` 即可进入管理系统。

### 4. 项目打包构建
若需编译为生产环境静态文件：
```bash
npm run build
```
打包输出目录为 `frontend/dist/`。

### 5. 代码格式化
运行 Prettier 格式化 `src/` 下的代码：
```bash
npm run format
```

---

## 📄 开源许可证
本项目遵循 [MIT 开源许可证](LICENSE)。
