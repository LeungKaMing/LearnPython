# LearnPython
:)

## 遗忘点
1. 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为字典dict的key；
而list是可变的，就不能作为字典dict的key（因其内部是无序的）。
2. *args是可变参数，args接收的是一个元组tuple / 列表list；**kw是关键字参数，kw接收的是一个对象dict。前者传入后args就相当于tuple类型，后者传入后kw就相当于dict类型，各自方法都能调用了。
3. isinstance(x, (int, float)) / isinstance(x, Iterable) 判断一个变量是否属于某个数据类型 / 判断一个变量是否可迭代
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