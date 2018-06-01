# 创建蓝本程序

from flask import Blueprint

main = Blueprint('main', __name__)

from . import forms, views
