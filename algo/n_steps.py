# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: n_steps.py
# Python  : python3.6
# Time    : 18-8-20 23:43

'''
跳台阶问题：
一共有n级台阶，青蛙一次可以跳1级或两级，请问一共有多少种跳法？
设该函数为f, n级台阶共有f(n)种方法；
假设最后跳了一级，则前面共有f(n-1)种方法；
假设最后跳了2级，则共有f(n-2)中方法；
显然f(n) = f(n-1) + f(n-2)（斐波那契函数）
因此可用递归或循环来求解
'''

def recur_fib(n):
    if n == 1 or n == 2: # n=1/2时分别有1/2中方法
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)

def for_fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        print(b)
    return b

'''
变态跳台阶
一次可以跳1~n阶，共有多少种跳法？
递推法
第一次跳1阶，共有f(n-1)种跳法
第一次跳2阶，有f(n-2)种跳法
...
第一次跳n阶，有f(n-n)种跳法（假设f(0)=1）
则f(n) = f(n-1) + f(n-2) + ... + f(0)
由f(n-1) = f(n-2) + f(n-3) + ... + f(0)
得f(n) = 2f(n-1)
'''
def mad_steps(n):
    if n == 1:
        return n
    else:
        return 2 * mad_steps(n-1)

def mad_steps_2(n):
    if n == 0:
        return
    return 2**(n-1)

if __name__ == '__main__':
    print(recur_fib(4))
    print(for_fib(4))