#!/usr/bin/python
#-*- coding:UTF-8 -*
# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，【一个对象包含了数据和操作数据的函数】。
# 将Student作为一个类，这个类所生成的对象实例拥有name和score这两个属性，要打印一个学生的成绩必须创建出这个学生实例。

# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类；相当于js的Object。
class Student(object):
  # 初始化方法：在创建实例的时候，就把name，score等属性绑上去；
  def __init__(self):
    # 1. __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身；
    # 2. 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去；
    # 3. 和普通的函数相比，【在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self】，并且，调用时，不用传递该参数；
    # 4. 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    # self.name = name
    # self.score = score
    self.__name = 'guest'
    self.__score = 60
    
  # 类的方法：数据封装
  def print_text(self):
    print('我是父类：{0} is name, {1} is score.'.format(self.__name, self.__score))
    return {
      'name': self.__name,
      'score': self.__score
    }
  # 类的方法
  def get_grade(self):
    if self.__score >= 90:
      return 'A'
    elif self.__score >= 70:
      return 'B'
    else:
      return 'C'
  def set_grade(self, score):
    self.__score = score

s = Student()
s.print_text()
s_score = s.get_grade()
# 可以给类本身 和 实例本身 绑定任何数据，这点跟js是一样的
s.age = 26
print(s.age)
Student.demo = 'hi'
print(Student.demo)
# __前缀命名的变量为私有变量
# print(s.__score) # 'Student' object has no attribute '__score'
s.set_grade(80)
print(s.get_grade())

# 继承
class Leung(Student):
  # 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
  def print_text(self):
    print('我是子类')
  pass
l = Leung()
print(l.print_text())

# 多态
# 当我们定义一个class的时候，我们实际上就定义了一种数据类型，与list、tuple、num、str基本数据类型是一样的：
type1 = isinstance(l, Leung) # 实例是当前Leung数据类型
type2 = isinstance(l, Student) # 实例也是当前类的父类Student数据类型
type3 = isinstance(Leung, Student)
print('检查一个变量是否某个类型：', type1, type2, type3)

def run_twice(animal):
  animal.print_text()
  animal.print_text()
run_twice(s)
run_twice(l)