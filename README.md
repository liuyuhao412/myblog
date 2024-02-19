# 项目操作手册

## **项目结构**

<pre> 
/myblog
|-- /client (前端应用) 
|   |-- /public 
|   |-- /src 
|   |   |-- /assets (静态资源) 
|   |   |-- /components (可复用的组件) 
|   |   |-- /router (前端路由配置) 
|   |   |-- /views (页面组件) 
|   |   |-- App.vue 
|   |   |-- main.js 
|   |-- /node_modules(运行环境)
|-- /server (后端应用) 
|   |-- /app
|   |   |-- /config (配置文件) 
|   |   |-- /models (数据库模型) 
|   |   |-- /views(视图) 
|   |   |-- extensions.py (初始化Flask扩展)
|   |-- /migrations(数据库迁移文件) 
|   |-- /MySQL_backup(数据库备份文件) 
|   |-- run.py (项目运行) 
|   |-- manage.py (管理脚本)
|   |-- requirements.txt (项目依赖) 
|   |-- /venv(运行环境)
|-- .gitignore 
|-- README.md
</pre>
## 操作步骤

### 环境配置

#### 配置前端环境

1. 安装 node.js 和 npm
   * 下载并安装 [Node.js](https://nodejs.org/)
   * Node.js 安装包通常会包含 npm（Node 包管理器）

2. 安装Vue CLI

   在命令行中运行以下命令安装 Vue CLI：

   ```
   npm install -g @vue/cli
   ```
3. 安装相应的包
   ```
   npm install axios
   npm install element-plus
   ```

#### 配置后端环境

 1. 安装 Python（此项目是python3.8）

    * 下载并安装 [Python](https://www.python.org/)

    * 安装virtualenv

      ```
      pip install virtualenv
      ```

 2. 创建虚拟环境

    ```
    cd .\server
    virtualenv venv
    virtualenv -p "你的python路径\python.exe" venv
    ```

 3. 激活虚拟环境

    ```
    cd .\server\venv\Scripts
    .\activate
    ```

 4. 安装环境依赖

    ```
    pip install -r requirements.txt
    ```

#### 配置数据库

 1. 安装并配置[MySQL](https://www.mysql.com/cn/)数据库
 2. 在 `.\server\app\config` 目录中的配置文件中设置数据库连接参数。
 3. 初始化数据库
    ```
    cd server
    python manage.py init_db
    ```
 4. 若执行迁移操作
     * 初始化迁移数据库
        ```
        cd server
        set FLASK_APP=manage.py
        flask db init
        ```
     * 生成迁移脚本
        ```
        cd server
        flask db migrate -m "数据库迁移的提示消息"
        ```
     * 执行迁移操作
        ```
        cd server
        flask db upgrade
        ```
     * 执行迁移回滚操作
        ```
        cd server
        flask db downgrade
        ```
5. 数据库备份和还原
     * 备份数据库
        ```
        cd server
        python manage.py backup_db
        ```
     * 还原数据库
        ```
        cd server
        python manage.py restore_db
        ```
#### 运行前后端应用

1. 运行前端

   ```
   cd .\client
   npm run serve
   ```

2. 运行后端（前，先初始化数据库）

   ```
   cd .\server
   python run.py
   ```

   

## 状态码

| 状态码 | 说明                     |
| ------ | ----                     |
| 200    | 登录成功                 |
| 201    | 登录失败                 |

## **学习资料**

- Flask 官方文档： [Flask](https://www.osgeo.cn/flask/)
- Flask-SQLAlchemy 官方文档： [SQLAlchemy](http://www.pythondoc.com/flask-sqlalchemy/)
- Flask-Migrate 官方文档： [Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- Vue 官方文档：[Vue](https://cn.vuejs.org/)
- Element-Plus 官方文档：[Element-Plus](https://element-plus.org/zh-CN/)

