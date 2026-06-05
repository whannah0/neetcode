class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        stack = []
        match = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                #stack is empty or 
                if not stack or stack[-1] != match[char]:
                    return False
                stack.pop()

        return len(stack) == 0