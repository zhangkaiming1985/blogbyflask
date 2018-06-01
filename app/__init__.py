from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
	# 工厂函数

	app = Flask(__name__)
	# 载入配置
	app.config.from_object(config[config_name])
	# 初始化
	config[config_name].init_app(app)

	# 完成各类初始化
	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)

	# 注册蓝本
	from .main import main as main_buleprint
	app.register_blueprint(main_buleprint)

	# 附加路由和定义错误页面

	return app
