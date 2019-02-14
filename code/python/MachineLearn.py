# -*- coding: utf-8 -*- 

#====================================================
#一元线性回归
#====================================================

# import numpy as np
# import matplotlib.pyplot as plt

# a_start =1
# b_start =0

# ##学习预测的损失函数评估
# def LearnLoss(hource,a,b):
# 	learn_price = learnPrice(hource,a,b)
# 	diff = learn_price - hource.getSalePrice()
# 	return pow(diff,2)

# ##返回预测的价格结果 
# def learnPrice(hource,a,b):
# 	return a*hource.getArea() + b

# ##当ab两个变量值一定时  统计所有样本的平均损失
# def statisticsLoss(a,b):
# 	loss = 0
# 	sample = sampleList()
# 	for i in sample:
# 		loss += LearnLoss(i,a,b)
# 	return loss / len(sample)

# ##经过求导得出损失函数L=(y<预测> - y) 对于a与b的偏导数
# ##损失函数L 对于a的偏导数为 (y_prediction - y)*x
# ##损失函数L 对于b的偏层数为 (y_prediction - y)
# def train(learning_gradient = 0.4):
# 	global a_start,b_start
# 	times = 10000
# 	tempLoss = 100;
# 	while times > 0 and  tempLoss - statisticsLoss(a_start,b_start) > 0.00000001:
# 		times -= 1
# 		tempLoss = statisticsLoss(a_start,b_start);
# 		resultMap = calculatePartialDerivatives(a_start,b_start)
# 		a_start -= learning_gradient * resultMap["a_derivative"]
# 		b_start -= learning_gradient * resultMap["b_derivative"]
# 		print("[%-4d]  ===>>>  a=%7.6f;  b=%7.6f;  statisticsLoss = %9.8f" % (10000 - times,a_start,b_start,statisticsLoss(a_start,b_start)))
# 	resultMap = {"a_val":a_start,"b_val":b_start}
# 	return resultMap

# ##在学习过程中我们要使用多个样本  也就是多个样本的的损失和最小  最此要求总损失函数L=∑((y_prediction - y)^2)
# ##由函数的和的求导法则得出所有损失函数的和的求导等于损失函数导数的和 所以函数的平均值的求导的平均值等于损失函数导数的平均值
# def calculatePartialDerivatives(a,b):
# 	a_derivative = 0
# 	b_derivative = 0
# 	##计算每个样本对于损失函数的偏导数求平均值
# 	sample = sampleList()
# 	for hourse in sample:
# 		y_prediction = learnPrice(hourse,a,b)
# 		a_derivative += (y_prediction - hourse.getSalePrice()) * hourse.getArea()
# 		b_derivative += (y_prediction - hourse.getSalePrice())
# 	resultMap = {"a_derivative":a_derivative/len(sample),"b_derivative":b_derivative/len(sample)}
# 	return resultMap

# ##用于测试结果集和预测结果
# def test(list,a,b):
# 	for hourse in list:
# 		print("面积：%f  ; 预测结果：   %f  ;实测结果：  %f  ;误差： %f%%" % (hourse.getArea(),learnPrice(hourse,a,b),hourse.getSalePrice(),100 * abs(learnPrice(hourse,a,b) - hourse.getSalePrice()) / hourse.getSalePrice()))

# ##定义学习样本
# def sampleList():
# 	hourseList = []
# 	hourseList.append(Hourse(0.85,7.05))
# 	hourseList.append(Hourse(1.08,8.95))
# 	hourseList.append(Hourse(1.118,9.25))
# 	hourseList.append(Hourse(1.17,9.7))
# 	hourseList.append(Hourse(1.19,9.88))
# 	hourseList.append(Hourse(1.25,10.35))
# 	hourseList.append(Hourse(1.309,10.82))
# 	return hourseList

# def main():
# 	abval = train()
# 	print("【测试结果】".center(40,"*"))
# 	test(sampleList(),abval["a_val"],abval["b_val"])
# 	for h in sampleList():
# 		plt.scatter(h.getArea(),h.getSalePrice())
# 	x = np.linspace(0.6,1.5,90);
# 	y = abval["a_val"] * x + abval["b_val"]
# 	plt.plot(x, y)
# 	print("【测试结果】".center(40,"*"))
# 	hourse = Hourse(1.2,0)
# 	print("1.2结果 = %f" % learnPrice(hourse,abval["a_val"],abval["b_val"]))
# 	plt.show()
#sklenarn===============================================================

from sklearn.linear_model import LinearRegression

import numpy as np
import matplotlib.pyplot as plt


##定义学习样本
def sampleList():
	hourseList = []
	hourseList.append(Hourse(0.85,7.05))
	hourseList.append(Hourse(1.08,8.95))
	hourseList.append(Hourse(1.118,9.25))
	hourseList.append(Hourse(1.17,9.7))
	hourseList.append(Hourse(1.19,9.88))
	hourseList.append(Hourse(1.25,10.35))
	hourseList.append(Hourse(1.309,10.82))
	return hourseList


def main():
	hourseList = sampleList()
	xdata = []
	ydata = []
	for hourse in  hourseList:
		plt.scatter(hourse.getArea(),hourse.getSalePrice())
		xdata.append((hourse.getArea(),1))
		ydata.append((hourse.getSalePrice(),2))
	#创建模型
	print(xdata)
	model = LinearRegression()
	model.fit(xdata,ydata)
	plt.plot(xdata,model.predict(xdata),'r')
	plt.ylim((6,12))
	plt.show()


#通用执行===============================================================
class Hourse(object):
  def __init__(self,area,salePrice):
  	self.area = area
  	self.salePrice = salePrice

  def getSalePrice(self):
  	return self.salePrice

  def getArea(self):
  	return self.area

main()
