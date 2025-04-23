class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self): # 设置虚拟节点，初始化size值
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        current_node = self.dummy_head.next # 从实际上的第一个节点开始（索引=1）
        for i in range(index):  # 结束时实际的索引为1+index，正好为需要取名义上的第index个节点（因为索引0被dummy_head占了）
            current_node = current_node.next

        return current_node.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current_node = self.dummy_head
        while current_node.next:    # 直接用是否后面还有节点判断是否到了末端
            current_node = current_node.next

        current_node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return

        current_node = self.dummy_head  # 从实际索引为0的dummy_head开始
        for i in range(index):  # 添加索引的位置为实际上的index-1，就是题意要求的，加在index前
            current_node = current_node.next
        new_node = ListNode(val, current_node.next)
        current_node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        current_node = self.dummy_head
        for i in range(index):
            current_node = current_node.next

        current_node.next = current_node.next.next
        self.size -= 1

    def __str__(self):
        # 遍历链表并以列表形式返回
        result = []
        current = self.dummy_head.next
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result) if result else "Empty LinkedList"



# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(9)
print(obj)
obj.addAtHead(1)
print(obj)

obj.addAtTail(999)
print(obj)

obj.addAtIndex(1,2)
print(obj)

obj.deleteAtIndex(3)
print(obj)

param_1 = obj.get(2)
print(obj)

