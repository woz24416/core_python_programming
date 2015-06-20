#coding=utf-8

#Exercise2-5:
i = 0
while i <=10:
	print i
	i += 1

# use for loop
for i in range(11):
	print i,


#Exercise 2-7
input_str = raw_input('Please enter a string:')
i = 0
while i < len(input_str):
	print input_str[i],
	i += 1

# use for loop
input_str = raw_input('Please enter a string:')
for s in input_str:
	print s


#Exercise 2-8
# use while loop
v = []
i = 0
s = 0
while i < 5:
	a = int(raw_input('Please enter a number:'))
	v.append(a)
	s = s + v[i]
	i += 1
print v
print s

# use for loop
number = 0
for i in range(5):
	number += int (raw_input('Please a number:'))
print number


#Exercise 2-9
number = 0
for i in range(5):
	number += float(raw_input('Please enter a number:'))
print number/5


#Exercise 2-10
num = int(raw_input('Please enter a number:'))
if num>1 and num<100:
	print num
else:
	while num>100 or num<1:
		print "input error"
		num = int(raw_input('Please enter a number:'))
	print num

#Exercise 2-11
number=[]
total = 0
for i in range(5):
	num = int(raw_input('please enter number:'))
	number.append(num)
print '计算五数之和，请选择1:'
print '计算5数的平均值，请选择2:'
print '退出，请按3：'
choice_input = input()

if choice_input == 1:
	for i in number:
		total += i
	print '五数之和为：',total
elif choice_input == 2:
	for i in number:
		total += i
	print '五数的平均值为：',total/5
elif choice_input == 3:
	exit()
else:
	print "输入错误"


