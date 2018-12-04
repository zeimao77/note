import os
import sys

FIND_BYSTR = 'netstat -aon|findstr '
KILLPID_BYSTR = 'taskkill -F -PID '  # 杀死pid

def findPID(port):
        pidSet = set()  # 用于存放pid
        result = os.popen(FIND_BYSTR + str(port))
        res = result.read()
        for line in res.splitlines():
            if line.find("TCP") > 0 or line.find("UDP") > 0:
                pidSet.add(line[::-1].split(" ", 1)[0][::-1])
        print("查找到占用[%d]端口的进程:[%s]" % (port,pidSet))
        return pidSet

def findInforByPid(pid):
        if len(pid)>0:
            result = os.popen(FIND_INFOR_BYPID + pid)
            res = result.read()
            for line in res.splitlines():
                if len(line.strip()) > 0:
                    return line.strip()
        return ""

def killPID(pid):
    if len(pid) > 0 and pid.isdigit():
        result = os.popen(KILLPID_BYSTR + pid)
        res = result.read()


def do():
    for i in range(1, len(sys.argv)):
        print("即将处理端口：%s" % sys.argv[i])
        result = findPID(int(sys.argv[i]))
        for item in result:
            print("即将杀死进程：%s" % item)
            killPID(item)
    print("处理完毕！！！")

do()

