from flask import Blueprint

blog_bp = Blueprint('blog_bp', __name__)

from .blog_views import *