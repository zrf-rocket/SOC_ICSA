#-*- encoding:utf-8 -*-
# @author:SteveRocket
# @Date:2023/10/10
# @File:edr_service
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

import os
import time

def daemonprocess():
    while True:
        process_list = os.popen("ps -A")
        line = process_list.readline()
        target_process = "edr_agent"
        process_status = False
        update_status = False
        while line:
            infos = line.split()
            pid = infos[0]
            cmd = infos[3]
            if cmd == target_process:
                process_status = True
            elif cmd == "update":
                update_status = True
            line = process_list.readline()

        if not process_status:
            time.sleep(10)
            target_file = "/opt/edr_agent/edr_agent"
            file_status = os.path.isfile(target_file)
            cmds = "{0} terminal &".format(target_file)
            if file_status:
                try:
                    os.system(cmds)
                except Exception as e:
                    print(e)
            else:
                print("no process file")

        if not update_status:
            update_file = "/opt/edr_agent/cache/edr_agent/update"
            if os.path.isfile(update_file):
                os.system("chmod +x /opt/edr_agent/cache/edr_agent/*")
                cmds = "{0} &".format(update_file)
                os.system(cmds)
        time.sleep(10)

if __name__ == '__main__':
    daemonprocess()





