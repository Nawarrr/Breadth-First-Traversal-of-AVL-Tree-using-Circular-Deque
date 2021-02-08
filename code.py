#This Code is Impelementation for Circular QUEUE (Deque) and AVL Tree
#Then performing Breadth First Traversal of AVL Tree using Circular Deque

class CircularDeque:
    def __init__(self, capacity: int):
        """
        Initialize your data structure here.
        Set the maximum size of the deque to be capacity.
        """
        self.capacity = capacity
        self.deque = [None] * capacity
        self.rear = self.front = -1

    def insertRear(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.rear += 1
        self.rear = self.rear % self.capacity
        self.deque[self.rear] = value
        if self.rear == 0 and self.front < 0:
            self.front = 0
        return True

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front -= 1
        if self.front < 0: self.front = self.capacity - 1
        if self.rear < 0: self.rear = self.capacity - 1
        self.deque[self.front] = value
        return True

    def deleteRear(self) -> bool:
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear -= 1
        if self.rear < 0: self.rear = self.capacity - 1
        if self.rear == self.front - 1:
            self.rear = -1
            self.front = -1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front += 1
        self.front = self.front % self.capacity
        if (self.rear == self.front - 1) or (self.front == 0 and self.rear == self.capacity - 1):
            self.rear = -1
            self.front = -1
        return True

    def getRear(self):
        """
        Get the rear item from the deque.
        """
        if self.isEmpty():
            return None
        return self.deque[self.rear]

    def getFront(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return None
        return self.deque[self.front]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.front == - 1 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        rear = (self.rear + 1) % self.capacity  # a more delicate solution
        if rear == self.front:
            return True
        return False



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1


class AVLTree:
    def getHeight(self, root) -> object:
        """
        Return the height of root node
        """

        if not root: return 0
        return root.height

    def getBalance(self, root):
        """
        Check for root's balance
        """

        if not root: return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        """
        Get the node with lowest value (i.e., far left node)
        """

        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def insert(self, root, val):
        """
        Insert node with target value "val"
        """

        if not root:
            return TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)
        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)
        elif balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

        return root

    def delete(self, root, val):
        """
        Delete a node with target value "val"
        """

        if not root:
            return root
        elif val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                temp, root = root.right, None
                return temp
            elif root.right is None:
                temp, root = root.left, None
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        if root is None:
            return root

        balance = self.getBalance(root)
        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)
        elif balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        return root

    def rotateLeft(self, root):
        """
        Left rotate the root tree
        """

        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        new_root.height = 1 + max(self.getHeight(new_root.left),
                                  self.getHeight(new_root.right))
        return new_root

    def rotateRight(self, root):
        """
        Right rotate the root tree
        """

        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        new_root.height = 1 + max(self.getHeight(new_root.left),
                                  self.getHeight(new_root.right))
        return new_root  #

    # PLEASE NOTE THAT THIS IS A PART OF THE AVL CLASS
    def printLevelOrder(self, root):
        """
        Given root node, print the root tree level by level
        """

        h = self.getHeight(root)

        for i in range(1, h + 1):
            self.Level(root, i)
        l = 1
        while not dq.isEmpty():
            if dq.getRear() != l:
                l += 1
                dq.deleteRear()
                print()
            else:
                dq.deleteRear()
            print(dq.getRear(), end=" ")
            dq.deleteRear()
        print()

    def Level(self, root, level, k=1):
        if root is None:
            return
        elif level == 1:
            dq.insertFront(k)
            dq.insertFront(root.val)
        elif level > 1:
            k += 1
            self.Level(root.left, level - 1, k)
            self.Level(root.right, level - 1, k)


#myTree = AVLTree()
#root = None
#nums = [33, 13, 52, 9, 21, 61, 8, 11]

#for num in nums:
#    root = myTree.insert(root, num)

#dq = CircularDeque((2**myTree.getHeight(root))*2)

#myTree.printLevelOrder(root)
#myTree.delete(root, 13)
#myTree.printLevelOrder(root)