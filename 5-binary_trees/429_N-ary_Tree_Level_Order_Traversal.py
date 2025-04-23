from collections import deque
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    @classmethod
    def build_from_level_order(cls, data):
        if not data:
            return None

        root = cls(data[0])
        queue = deque([root])
        idx = 1

        while idx < len(data):
            if data[idx] is None:
                # start children nodes
                parent = queue.popleft()
                idx += 1
                children = []
                while idx < len(data) and data[idx] is not None:
                    child = cls(data[idx])
                    children.append(child)
                    queue.appendleft(child)
                    idx += 1
                parent.children = children
            else:
                idx += 1

        return root

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.children:
                    for child in node.children:
                        queue.append(child)
            result.append(level)

        return result



if __name__ == '__main__':
    s = Solution()
    level = [1,None,3,2,4,None,5,6]
    tree = Node.build_from_level_order(level)
    print(s.levelOrder(tree))
