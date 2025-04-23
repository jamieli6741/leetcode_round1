from collections import deque
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def build_from_list(cls, l):
        if not l:
            return None

        root = cls(l[0])
        queue = deque([root])
        i = 1

        while queue and i < len(l):
            current = queue.popleft()

            if i < len(l) and l[i] is not None:
                current.left = cls(l[i])
                queue.append(current.left)
            i += 1

            if i < len(l) and l[i] is not None:
                current.right = cls(l[i])
                queue.append(current.right)
            i += 1

        return root



class Solution():
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        stack = [(root, False) if root else None]
        result = []

        while stack:
            node, visited = stack.pop()

            if visited:
                result.append(node.val)
                continue

            if node.right:
                stack.append((node.right, False))

            stack.append((node, True))

            if node.left:
                stack.append((node.left, False))

        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode.build_from_list([5,3,7,2,4,None, None])
    print(s.inorderTraversal(root))
