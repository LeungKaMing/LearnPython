#!/usr/bin/python
#-*- coding:UTF-8 -*
import os
import math
# 模块引入：可以简单看成从 什么地方 引入 什么模块
from collections import Iterable
from functools import reduce

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
    print('enumerate: ', key, value)
  # 得出结论是：凡是可迭代的对象，我们基本都不关心它的数据类型
  if isinstance(str, Iterable):
    print('{0}是可迭代的'.format(str))
  if isinstance(list, Iterable):
    print('{0}是可迭代的'.format(list))
  if isinstance(obj, Iterable):
    print('{0}是可迭代的'.format(obj))
elif userInput == 'list3':
  arr = []
  # 如何生成[1*1, 2*2, 3*3, 4*4...]的数组
  # 1)
  # for num in list(range(1, 11)):
  #   arr.append(num * num)
  # print(arr)
  # 2.1) 一行解决的优雅方式 => 可以理解成既然是写在数组里面的表达式就不需要list强制转换
  arr = [num*num for num in range(1, 11)]
  print(arr)
  # 2.2) 筛选出偶数
  arr2 = [num*num for num in list(range(1, 11)) if num % 2 == 0]
  print(arr2)
  # 3) 列出某个目录下的文件和目录
  arr3 = [d for d in os.listdir('./')]
  print(arr3)
  # 4) 同时遍历key和value => obj.items()
  obj = {'name': 'ljm', 'age': '26'}
  arr4 = [key + '=' + value for key, value in obj.items()]
  print(arr4)
  # 5) 将某个数组的字符串全部变成小写 => 调用字符串方法lower();将某个数组的字符串全部变成大写 => upper()
  arr5 = [num.lower() for num in ['Sa', 'Sa', 'Sa']]
  print(arr5)   
elif userInput == 'gene':
  # 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
  # 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。【它是一种算法！】
  # 思考：是否可以将机器学习也归为生成器的一种概念？
  list = [x for x in range(10)]
  print('通过列表生成式，简单生成一个1~10的数组：', list)
  gene = (x for x in range(5))
  print('通过生成的一个1~10数组创建生成器：', gene)
  # generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误 => 通过抛出StopIteration的错误，【可以知道生成器generator也是一个可迭代的对象！跟list，dict，str一样！】
  # print(next(gene))
  # print(next(gene))
  # print(next(gene))
  # print(next(gene))
  # print(next(gene))
  # print(next(gene))
  # 。。。太累赘了，所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
  collect = [x for x in gene]
  print('将列表生成式与生成器结合来输出：', collect)
  print('以下看看著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...')
  def fib(max):
    # 有点js解构赋值的味道
    index, a, b = 0, 0, 1
    while index < max:
      # 1) a = 0 <=【b = 1】 
      # 2) a = 1 <=【b = 1】 
      # 3) a = 1 <=【b = 2】 <--- 这里开始，任意一个数都可由前两个数相加得到
      # 4) a = 2 <=【b = 3】 
      # 5) a = 3 <=【b = 5】
      # 6) a = 5 <=【b = 8】
      print(b)
      a, b = b, a + b
      index = index + 1
    return 'bye'
  print('改造成生成器前，是一个普通函数：', fib(10))
  # 那么如何将上述函数转换为生成器generator呢？跟js又有交集了！
  # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个生成器generator。
  # 你也可以将yield理解为print
  def geneFib(max):
    # 有点js解构赋值的味道
    index, a, b = 0, 0, 1
    while index < max:
      # 1) a = 0 <=【b = 1】 
      # 2) a = 1 <=【b = 1】 
      # 3) a = 1 <=【b = 2】 <--- 这里开始，任意一个数都可由前两个数相加得到
      # 4) a = 2 <=【b = 3】 
      # 5) a = 3 <=【b = 5】
      # 6) a = 5 <=【b = 8】
      yield b
      a, b = b, a + b
      index = index + 1
    return 'bye'
  collect2 = [x for x in geneFib(10)]
  print('改造成生成器后，是一个可迭代的生成器函数：', collect2)
  # 函数是顺序执行，遇到return语句或者最后一行函数语句就直接返回，再次调用也会在return的位置返回；而变成generator的函数，每次调用next()后，遇到yield语句就直接返回，再次执行时从上次返回的yield语句处继续执行 => yield有等待并保存上次返回的作用，跟js一样
  def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
    return 'bye'
  o = odd()
  print('改造成带有多个yield的生成器后，证明yield带有“断点续传”的意味：')
  print(next(o))  # 1
  print(next(o))  # 3
  print(next(o))  # 5
elif userInput == 'tri':
  # 杨辉三角
  # 期待输出:
  # [1]
  # [1, 1]
  # [1, 2, 1]
  # [1, 3, 3, 1]
  # [1, 4, 6, 4, 1]
  # [1, 5, 10, 10, 5, 1]
  # [1, 6, 15, 20, 15, 6, 1]
  # [1, 7, 21, 35, 35, 21, 7, 1]
  # [1, 8, 28, 56, 70, 56, 28, 8, 1]
  # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
  # 每个数组的第一项和最后一项都是1
  # # 除第一次外，[1] + arr[0] + arr[1] + ... + [1]
  # [1] + arr[0] + arr[1] + [1] => [1, 1+1 , 1]
  # [1] + (arr[0] + arr[1]) + (arr[1] + arr[2]) + [1] => [1, 1+2, 2+1 , 1]
  # [1] + (arr[0] + arr[1]) + (arr[1] + arr[2]) + (arr[2] + arr[3]) + [1] => [1, 1+3, 3+3, 3+1 , 1]
  arr = [1]
  def tri():
    global arr
    while True:
      yield arr
      if len(arr) == 1:
        arr.append(1)
      else:
        temp = arr
        arr = [1]
        for num in list(range(len(temp))):
          if num > 0:
            arr.append(temp[num - 1] + temp[num])
        arr.append(1)
        if len(arr) == 10:
          break
    return arr
  # 执行生成器
  t = tri()
  for tItem in t:
    print(tItem)
elif userInput == 'tri2':
  arr = [1]
  def tri2():
    global arr
    while True:
      yield arr
      if len(arr) == 1:
        arr.append(1)
      else:
        m = [arr[num] + arr[num-1] for num in range(len(arr)) if num > 0]
        arr = [1] + m + [1] # 数组的一种写法：合并
        if len(arr) == 10:
          break
    return arr
  # 执行生成器
  t = tri2()
  for tItem in t:
    print(tItem)
elif userInput == 'hoc1-1':
  def demo(x, y, f):
    return f(x) + f(y)
  print(demo(1, 2, abs))
  
  # 内置函数map / reduce => 类似js的lodash写法
  def f(x):
    return x * x
  result = map(f, [1, 2, 3, 4, 5, 6])
  # <map object at 0x7f31b11d92e8> => 这是一个迭代器，可以通过next来遍历输出 / for...in...
  # 1. next每次调用迭代器
  # print(next(result)) # 1
  # print(next(result)) # 4
  # print(next(result)) # 9
  # 2. 遍历迭代器
  # for r in result:
  #   print(r)
  # 3. 强转换为list类型
  print('result: ', list(result))

  # reduce函数就是将一个list的前后两项都放在函数处理，常用来求乘积
  def f2(x, y):
    return x * y
  result2 = reduce(f2, [1, 2, 3, 4, 5, 6])
  print('result2: ', result2)

  # sum函数常用来求叠加
  result3 = sum([1, 2, 3, 4, 5, 6])
  print('result3: ', result3)

  # # map函数还可以用来遍历字符串 => '1', '3', '5'...
  def demo(str):
    # lambda代替，相当于匿名函数
    # def compare(x, y):
    #   return x * y
    # 字典
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
    # 遍历字符串的生成器
    gene = (s for s in str)
    # 只过滤在字典能找到的元素，并且将元素转换成整数
    # if dict.get(num)
    list = [int(num) for num in gene if num in dict]
    result = reduce(lambda x,y: x*y, list)
    return result
  print(demo('13579'))
elif userInput == 'hoc1-2':
  # 凡是这种对某个索引位置进行操作的场景，都要用到切片[1:2:3]
  # 切片回顾：第一个冒号前代表开始索引，第一个冒号后代表结束索引，第三个冒号代表每隔多少位取一次
  def normalize(name):
    return name[0].upper() + name[1:]
  L1 = ['adam', 'json', 'leung']
  L2 = list(map(normalize, L1))
  print(L2)

  L3 = reduce(lambda x,y: x*y, [1, 2, 3, 4, 5])
  print(L3)

  def str2float(s):
    if isinstance(s, str):
      return float(s)
  L4 = str2float('123.456')
  print(L4)
elif userInput == 'hoc2-1':
  # filter也是Python的内置函数，用于过滤数组
  # 传参方式跟map一样，和map不同的是，传入的函数将作用于每个元素，然后根据返回值是True还是False决定过滤元素与否，最后生成一个新的数组！
  # filter返回值<filter object at 0x7f7e9273bac8>，与map一样都是生成器Iterator => next()处理 / for...in...处理 / list()强制转换为list类型
  def odd(num):
    return num % 2 == 0
  L1 = filter(odd, list(range(10)))
  # print('偶数的有：', L1) # <filter object at 0x7f7e9273bac8>
  print('偶数的有：', list(L1))

  # strip也是python内置的内置函数，用于去除空白字符
  def notEmpty(s):
    # and 相当于js的&&, or 相当于js的||
    if isinstance(s, str):
      return s and s.strip()
  L2 = list(filter(notEmpty, ['A', ' ', 'C', None, 'D', '', 'E']))
  print('去除空白字符后为：', L2)
elif userInput == 'pure':
  # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
  # 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
  # 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
  # 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
  # 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
  # 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
  # 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
  # 不断筛下去，就可以得到所有的素数。
  def pure(arr):
    while True:
      yield arr
      first = arr[0]
      second = arr[1:]
      for num in second:
        arr = list(filter(lambda x: x % first != 0, arr))
      # 跳出死循环的条件
      if len(arr) == 1:
        print('arr长度为1: ', arr)
        break
  result = pure(list(range(2, 100)))
  for r in result:
    print(r)
elif userInput == 'repeat':
  def demo(num):
    num = str(num)
    arr = list(range(len(num))) # 由于数字类型是没法获取索引的，所以先将其强转为字符串类型，然后根据字符串的长度进行遍历
    count = 0
    for n in arr:
      # 第一位数字跟最后一位数字进行比较，第二位跟倒数第二位进行比较，以此类推
      if num[n] == num[-(n+1)]:
        count = count + 1
        if count == len(arr):
          return num
  # 你可以把filter换成map，就会知道filter是惰性计算，没有return结果的不会返回；而map则是没有return结果也会返回None
  print(list(filter(demo, list(range(30000)))))
elif userInput == 'hoc3-1':
  # sorted是Python内置函数，用于排序
  result = sorted([3, 1, 0, -2, 4, 0])
  print('排序：', result)
  # key指定的函数将作用于数组的每一个元素上，并根据key函数返回的结果进行排序
  result2 = sorted([3, 1, 0, -2, 4, 0], key=abs)
  print('按绝对值来排序：', result2)
  # str.lower是Python内置的转换小写的函数
  result3  = sorted(['Joe', 'JoM', 'AJoEE', 'EKK', 'bbA', ], key=str.lower)
  print('按绝对值来排序：', result3 )
  # 反向排序，需传入第三个参数reverse=True
  result4  = sorted(['Joe', 'JoM', 'AJoEE', 'EKK', 'bbA', ], key=str.upper, reverse=True)
  print('按绝对值来排序：', result4 )
elif userInput == 'hoc3-2':
  def demo(arr):
    return arr[0]
  def demo2(arr):
    return arr[1]
  result = sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=demo)
  result2 = sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=demo2, reverse=True)
  print('按姓名来排列：', result)
  print('按分数高到低来排列：', result2)
elif userInput == 'hoc4-1':
  # 传入一个数组，返回一个能够运算求和的函数 => 高阶函数hoc的体现
  def sum(*arr):
    def result():
      total = 0
      for item in arr: # 内部result函数调用外部sum的参数，体现出【闭包】
        total = total + item
      return total
    return result
  r = sum(1, 2, 3, 4, 5, 6) # <function sum.<locals>.result at 0x7f4473d252f0>
  # print(r)
  print(r())
  r1 = sum(1, 2, 3, 4, 5, 6)
  r2 = sum(1, 2, 3, 4, 5, 6)
  print(r1 == r2) # 虽然就算传参和结果都一样，但由于每次调用都会产生一个新的堆栈，所以互不相等
elif userInput == 'hoc4-2':
  def count():
    fs = []
    for num in list(range(1, 4)):
      def demo():
        return num * num
      fs.append(demo)
    return fs
  # 类似es6的数组解构
  f1, f2, f3 = count()
  print(f1()) # 9
  print(f2()) # 9
  print(f3()) # 9
  # 上述情况正是由于跟js一样，没有用let来做循环，而是用了var，导致遍历传入的参数是以最后一位数为准 => 改造成闭包
  # 返回函数时，不要引用任何循环变量 或者 后续会发生变化的变量！
  def count2():
    def wraper(i):
      # def demo():
      #   return i * i
      # 用下面匿名函数实现
      return lambda: i*i
    fs = []
    for num in list(range(1, 4)):
      fs.append(wraper(num)) # 可以看出这里是跟上面写法不同的地方：用一个包装函数把循环变量存起来，再让返回函数使用，这样就保证了参数不会变！
    return fs
  f1, f2, f3 = count2()
  print(f1()) # 1
  print(f2()) # 4
  print(f3()) # 9
elif userInput == 'hoc4-3':
  # 需求：每次调用都返回递增函数 
  # => 生成器
  # def makeCounter():
  #   sum = 1
  #   while True:
  #     yield sum
  #     sum = sum + 1
  #     if (sum == 10):
  #       break
  # r = makeCounter()
  # print(next(r))
  # print(next(r))
  # print([x for x in makeCounter()])

  # => 闭包hoc
  # arr.append(demo(x)) => 这样就只会立马执行，并不满足我们的延迟执行，返回闭包函数的初衷
  # arr.append(wraper(x)), def wraper(x): def demo: return x return demo => 为了延迟执行并且带参，必须要有包装函数进行中间传递 
  def makeCounter2():
    arr = []
    for x in list(range(1, 4)):
      def wraper(x):
        def demo():
          return x
        return demo
      arr.append(wraper(x))
    return arr
  f1, f2, f3 = makeCounter2()
  print(f1()) # 1
  print(f2()) # 2
  print(f3()) # 3
elif userInput == 'anoymous':
  # 1. 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
  # 2. 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
  result = map(lambda x: x*x, [1, 2, 3, 4, 5, 6])
  print(list(result))
  
  result2 = lambda x: x
  print(result2(6))
  
  def anoymous():
    arr = []
    for num in list(range(1, 4)):
      def demo():
        return lambda num: 2 + num * num
      arr.append(demo())
    return arr
  result3 = anoymous()
  r1, r2, r3 = result3
  print(r1(1)) # 3
  print(r2(2)) # 6
  print(r3(3)) # 11
elif userInput == '@':
  # 函数对象有一个公共属性__name__，用于获取当前函数名字 => func.__name__
  # “装饰器”（Decorator）：在代码运行期间动态增加功能的方式。 => 本质上就是一个返回函数的hoc高阶函数
  # 1. 装饰器不带参
  def log(func):
    def wraper(*args, **kw):
      # wraper正是装饰器的核心部分 <<<<<<<<<<<<<<<<<<<
      # *args - 列表/元组；**kw - 对象
      print('函数名是：{0}'.format(func.__name__))
      print('参数是：', args, kw) # (1, 2, 3) {'age': 26, 'name': 'leung'}
      return func(*args, **kw) # 强制转换为可选参数 和 关键参数原封不动丢回去
    return wraper

  # 相当于now = log(now)，现在的now就不是返回原来内容了，而是返回装饰器返回的内容
  @log
  def now(*args, **kw):
    return {
      'arr': [num for num in args],
      'dict': kw
    }
  r = now(1, 2, 3, **{'name': 'leung'}, age=26) # review：第一个可选参数 => 可通过*[] / *() 将列表/元组强制转换 / 以相应格式传入1, 2, 3...；第二个关键参数 => 可通过**{} 将对象强制转换 / 以相应格式传入name='leung', age='25'
  print('log装饰器处理后的now函数结果为：', r)

  # 2. 装饰器带参
  def log2(text):
    def decorator(func):
      def wrapper(*args):
        print('传入的函数名：', func.__name__)
        print('装饰器传入的参数：', text)
        return func(args)
      return wrapper
    return decorator
  
  # 相当于now2 = log2('hello world')(now2)
  @log2('hello world')
  def now2(arr):
    arr = [num * num for num in arr]
    return list(arr)
  print(now2(1, 2, 3, 4, 5), '<<<<<<<<<<3')
elif userInput == 'likeFunc':
  import functools
  # 用法：functools.partial(系统内置函数 / 自定义函数, 第一个传入前面函数的参数【外面调用的时候再传入参数，则要求前面的函数必须要是 默认参数*args】)
  int2 = functools.partial(int, base=2)
  print('int类型转换：', int2('1000000'))

  def demo(num):
    return num
  demo = functools.partial(demo, 10)
  print('传入单个参数：', demo())

  def demo2(*list):
    return [num for num in list]
  demo2 = functools.partial(demo2, 10)
  print('传入多个参数作为默认参数：', demo2(3, 4, 5, 6))
elif userInput == 'ta':
  def move(n, a, b, c):
    if n==1:
      print(a,'-->',c, '其他参数是:',b) # 假设只有一个圆盘的情况，直接就是从a到c
    else:
      # 多个圆盘的情况下，将所有圆盘拆分成第一个圆盘和其他圆盘
      move(n-1,a,c,b)  #首先需要把 (N-1) 个圆盘移动到 b
      move(1,a,b,c)    #将a的最后一个圆盘移动到c
      move(n-1,b,a,c)  #再将b的(N-1)个圆盘移动到c
  move(3, 'A', 'B', 'C')
else:
  import sys
  print(sys.path)
  print('尊敬的用户您好，您所输入的{0}并不匹配条件，输入字符串的长度为{1}'.format(userInput, len(userInput)))