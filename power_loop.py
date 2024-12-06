base = int(input("Enter the base num "))
exponent = int(input("Enter the exponent"))

ans = 1

for i in range(exponent):
    ans*= base

print(base,"rasied to the power",exponent,"is",ans)
