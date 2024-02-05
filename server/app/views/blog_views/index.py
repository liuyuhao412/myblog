from . import blog_bp
from flask import jsonify, request


@blog_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    Username = data.get('Username')
    Password = data.get('Password')
    ip_address = request.remote_addr
    request_method = request.method
    request_path = request.path
    http_version = request.environ.get('SERVER_PROTOCOL')
    status_code = 200  # 在此示例中，你可以根据实际情况设置状态码

    # 记录日志
    log_message = f"Username: {Username}, IP: {ip_address}, " \
                  f"Request: {request_method} {request_path} {http_version}, Status Code: {status_code}"
    logging.info(log_message)

    return jsonify({'code': 200, 'msg': 'success'})
