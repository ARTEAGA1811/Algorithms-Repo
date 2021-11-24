def firstUniqChar(s: str) -> int:
    logs = set()
    for i in range(0,len(s)-1):
        if s[i] in logs:
            continue
        flag = False
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                logs.add(s[i])
                flag = True
                break
        if not flag:
            return i
    if s[-1] in logs:
        return -1
    return len(s)-1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
print(firstUniqChar('lllllllo'))