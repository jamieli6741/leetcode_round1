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


from collections import deque


class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            level_size = len(queue)
            depth += 1
            for _ in range(level_size):
                node = queue.popleft()

                if (not node.left) and (not node.right):
                    return depth

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return depth


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode.build_from_list([1,2,3,None,None,4])
    print(s.minDepth(tree))