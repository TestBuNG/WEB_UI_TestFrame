"""
import subprocess
import os
import signal
import logging
import time

base_dir = os.path.dirname(os.getcwd())
testcase_dir = base_dir + '\\testcase'
print(testcase_dir)


def run():
    try:
        logging.info('====== <执行pytest命令> =====')
        p = subprocess.Popen('pytest -v test_login.py', cwd=testcase_dir)
        time.sleep(3)
        logging.info('=====< 开启进程的pid-> '+str(p.pid)+'=====')
        #os.kill(r.pid, signal.SIGKILL)
    except TimeoutError:
        print("命令执行失败")
run()
"""
