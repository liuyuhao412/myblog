from . import blog_bp,init_app_logging
from flask import jsonify, request
from app.models.model import User

logger = init_app_logging()

@blog_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    Username = data.get('Username')
    Password = data.get('Password')
    ip_address = request.headers.get('X-Forwarded-For')
    if not ip_address:
        ip_address = request.remote_addr
    request_method = request.method
    request_path = request.path
    http_version = request.environ.get('SERVER_PROTOCOL')
   
    #登录
    loginUser = User.query.filter(User.Username == Username).first()
    if loginUser:
        if loginUser.Password == Password:
            status_code = 200
            msg = '用户登录成功'
        else:
            status_code = 201
            msg = '用户名或密码错误'
    else:
        status_code = 201
        msg = '用户不存在'
         # 记录日志
    log_message = f"Username: {Username}, IP: {ip_address}, " \
                  f"Request: {request_method} {request_path} {http_version}, Status Code: {status_code}," \
                  f"Message: {msg} "
    logger.info(log_message)
    return jsonify({'code': status_code, 'msg': msg})
    