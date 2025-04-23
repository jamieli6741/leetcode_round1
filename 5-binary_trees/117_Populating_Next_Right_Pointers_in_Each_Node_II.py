from collections import deque
# same solution as 116
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for _ in range(level_size):
                curr = queue.popleft()
                if prev:
                    prev.next = curr

                prev = curr

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        return root
