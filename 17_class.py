class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == []:
            return 0
        else:
            digits_list = list(digits)
            ans = []
            nums = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mmo', 'pqrs', 'tuv', 'xyz']
            # while digits_list:
            a = nums[int(digits_list.pop(0))]
            a = list(a)

            c = list(a)
            while digits_list:
                b = nums[int(digits_list.pop(0))]
                b = list(b)
                # c = list(a)
                while b:
                    b1 = b[0]
                    while a:
                        ans.append(a.pop(0) + b1)
                    b.pop(0)
                    a = list(c)
                c = list(ans)
                a = ans
                ans = []
            return a

