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
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0



        return depth


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode.build_from_list([1,None,2])
    print(s.maxDepth(tree))