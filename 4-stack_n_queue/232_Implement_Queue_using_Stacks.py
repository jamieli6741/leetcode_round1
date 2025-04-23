class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        res = self.pop()    # 注意：调用pop会移除顶部元素
        self.stack_out.append(res)  # 需要把已经移除的元素加回去，因为peek操作不移除，只是查询
        return res

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)    # 注意这里是or，只要输入和输出栈里任何一个不为空，就不是empty queue

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()