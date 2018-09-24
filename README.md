# LearnPython
:)

## 遗忘点
1. 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为字典dict的key；
而list是可变的，就不能作为字典dict的key（因其内部是无序的）。
2. *args是可变参数，args接收的是一个元组tuple / 列表list；**kw是关键字参数，kw接收的是一个对象dict。前者传入后args就相当于tuple类型，后者传入后kw就相当于dict类型，各自方法都能调用了。
3. from collections import Iterable, isinstance(x, (int, float)) / isinstance(x, Iterable) 判断一个变量是否属于某个数据类型 / 判断一个变量是否可迭代
4. 对象方法
- 判断一个对象是否有该键名：key in obj
- 判断一个对象是否有该键名：obj.get(key)
- 快速迭代对象的键：obj.keys()
- 快速迭代对象的值：obj.values()
- 将对象的key-value转换成元组tuple：obj.items()
5. 内置方法
- enumerate 能把列表list用key-value的形式分别输出：索引-值
```
for key,value in enumerate(list):
  print(key, value)
```
- os
```
1. os.listdir(dirname) - 返回带有该dirname下的目录和文件名组成的列表
```
6. 列表生成式
```
# 注意这里的range(10)并不像普通循环 for item in list(range(10)) 写法一样需要进行强制转换类型
list = [x for item in range(10)] # 这就是一条简单的列表生成式
list2 = [x for item in range(10) if x % 2 === 0] # 这就是一条仅仅输出1-10范围内偶数的列表生成式
```
7. 生成器generator
> 无非就是把列表生成器外面的[]符号换成()，就是一个简单的生成器了。
```
# 1) 生成器最简单的一种形式 
list = [x for item in range(10)] # 这就是一条简单的列表生成式
gene = (x for item in range(10)) # 这就是一条简单的生成器
# 2) 调用
next(gene)
next(gene)
next(gene)
# ...太累赘了，所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
# 3) for循环怎么写
gene = (x for x in range(5))
print(gene)
# 4) 生成器高级的一种形式 => 将函数加yield改造
def odd():
  print('step 1')
  yield 1
  print('step 2')
  yield(3)
  print('step 3')
  yield(5)
  return 'bye'
g = odd() # 函数版本的生成器
next(g)
next(g)
next(g)
# 结论：函数是顺序执行，遇到return语句或者最后一行函数语句就直接返回，再次调用也会在return的位置返回；而变成generator的函数，每次调用next()后，遇到yield语句就直接返回，再次执行时从上次返回的yield语句处继续执行 => yield有等待并保存上次返回的作用，跟js一样
```
8. 迭代器
> 通过上述，我们可以知道，适用于for...in...循环的数据类型有以下几种：
- 集合数据集类型，如list、tuple、set、dict、str
- 生成器generator
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
```
from collections import Iterable
# 常用内置函数isinstance()判断一个对象是否为可迭代对象Iterable
>>> isinstance([], Iterable) # 数组
True
>>> isinstance({}, Iterable) # 对象
True
>>> isinstance('abc', Iterable) # 字符串
True
>>> isinstance([x for x in range(10)], Iterable) # 列表生成式
True
>>> isinstance((x for x in range(10)), Iterable) # 生成器
True
>>> isinstance(100, Iterable) # 数字类型并不是可迭代对象
False

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 1. 生成器可以被next()不断调用，所以生成器是一个Iterator迭代器；并且生成器也是一个可以被isinstance()判断出的可迭代对象。
# 2. 生成器既是Iterator迭代器，又是Iterable可迭代对象；list、dict、str虽然是Iterable可迭代对象，但却不是Iterator迭代器 => 简单来说，能被next()调用的，又能能被for...in...遍历肯定既是迭代器，又是可迭代对象；不能被next()调用，但能被for...in...遍历的只能是可迭代对象
# 3. 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
from collections import Iterator # 迭代器
isinstance(iter([]), Iterator)  # True
isinstance(iter({}), Iterator)  # True
isinstance(iter('abc'), Iterator)  # True

# 你可能会问，为什么list、dict、str等数据类型不是Iterator迭代器？
# 简单来说，因为Iterator迭代器可以看成是一个我们【不能知道长度】的有序序列，list, dict, str我们都可以通过肉眼能看出长度。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass

# 实际上完全等价于：

# 首先将 非迭代器对象 通过iter方法转换成 迭代器对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```
注意！搞清楚import Iterable 和 import Iterator 是两码事，一个是引入可迭代对象判断，一个是引入迭代器判断
9. 函数式编程
> 简单来说就是允许把函数本身作为参数传入，返回一个新的函数 => 高阶函数(HOC)，也就是我们常说的函数式编程
- 有个需要关注的点是，函数名也可以看成变量 => 内置计算绝对值的函数abs，可以看成是变量abs，值为一个匿名函数
```
def demo(x, y, f):
    return f(x) + f(y)

demo(1, 2, demo)
```
## 如何安装第三方模块
> 通过pip这个包管理工具完成的；python3.5对应的是pip3。
假设现在需要安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。
> 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow => 类似NodeJS包都在npmjs.com注册一样。
- 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
```
import sys
print(sys.path) # ['/media/leung/DATA/Python/LearnPython', '/usr/local/lib/python35.zip', '/usr/local/lib/python3.5', '/usr/local/lib/python3.5/plat-linux', '/usr/local/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/site-packages']
```