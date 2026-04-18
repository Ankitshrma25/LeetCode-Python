def rotatString(s, goal):
    k = 1
    n = 0
    while (n > len(s)):
        
        s = s[k:] + s[:k]
        n += 1

        if s != goal:
            rotatString(s, goal)
            return True
    return True
    
s = "abcde"
goal = "cdaeb"

result = rotatString(s, goal)
print(result)