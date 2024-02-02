def addBinary(self, a: str, b: str) -> str:
    output = int(a,2) + int(b,2)
    return "{:b}".format(output)
a = "100"
b = "11"
print(addBinary(a,b))