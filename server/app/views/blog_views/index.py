from . import blog_bp
from flask import jsonify, request


@blog_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('Username')
    password =data.get('Password')
    return jsonify({'code': 200, 'msg': 'success'})
