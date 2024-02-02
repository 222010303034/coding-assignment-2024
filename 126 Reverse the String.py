def reverseWords(self, s: str) -> str:
    x=s.split()
    return " ".join(x[::-1])
a=reverseWords("the sky is blue")
print(a)