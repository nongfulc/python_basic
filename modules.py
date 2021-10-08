# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/8
# @Version 1.0
# A module is basically a file containing a set of functions to include in your app.
# can use pip package manager to install modules

# import core modules
import datetime
import time
from datetime import date

from camelcase import CamelCase

now = datetime.datetime.now()
print(now)
print(date.today())
print(time.time())

c = CamelCase()
print(c.hump('hello world'))
