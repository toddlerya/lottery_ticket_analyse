#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: qguo
#date: 20160523

"""
双色球:
33个可选数字球，标记为从1—33，玩家可选7个,
其中6个为红球(1—33)，1个为蓝球(1—16),
每个号码只选1次(红球与篮球可以重复),不可重复选择
"""

import numpy as np

def get_ball(start,end):
	return np.random.randint(int(start),int(end)+1)

def generate_num():
	red_ball = []
	blue_ball = get_ball(1,16)
	while len(red_ball) < 6:
		number = get_ball(1,33)
		red_ball.append(number)
		set(red_ball)
	return 'red', str(red_ball)[1:-1], 'blue', blue_ball

def main():
	for i in range(100000):
		with open('result.log', 'a+') as f:
			# f.writelines(str(generate_num())[1:-1]+'\n')
			print str(generate_num())[1:-1]

if __name__ == '__main__':
	main()