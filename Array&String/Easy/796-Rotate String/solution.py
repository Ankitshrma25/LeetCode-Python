class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s+s)
    
s = "abcde"
goal = "cdaeb"
RotateStringSolv = Solution()

result = RotateStringSolv.rotateString(s=s, goal=goal)


print(result)