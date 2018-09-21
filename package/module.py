#!/usr/bin/python
#-*- coding:UTF-8 -*
# module模块 => package.module模块
import sys
__author__ = 'Leung' # 特殊变量，我们自己的变量一般不要用这种变量名
def hello():
    # argv变量：用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args = sys.argv
    if len(args) == 1:
        print('hello world.')
    else:
        arr = [num for num in args[1:]]
        print(arr, __name__)
if __name__ == '__main__':
    # 总结一下：
    # 如果我们是直接执行某个.py文件的时候，该文件中那么”__name__ == '__main__'“是True,但是我们如果从另外一个.py文件通过import导入该文件的时候，这时__name__的值就是我们这个py文件的名字而不是__main__；
    # 这个功能还有一个用处：调试代码的时候，在”if __name__ == '__main__'“中加入一些我们的调试代码，我们可以让外部模块调用的时候不执行我们的调试代码，但是如果我们想排查问题的时候，直接执行该模块文件，调试代码能够正常运行。
    hello()