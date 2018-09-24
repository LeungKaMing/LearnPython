#!/usr/bin/python
#-*- coding:UTF-8 -*
# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，【一个对象包含了数据和操作数据的函数】。
# 将Student作为一个对象，这个对象拥有name和score这两个属性，要打印一个学生的成绩必须创建出这个学生实例。
class Student(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score
  def print_score(self):
    print('{0} is name, {1} is score.'.format(self.name, self.score))

leung = Student('LeungKaming', 100)
leung.print_score()