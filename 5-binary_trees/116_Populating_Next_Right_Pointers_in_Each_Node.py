from collections import deque
class TreeNode():
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @classmethod
    def build_from_list(cls, data):
        if not data:
            return None

        root = cls(data[0])
        queue = deque([root])
        idx = 1

        while queue and idx < len(data):
            node = queue.popleft()
            # left child
            if idx < len(data):
                left_node = cls(data[idx])
                node.left = left_node
                queue.append(left_node)
                idx += 1

            # right child
            if idx < len(data):
                right_node = cls(data[idx])
                node.right = right_node
                queue.append(right_node)
                idx += 1

        return root

    @staticmethod
    def serialize(root):
        """
        Traverse the tree using `next` pointers and serialize the structure
        into a list where '#' denotes end of each level.
        """
        result = []
        leftmost = root

        while leftmost:
            curr = leftmost
            leftmost = None
            while curr:
                result.append(curr.val)
                if not leftmost:
                    if curr.left:
                        leftmost = curr.left
                    elif curr.right:
                        leftmost = curr.right
                curr = curr.next
            result.append('#')

        return result


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return []

        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for _ in range(level_size):
                node = queue.popleft()
                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,4,5,6,7]
    tree = TreeNode.build_from_list(l)
    output = s.connect(tree)
    print(TreeNode.serialize(output))