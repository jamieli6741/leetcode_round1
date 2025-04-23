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

class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max(level))

        return result


if __name__ == '__main__':
    s = Solution()
    l = [3,9,20,None,None,15,7]
    tree = TreeNode.build_from_list(l)
    print(s.largestValues(tree))