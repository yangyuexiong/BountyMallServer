# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 16:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : AppHook.py
# @Software: PyCharm

from flask import request


def app_before_request():
    print('=== app_before_request ===')
    path = request.path
    print(path)
    return


def app_after_request(response):
    print('=== app_after_request ===')
    return response
