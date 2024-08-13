# MyBlog 前端服务器

MyBlog 是一个前后端分离的博客应用，前端使用 Vue.js 构建，后端使用 Flask 构建。该项目包括用户认证、个人资料管理、博客文章的查看和编辑功能。

## 环境配置

1. 安装 node.js 和 npm

   - 下载并安装 [Node.js](https://nodejs.org/)
   - Node.js 安装包通常会包含 npm（Node 包管理器）
2. 安装 Vue CLI

   在命令行中运行以下命令安装 Vue CLI：

   ```
   npm install -g @vue/cli
   ```
3. 创建 Vue3 项目

   ```
   vue create client
   项目依赖有typescript、router、vuex
   ```
4. 安装相应的包

   ```
   cd client
   npm install axios
   npm install element-plus
   ```


## 项目结构

<pre>

/myblog
|-- /node_modules 		# 运行环境依赖（忽略,不上传）
|-- /public 			# 存放公共文件
|-- /src 			# 源代码目录
|   |-- /api                   	# 接口目录
|   |-- /assets                 # 静态文件目录（包括图片等）
|   |-- /backup                 # 组件的备份
|   |-- /components             # 组件
|   |-- /router             	# 路由
|   |-- /store             	# 状态管理
|   |-- /utils             	# 工具
|   |-- /views             	# 视图文件
|   |-- App.vue             	# 主应用组件
|   |-- main.ts             	# 程序的入口文件
|   |-- shims-vue.d.ts		# TypeScript 的声明文件
|-- .browserslistrc 		# 浏览器兼容性配置
|-- .eslintrc.js 		# ESLint 配置文件，定义代码风格和 lint 规则 
|-- .gitignore 			# Git 忽略文件配置，指定 Git 忽略的文件和目录
|-- package-lock.json 		# npm 锁定文件，确保一致的安装版本
|-- package.json 		# npm 配置文件，包含项目依赖、脚本等
|-- tsconfig.json 		# TypeScript 配置文件（如果使用 TypeScript


</pre>

## 项目运行

### 运行

```
   打开client文件夹
   npm run serve
```

### **打包**

```
   打开server文件夹
   npm run build
```

## **学习资料**

- Vue 官方文档：[Vue](https://cn.vuejs.org/)
- Element-Plus 官方文档：[Element-Plus](https://element-plus.org/zh-CN/)
