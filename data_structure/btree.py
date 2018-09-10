# -*- coding: utf-8 -*-
# Author  : Super~Super
# FileName: btree.py
# Python  : python3.6
# Time    : 18-8-23 21:53

class Node(object):
    '''
    二叉树节点
    '''
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

def lookup(root):
    '''
    层次遍历
    '''
    row = [root]
    while row:
        print(row)
        row = [kid for item in row for kid in (item.left, item.right) if kid]

def deep(root):
    '''
    深度遍历
    '''
    if not root:
        return
    print(root.data)
    deep(root.left)
    deep(root.right)

if __name__ == '__main__':
    lookup(tree)
    deep(tree)

'''
前中后序遍历

深度遍历改变顺序就OK了
'''
#coding:utf-8
#二叉树的遍历
#简单的二叉树节点类
class Node(object):
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

def mid_travelsal(root):
    # 中序遍历:遍历左子树,访问当前节点,遍历右子树
    if root.left is not None:
        mid_travelsal(root.left)
    #访问当前节点
    print(root.value)
    if root.right is not None:
        mid_travelsal(root.right)

def pre_travelsal(root):
    # 前序遍历:访问当前节点,遍历左子树,遍历右子树
    print (root.value)
    if root.left is not None:
        pre_travelsal(root.left)
    if root.right is not None:
        pre_travelsal(root.right)

def post_trvelsal(root):
    # 后续遍历:遍历左子树,遍历右子树,访问当前节点
    if root.left is not None:
        post_trvelsal(root.left)
    if root.right is not None:
        post_trvelsal(root.right)
    print (root.value)

def maxDepth(root):
    # 求最大树深
        if not root:
            return 0
        return max(maxDepth(root.left), maxDepth(root.right)) + 1

def isSameTree(p, q):
    # 求两棵树是否相同
    if p == None and q == None:
        return True
    elif p and q :
        return p.value == q.value and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else :
        return False

def rebuild(pre, center):
    # 前序中序求后序
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur

def deep(root):
    if not root:
        return
    deep(root.left)
    deep(root.right)
    print(root.value)
