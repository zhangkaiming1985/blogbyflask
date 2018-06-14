# 创建蓝本：用户认证相关路由

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views