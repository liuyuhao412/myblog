from flask import Flask
from .config import load_config
from .extensions import db


def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(load_config())

    # 初始化数据库
    db.init_app(app)

    # 注册蓝图
    from .views.blog_views import blog_bp as blog_blueprint
    app.register_blueprint(blog_blueprint)

    return app
