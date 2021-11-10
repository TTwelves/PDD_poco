# -*- encoding=utf8 -*-
__author__ = "1"

import random

import yaml
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/RKPRCEVOYTBQVCOF?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH",])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def random_second():
    second = random.randint(3, 20)
    return int(second)

def save_yaml(data: list):
    with open('./pdd-cat.yaml', 'a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    datas = []

    while True:
        goods_list = poco("android:id/content").offspring("com.xunmeng.pinduoduo:id/alr").offspring(
            "com.xunmeng.pinduoduo:id/cx7").child("android.widget.FrameLayout")

        for g in goods_list:
            data = []
            name1 = g.offspring("com.xunmeng.pinduoduo:id/tv_title").get_text()
            data.append(name1)
            price1 = g.offspring("com.xunmeng.pinduoduo:id/efu").get_text()
            data.append(price1)
            sale_num = g.offspring("com.xunmeng.pinduoduo:id/ek9").get_text()
            data.append(sale_num)
            print(data)
            datas.append(data)

        poco.scroll(direction="vertical", percent=0.5, duration=1.0)
        sleep(random_second())
        save_yaml(datas)
        datas = []
