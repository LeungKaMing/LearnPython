#!/usr/bin/python
#-*- coding:UTF-8 -*
userInput = input('请输入：')
if userInput == 'admin':
  print('欢迎您，管理员！')
elif userInput == 'ljm':
  print('欢迎您，' + userInput)
elif userInput == 'cal':
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
  print('Now the line becomes: ', list)
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
    # 先最多录入5个人的信息
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
  print('Ur addrbook becomes this: ', addrList)
else:
  print('尊敬的用户您好，您所输入的{0}并不匹配条件，输入字符串的长度为{1}'.format(userInput, len(userInput)))