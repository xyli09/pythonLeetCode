print("{} {}".format("hello", "world")) # 不设置指定位置，按默认顺序



print("{0} {1}".format("hello", "world")) # 设置指定位置

print("{1} {0} {1}".format("hello", "world") )# 设置指定位置


#通过关键字

print("名字：{name}, 地址 {url}".format(name="python学习", url="https://www.python.org/"))

# 通过字典设置参数

site = {"name": "python学习", "url": "https://www.python.org/"}

print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数

my_list = ['python学习', 'https://www.python.org/']

print("网站名：{0[0]}, 地址 {0[1]}".format(my_list)) # "0" 是必须的

print('{:^14}'.format('python')) #居中对齐

print('{:>14}'.format('python')) #右对齐

print('{:<14}'.format('python')) #左对齐

print('{:*<14}'.format('python'))

print('{:&>14}'.format('python'))

print('{:.1f}'.format(4.234324525254))

print('{:.4f}'.format(4.1))

print('{:b}'.format(250))

print('{:o}'.format(250))

print('{:d}'.format(250))

print('{:x}'.format(250))

print('{:,}'.format(100000000))

print('{:,}'.format(235445.234235))


from collections import Iterable

print(isinstance('abc', Iterable) )# str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代

def calc(*numbers):

    sum = 0

    for n in numbers:

        sum = sum + n * n

    return sum