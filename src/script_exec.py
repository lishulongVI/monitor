# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/11/1 下午5:44
"""
import subprocess
from subprocess import Popen

from const import web_shell


def exec_script():
    proc = Popen(args=[web_shell], shell=True, stdout=subprocess.PIPE)
    return proc.stdout.read().decode('utf-8').split('\n')

# exec_script()
