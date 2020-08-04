class Solution:
    def isValid(self, s):
        a=[]
        for n in s:
            if n in ['(', '[', '{']:
                a.append(n)
            elif n == ')':
                if not a:
                    return False
                elif a.pop() != '(':
                    return False
            elif n == ']':
                if not a:
                    return False
                elif a.pop() != '[':
                    return False
            elif n == '}':
                if not a:
                    return False
                elif a.pop() != '{':
                    return False
            if len(a) > (len(s)/2):
                return False
        if a != []:
            return False
        else:
            return True 

i = Solution()
a = i.isValid("()")
print(a)