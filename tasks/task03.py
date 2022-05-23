# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 16:34
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : task03.py
# @Software: PyCharm


from tasks.celery import cel


@cel.task
def execute_main(test_obj):
    return "执行完成"
