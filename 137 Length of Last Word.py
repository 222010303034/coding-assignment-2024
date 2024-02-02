def lengthOfLastWord(self, s: str) -> int:
    l = s.split()
    return len(l.pop())

s="hello world"
print(lengthOfLastWord(s))