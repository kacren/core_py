#!/usr/bin/env python3

import random

#1. 提示并获取用户的输入
player = int(input('请输入 0剪刀 1石头 2布：'))

#2. 让电脑出一个随机数
computer = random.randint(0,2)

#3. 判断用户的输入,然后显示对应的结果
#if 玩家获胜的条件:
if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
    print('你赢了')
#elif 玩家平局的条件:
elif player==computer:
    print('平局')
else:
    print('你输了')
