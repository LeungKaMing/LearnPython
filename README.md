# LearnPython
:)

## 遗忘点
1. 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为字典dict的key；
而list是可变的，就不能作为字典dict的key（因其内部是无序的）。
2. *args是可变参数，args接收的是一个元组tuple / 列表list；**kw是关键字参数，kw接收的是一个对象dict。前者传入后args就相当于tuple类型，后者传入后kw就相当于dict类型，各自方法都能调用了。