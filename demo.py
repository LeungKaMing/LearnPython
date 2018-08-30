#!/usr/bin/python
#-*- coding:UTF-8 -*
userInput = input('请输入：')
if userInput == 'admin':
  print('欢迎您，管理员！')
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
  if condition == True:
    dict.pop('Jacob')
    print('Jacob is gone now: ', dict)
elif userInput == 'set':
  # set集合里面是不存在重复项的，所以可以将list借set()方法来做去重
  # 将去重后的list用list()方法强转回来，就实现了一次数组去重
  set = set([1,1,3,4,7,7])
  print('Now set becomes: ', set, ' and now becomes list: ', list(set))
else:
  print('尊敬的用户您好，您所输入的{0}并不匹配条件，输入字符串的长度为{1}'.format(userInput, len(userInput)))