from collections import deque
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def build_from_list(cls, vals):
        if not vals:
            return None

        root = cls(vals[0])
        queue = deque([root])
        idx = 1

        while queue and idx < len(vals):
            node = queue.popleft()
            if idx < len(vals):
                left_node = cls(vals[idx])
                node.left = left_node
                queue.append(left_node)
                idx += 1

            if idx < len(vals):
                right_node = cls(vals[idx])
                node.right = right_node
                queue.append(right_node)
                idx += 1

        return root

def serialize(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root


if __name__ == '__main__':
    vals = [3,1,5,None,None,4,6]
    root = TreeNode.build_from_list(vals)
    s = Solution()
    print(serialize(s.invertTree(root)))