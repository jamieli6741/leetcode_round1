from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while i < len(lst):
        current = queue.popleft()
        if current:
            # 构造左子节点
            if i < len(lst) and lst[i] is not None:
                current.left = TreeNode(lst[i])
                queue.append(current.left)
            i += 1

            # 构造右子节点
            if i < len(lst) and lst[i] is not None:
                current.right = TreeNode(lst[i])
                queue.append(current.right)
            i += 1

    return root

class Solution:
    def inorderTraversal(self, root):
        values = []
        stack = [(root, False) if root else []]

        while stack:
            node, visited = stack.pop()
            if visited:
                values.append(node.val)
                continue

            if node.right:
                stack.append((node.right, False))

            stack.append((node, True))

            if node.left:
                stack.append((node.left, False))

        return values


if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    root = build_tree_from_list(lst)
    sol = Solution()
    print(sol.inorderTraversal(root))

