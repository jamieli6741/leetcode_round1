from collections import deque

## solution 1: 2 deques
# class MyStack:
#     def __init__(self):
#         self.stack_in = deque()
#         self.stack_out = deque()
#     def push(self, x: int) -> None:
#         self.stack_in.append(x)
#
#     def pop(self) -> int:
#         if len(self.stack_in) == 0:
#             return None
#
#         for i in range(len(self.stack_in)-1):
#             self.stack_out.append(self.stack_in.popleft())
#
#         self.stack_in, self.stack_out = self.stack_out, self.stack_in
#         # 注意，这里需要交换stack_in和stack_out，保证stack_in始终为我们的唯一队列
#         return self.stack_out.popleft()
#
#     def top(self) -> int:
#         top_element = self.pop()
#         self.stack_in.append(top_element)
#         return top_element
#
#     def empty(self) -> bool:
#         return len(self.stack_in) == 0

## solution 2: 1 deque
class MyStack:
    def __init__(self):
        self.stack = deque()
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        # deque popleft出来的元素加到队尾去，这样省去了第二个deque
        if len(self.stack) == 0:
            return None

        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())

        return self.stack.popleft()

    def top(self) -> int:
        top_element = self.pop()
        self.stack.append(top_element)
        return top_element

    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()