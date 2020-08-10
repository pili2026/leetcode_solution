class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Recursive Solution
# class Solution:
#     def maxDepth(self, root) -> int:
#         if not root or root.val is None:
#             return 0
#
#         left_level = self.maxDepth(root.left) + 1
#         right_level = self.maxDepth(root.right) + 1
#
#         return max(left_level, right_level)

class Solution:
    def maxDepth(self, root: Node) -> int:
        queue = []
        max_depth = 0

        if not root:
            return 0
        queue.append(root)

        while queue:
            size = len(queue)
            print(size)
            while size:
                var = queue.pop(0)
                if var.left:
                    queue.append(var.left)
                if var.right:
                    queue.append(var.right)

                size -= 1
            max_depth += 1
        return max_depth


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)

s = Solution()
print(s.maxDepth(tree))
