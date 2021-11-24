#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

def solucionar(s:str, t:str):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in t:
            indFound = t.find(s[i])
            t = t[:indFound]+t[indFound+1:]
        else:
            return False
    return True


