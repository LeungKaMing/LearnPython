#!/usr/bin/python
#-*- coding:UTF-8 -*
import math
# 模块引入：可以简单看成从 什么地方 引入 什么模块
from collections import Iterable

def my_abs (x):
  if not isinstance(x, (int, float)):
    raise TypeError('您输入的数据类型不符合整型和浮点型，请重新输入')
  if x > 0:
    print(x)
  elif x < 0:
    x = abs(x)
    print(x)
  else:
    # 还没想好要做什么，先留个占位符
    pass
  return x

def move (x, y, step, angle=0):
  nx = x + step * math.cos(angle)
  ny = y - step * math.sin(angle)
  return nx, ny

def changeable (*num):
  # 可变参数就是传入的参数个数不定。
  # 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，【参数num就会被强制转成tuple类型】，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数。
  sum = 0
  for item in num:
    sum = sum + item * item
  return sum

def key (name, age, **key):
  if 'city' in key:
    pass
  if 'job' in key:
    pass
  print('My name is {0}, my age is {1}, other is {2}'.format(name, age, key))
  return None
def key2 (name, age, *, city):
  print('My name is {0}, my age is {1}, other is {2}'.format(name, age, city))

def feedback (n):
  if n == 1:
    return 1
  return n * feedback(n-1)

userInput = input('请输入：')
if userInput == 'admin':
  print('欢迎您，管理员！')
elif userInput == 'changeable':
  print(changeable(1, 2, 3))
  # *nums表示把nums这个list的所有元素作为可变参数传进去。
  # Python允许你用已经存在的list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
  list = [1, 3, 5]
  tuple = (2, 4, 6)
  print(changeable(*list))
  print(changeable(*tuple))
elif userInput == 'key':
  print(key('ljm', 12, city='gx', province='gd'))
  dict = {
    'city': 'gz',
    'province': 'gd'
  }
  print(key('ljm', 26, **dict))
elif userInput == 'key2':
  # 命名关键字参数：*后的名字是要传入的，输入的不是*后跟的参数名，直接报错
  print(key2('leung', 23, province='gd', hobby='coding', city='gx'))
elif userInput == 'feedback':
  print(feedback(3))
elif userInput == 'cal':
  # int()函数 能把字符串类型转换成数字类型
  x = input('请输入第一位操作数：')
  y = input('请输入第二位操作数：')
  method = input('请输入运算法则：')
  if method == '+':
    sum = int(x) + int(y)
  elif method == '-':
    sum = int(x) - int(y)
  elif method == '*':
    sum = int(x) * int(y)
  elif method == '/':
    sum = int(x) / int(y)
  elif method == '%':
    sum = int(x) % int(y)
  print('sum: ', sum)
elif userInput == 'list':
  list = ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
  print('Jack' in list, '<<<<<<<<<<')
  list.append('Skr')
  bobIndex = 2
  nameInput = input('Enter ur name, then u will line up before Bob...')
  list.insert(bobIndex, nameInput)
  print('Now the line becomes: ', list)
  print('Everybody hates Adam，so I will delete him from the list')
  list.pop()
  print('Now the line becomes: ', list)
  print('I hate Bob I will delete him from the list')
  list.remove('Bob')
  print('Now the line becomes: ', list, ' and its length becomes: ', len(list))
  list.sort()
  print('Gonna sort the line：', list)
elif userInput == 'list2':
  # 从索引0开始取，直到索引3为止，但不包括索引3。
  list = list(range(100))
  tuple = tuple(range(100))
  str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  print('切片取数组前三项', list[0:3])
  print('切片取数组后三项', list[-3:])
  print('切片从第10个数开始，每隔2个数取一项', list[50::2])
  print('切片复制一个列表', list[:])
  print('tuple也是list的一种，虽然它是不可变的，但是是允许切片操作，结果仍是tuple', tuple[::5])
  print('字符串也可以看成是list的一种，每个元素就是一个字符，也是是允许切片操作，结果仍是字符串', str[::5])
elif userInput == 'tuple':
  tuple = (['javascript', 'nodejs'], 'python')
  print('Now u have this tuple: ', tuple)
  print('U can still change js stuff, but u can not change tuple\'s length')
  tuple[0][1] = ''
  print('Then tuple becomes: ', tuple)
elif userInput == 'addrbook':
  addrList = []
  userName = input('U can enter ur name：')
  userAge = input('U can enter ur age：')
  userAddr = input('U can enter ur addr：')
  userTel = input('U can enter ur tel：')
  addrList.append({
    'userName': userName,
    'userAge': userAge,
    'userAddr': userAddr,
    'userTel': userTel
  })
  count = 1
  while count <= 2:
    # 先最多录入2个人的信息
    userName = input('U can enter ur name in {0} time：'.format(count + 1))
    userAge = input('U can enter ur age in {0} time：'.format(count + 1))
    userAddr = input('U can enter ur addr in {0} time：'.format(count + 1))
    userTel = input('U can enter ur tel in {0} time：'.format(count + 1))
    addrList.append({
      'userName': userInput,
      'userAge': userAge,
      'userAddr': userAddr,
      'userTel': userTel
    })
    count = count + 1
  print('Ur addrbook becomes this: ', addrList, ' and its length becomes: ', len(addrList))
elif userInput == '1to100':
  # range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
  # list()函数 能把序列转换成列表类型
  sum = 0
  total = list(range(100))
  for item in total:
    sum = sum + item
  print('由1加到100,得出的总数为：{0}'.format(sum))
elif userInput == 'odds':
  # continue 可以提前结束本次循环，开始下一个循环
  # break 跳出循环
  sum = 0
  while sum < 12:
    if sum == 10:
      break
    if sum % 2 != 0:
      sum = sum + 1
      continue
    print('0到10，偶数的有：{0}'.format(sum))
    sum = sum + 1
elif userInput == 'evens':
  sum = 0
  while sum < 11:
    if sum == 9:
      break
    if sum % 2 != 1:
      sum = sum + 1
      continue
    print('0到10，奇数的有：{0}'.format(sum))
    sum = sum + 1
elif userInput == 'dict':
  # 字典没有顺序可言
  dict = {
    'Jacob': '90',
    'Leung': '100'
  }
  name1 = input('Jacob or Leung, who\'s ur favorite?')
  result1 = name1 in dict
  print('通过x in dict来判断该x是否是字典的key', result1)
  name2 = input('Jacob or Leung, who\'s ur favorite?')
  result2 = dict.get(name2, 'undefined user')
  print('通过dict.get来判断该x是否是字典的key，为None则输出第二个参数默认值', result2)
  condition = input('everybody hates Jacob?')
  if condition == 'yes':
    dict.pop('Jacob')
    print('Jacob is gone now: ', dict)
elif userInput == 'set':
  # set集合里面是不存在重复项的，所以可以将list借set()方法来做去重
  # 将去重后的list用list()方法强转回来，就实现了一次数组去重
  set1 = set([1,1,3,4,7,7])
  # 可以重复添加元素，但不会有效果，因为set本身就会去重
  set1.add(8)
  set1.remove(1)
  print('Now set becomes: ', set1, ' and now becomes list: ', list(set1))
  # 由于set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
  set2 = set([2, 3, 4])
  set3 = set([2, 3, 4, 10])
  print('交集为：', set2 & set3)
  print('并集为：', set2 | set3)
elif userInput == 'str':
  str = 'Tracy'
  temp = str.replace('T', 't')
  print('Gonna replace from Tracy to Skr2：', temp, ', but the origin str still not change：', str, '原因是：字符串是不可变对象。')
elif userInput == 'sys':
  print('用于计算绝对值的系统方法：', abs(-11))
  print('用于计算最小值的系统方法：', min(1, 3, 5))
  print('用于计算最大值的系统方法：', max([2, 4, 6]))
elif userInput == 'type':
  # 数据类型转换
  print('将字符串123强转为int类型:', int('123'))
  print('将字符串123强转为float类型:', float('123'))
  print('将浮点型123强转为字符串类型:', str('123.123'))
  print('将整型123强转为布尔类型:', bool(123))
elif userInput == 'def':
  # math.sqrt(2) 还有诸如类似这种方法计算平方根
  my_abs('123')
elif userInput == 'move':
  x, y = move(100, 100, 60, math.pi/6)
  print('可以有类似js的es6解构赋值一样：', x, y)
  print('实际上这个方法返回的是什么呢？', move(100, 100, 60, math.pi/6), ' ,Python的函数返回多值其实就是返回一个tuple数据类型！')
elif userInput == 'for':
  # 数组、对象皆迭代
  obj = {'name': 'leung', 'age': 26}
  list = ['javascript', 'nodejs', 'python']
  tuple = ['js', 'nj', 'py']
  for key in list:
    print(key, 'I am from list')
  for key in tuple:
    print(key, 'I am from tuple')
  for item in obj:
    print('key: {0} and value: {1}'.format(item, obj[item]))
  # for key in obj.keys():
  #   print('key from obj: {0}'.format(key))
  # for value in obj.values():
  #   print('value from obj: {0}'.format(value))
  # for ob in obj.items():
  ## key和value同时变成tuple的一项，归到同一个tuple里 => ('age', 26)
  #   print(ob)
  str = 'ABCDEFG'
  for sItem in str:
    print(sItem, 'I am from str')
  # 能把列表list用key-value的形式分别输出：索引-值
  for key,value in enumerate(list):
    print(key, value)
  # 得出结论是：凡是可迭代的对象，我们基本都不关心它的数据类型
  if isinstance(str, Iterable):
    print('{0}是可迭代的'.format(str))
  if isinstance(list, Iterable):
    print('{0}是可迭代的'.format(list))
  if isinstance(obj, Iterable):
    print('{0}是可迭代的'.format(obj))
else:
  print('尊敬的用户您好，您所输入的{0}并不匹配条件，输入字符串的长度为{1}'.format(userInput, len(userInput)))