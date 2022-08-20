import re

if __name__=='__main__':
    x="IN KLU AT KLU"
    y= re.findall("KL",x)
    print(y)
    z=re.search("KLU",x)
    print(z)
    p=re.sub("K","9",x)
    print(p)
    u=re.split("U",x,2)
    print(u)