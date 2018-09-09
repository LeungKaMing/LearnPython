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