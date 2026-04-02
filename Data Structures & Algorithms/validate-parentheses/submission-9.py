class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={")":"(","]":"[","}":"{"}
        for ch in s:
            if ch not in closetoopen:
                stack.append(ch)
            else:
                if stack and stack[-1]==closetoopen[ch]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False

        