from app import create_app, db

# 创建应用实例
app = create_app()

# 运行应用
if __name__ == '__main__':
    app.run()