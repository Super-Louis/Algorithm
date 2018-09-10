"""
BST(二分查找树Python实现)
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST():
    def __init__(self, data):
        self.root = Node(data[0])
        for d in data[1:]:
            self.insert(self.root, d)

    def insert(self, node, data):
        """从根节点开始插入"""
        if node == None: # 节点不存在，递归结束
            return Node(data)
        elif data < node.data:
            node.lchild = self.insert(node.lchild, data)
        elif data > node.data:
            node.rchild = self.insert(node.rchild, data)
        return node

    def search(self, node, data):
        """从根节点开始搜索
        :param node: current node
        :param data: data for search
        :return: True / False
        """
        if node is None: # 如果节点为None则说明树不存在，或所要寻找的数字不存在
            return False
        if node.data == data: # 找到了对应的数字
            return True
        elif data < node.data: # 小于当前节点则在当前节点的左子节点递归查找
            return self.search(node.lchild, data)
        else:
            return self.search(node.rchild, data)

    def findmin(self, node):
        """从根节点开始寻找最小值"""
        if node.lchild == None:
            return node.data
        else:
            return self.findmin(node.lchild)

    def findmax(self, node):
        if node.rchild == None:
            return node.data
        else:
            return self.findmax(node.rchild)

    def delete(self, node, data):
        """从根节点开始查找并删除
        1. 无左右节点直接删除
        2. 只有左节点/右节点，删除该节点，将其子节点作为当前节点
        3. 既有左，又有右节点，找出右子树最小值，作为当前节点的值，并删掉其右子树最小值
        """
        if node == None:
            return
        if data < node.data: # 小于当前节点，则对当前节点的左节点进行删除操作
            node.lchild = self.delete(node.lchild, data)
        elif data > node.data: # 大于当前节点，则对当前节点的右节点进行删除操作
            node.rchild = self.delete(node.rchild, data)
        else: # 等于当前节点，分三种情况
            if not (node.lchild or node.rchild): # condition 1
                node = None # 节点置为None
            elif node.lchild and node.rchild: # condition 3
                rmin = self.findmin(node.rchild)
                node.data = rmin
                node.rchild = self.delete(node.rchild, rmin)
            elif node.lchild: # condition 2.1
                node = node.lchild
            elif node.rchild:
                node = node.rchild
        return node

    def printTree(self, root):
        # 打印二叉搜索树(中序打印，有序数列)
        if root == None:
            return
        self.printTree(root.lchild)
        print(root.data, end=' ')
        self.printTree(root.rchild)

    def preOrderTraverse(self, node):
        # 前序遍历
        # 根节点 --> 左子树 --> 右子树
        if node is not None:
            print(node.data, end=' ')
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    def inOrderTraverse(self, node):
        # 中序遍历
        # 左子树 --> 根节点 --> 右子树
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print(node.data, end=' ')
            self.inOrderTraverse(node.rchild)

    def postOrderTraverse(self, node):
        # 后序遍历
        # 左子树 --> 右子树 --> 根节点
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.data, end=' ')

    def rowOrderTraverse(self, node):
        # 层次遍历，一般用队列实现(先进先出)
        if node == None:
            return
        queues = [node]
        while queues:
            n = queues[0]
            print(n.data, end=' ')
            queues.remove(n)
            if n.lchild:
                queues.append(n.lchild)
            if n.rchild:
                queues.append(n.rchild)

    def preOrderStack(self, node):
        # todo: 前序遍历堆栈实现(后进先出)
        # 根 --> 左 --> 右
        if node == None:
            return
        stacks = [node]
        while stacks:
            n = stacks.pop()
            print(n.data, end=' ')
            if n.rchild: # 先加右节点
                stacks.append(n.rchild)
            if n.lchild: # 再加左节点
                stacks.append(n.lchild)

    def inOrderStack(self, node):
        # todo: 中序遍历堆栈实现
        # 左 --> 根 --> 右
        if node == None:
            return
        stacks = []
        while node or stacks:
            while node:
                stacks.append(node)
                node = node.lchild # 一直遍历到最左节点
            n = stacks.pop()
            print(n.data, end= ' ')
            node = n.rchild


    def postOrderStack(self, node):
        # todo: 后序遍历堆栈实现
        # 右 --> 右 --> 根
        # todo:!!!
        pass


if __name__ == '__main__':
    bst = BST([3,1,7,4,6,5])
    # print(bst.search(bst.root, 4))
    # print(bst.findmin(bst.root))
    # print(bst.findmax(bst.root))
    # # bst.delete(bst.root, 4)
    # bst.printTree(bst.root)
    # print('\n')
    # bst.preOrderTraverse(bst.root)
    # print('\n')
    # bst.preOrderStack(bst.root)
    bst.inOrderTraverse(bst.root)
    print('\n')
    bst.inOrderStack(bst.root)
    # bst.postOrderTraverse(bst.root)
    # print('\n')
    # bst.rowOrderTraverse(bst.root)