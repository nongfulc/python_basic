# -*- coding: utf-8 -*-
# @Author lc_666
# @Date 2021/10/8
# @Version 1.0
# handle json
import json

peter = '''
{
"name":"Peter","age":90
}
'''

p = json.loads(peter)

print(p)
print(p.get('name'))

car = {'brand': 'BMW', 'price': 1000}
print(json.dumps(car))
