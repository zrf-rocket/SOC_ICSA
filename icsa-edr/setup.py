# -*- encoding:utf-8 -*-
# @author:SteveRocket
# @Date:2023/10/10
# @File:setup
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

import sys


class Controller():
    def __init__(self, action: str):
        if "setup" == action:
            self.setup()
        elif "restart" == action:
            self.restart()
        elif "uninstall" == action:
            self.uninstall()
        elif "update" == action:
            self.update()
        else:
            print("""参数输入错误，请输入如下参数：
setup：安装Agent
restart：重启Agent
uninstall：卸载Agent
update：更新Agent"""
                  )

    # 安装 setup
    def setup(self):
        print("start install......")
        print("install success......")

    # 重启 restart
    def restart(self):
        print("restart......")
        print("restart success......")

    # 卸载 uninstall
    def uninstall(self):
        print("start uninstall......")
        print("uninstall success......")

    # 更新 update
    def update(self):
        print("start update......")
        print("update success......")


if __name__ == '__main__':
    action = sys.argv[1:]
    controller = Controller(action=action)
