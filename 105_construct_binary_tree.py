class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def build_tree_recursive(self, preorder: list, inorder: list):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.build_tree_recursive(preorder, inorder[0:ind])
            root.right = self.build_tree_recursive(preorder, inorder[ind+1:])
            return root.val
        return None

    def build_tree_iteration(self, preorder: list, inorder: list):
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        stack = [(root, preorder, inorder)]
        while stack:
            args = stack.pop()
            node, preorder, inorder = args[0], args[1], args[2]
            if len(preorder) == 0:
                continue
            root_idx = inorder.index(preorder[0])

            if root_idx > 0:  # There's a left subtree
                node.left = TreeNode(preorder[1])
                stack.append((node.left, preorder[1: root_idx + 1], inorder[: root_idx]))
            if root_idx < len(inorder) - 1:  # There's a right subtree
                node.right = TreeNode(preorder[root_idx + 1])
                stack.append((node.right, preorder[root_idx + 1:], inorder[root_idx + 1:]))

        return root


s = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# print(s.build_tree_recursive(preorder, inorder))
print(s.build_tree_iteration(preorder, inorder))
