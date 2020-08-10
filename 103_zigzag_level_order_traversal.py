class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Node):
        if not root:
            return []
        result = []
        node_level = 0
        queue = [root]

        while queue:
            node_level += 1
            level = []

            for i in range(0, len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if node_level % 2 == 0:
                result.append(level[::-1])
            else:
                result.append(level)
        return result

binary_tree = Solution()
tree_node = Node(1)
tree_node.left = Node(2)
tree_node.right = Node(3)
tree_node.left.left = Node(4)
tree_node.left.right = Node(5)
tree_node.right.left = Node(6)
tree_node.right.right = Node(7)

print(binary_tree.zigzagLevelOrder(tree_node))
