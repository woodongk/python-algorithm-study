class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        depth = 0
        level = [root] if root else []
        print(level, depth)

        # 몇 층인지 모르는 상태
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
                level = queue
        return depth