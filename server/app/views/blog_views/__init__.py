from flask import Blueprint
import logging
import os
from hashlib import md5

blog_bp = Blueprint('blog_bp', __name__)

def init_app_logging():
    current_directory = os.path.dirname(__file__)
    three_levels_up = os.path.abspath(os.path.join(current_directory, '../../../'))
    log_file_directory = os.path.join(three_levels_up, 'logging')
    log_file_info = os.path.join(log_file_directory, 'app.log')
    if not os.path.exists(log_file_directory):
        print(f"目录 '{log_file_directory}' 不存在，正在创建...")
        os.makedirs(log_file_directory)

    file_info = logging.FileHandler(log_file_info)
    file_info.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%d/%b/%Y %H:%M:%S'))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_info)
    return logger

def md5_encryption(input):
    m = md5()
    m.update(input.encode())
    output = m.hexdigest()
    return output

from .index import *