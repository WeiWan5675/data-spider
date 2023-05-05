#!/usr/bin/env python        可以让这个py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-      使用标准UTF-8编码；

' a test module '            #表示模块的文档注释

__author__ = 'Michael Liao'  #作者名

import sys                   #导入其他模块
import io as StringIO #导入其他模块，并使用as命名别名

def test():
    print('run')
    return True

'''
当我们在命令行运行模块文件时，Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
最常见的就是运行测试。
'''
if __name__=='__main__':
    test()