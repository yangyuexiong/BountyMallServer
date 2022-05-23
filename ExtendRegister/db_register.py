# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 16:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : db_register.py
# @Software: PyCharm


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_db(app):
    """db注册"""
    db.init_app(app)
