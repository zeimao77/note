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
    if len(pidSet) > 0:
        print("查找到占用[%d]端口的进程:[%s]" % (port,pidSet))
    return pidSet

def killPID(pid):
    if len(pid) > 0 and pid.isdigit():
        result = os.popen(KILLPID_BYSTR + pid)
        res = result.read()
        if res.startswith("成功: "):
            print("[√]:"+res[3:])
        else:
            print("[×]:"+res)

def main(port_list):
    for i in range(1, len(port_list)):
        print("正在处理端口：%s" % sys.argv[i])
        result = findPID(int(sys.argv[i]))
        for item in result:
            killPID(item)
    print("[处理完毕]".center(30,'*'))

if __name__ == '__main__':
    main(sys.argv)

