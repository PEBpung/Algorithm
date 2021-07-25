class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[': ']', '{':'}'}

        for i in range(len(s)):
            if s[i] in brackets.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                b = stack.pop()
                if not brackets[b] is s[i]:
                    return False
        if stack:
            return False
        return True