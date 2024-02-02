class Config:
    DEBUG = True
    TESTING = False
    # 数据库的配置信息
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'myblog'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 动态追踪修改设置，没有设置会有警告
    SQLALCHEMY_ECHO = False  # 查询时显示原始SQL语句
    SECRET_KEY = 'mySecretKey'
