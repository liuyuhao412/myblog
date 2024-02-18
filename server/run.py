from app import create_app

# 创建应用实例
app = create_app()
app.logger.disabled = True

# 运行应用
if __name__ == '__main__':
    app.run()