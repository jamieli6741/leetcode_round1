class Solution:
    def div(self, x, y):
        return int(x/y) if x*y > 0 else -(abs(x) // abs(y))

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+' or item == '-' or item == '*' or item == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                if item == '+':
                    stack.append(num1 + num2)
                if item == '-':
                    stack.append(num2 - num1)
                if item == '*':
                    stack.append(num1 * num2)
                if item == '/':
                    stack.append(self.div(num2, num1))
            else:
                stack.append(int(item))

        result = stack.pop()
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["2","1","+","3","*"]))
