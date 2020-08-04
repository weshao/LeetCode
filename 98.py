class Solution:
    def isValidBST(self, root) -> bool:

        def find2(root):
            if root:
                if root>1:
                    find2(root)
                    print(">1")
                else:
                    return


                return True
        a = find2(root)
        return a
i= Solution()
a=i.isValidBST(1)
print(a)