userInput = input('请输入：')
if userInput == 'admin':
  print('欢迎您，管理员！')
elif userInput == 'ljm':
  print('欢迎您，' + userInput)
elif userInput == 'cal':
  x = input('请输入第一位操作数：')
  y = input('请输入第二位操作数：')
  method = input('请输入运算法则：')
  sum = int(x) + int(y)
  print('x' + method + ' y = ' + str(sum))
else:
  print('kidding me?您输入的是：' + userInput + '字符串长度是：' + str(len(userInput)))