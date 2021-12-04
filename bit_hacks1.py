
def even(a):
    if(a & 1 !=0):
        print("odd")
    else:
        print("even")

def oppsig(a,b):
    if(a^b < 0):
        print("opposite")
    else:
        print("Not opposite")

def add1(a):
    print(-~a)


if __name__ == '__main__':
    a,b = map(int,input("").split(" "))
    even(a)
    oppsig(a,b)

    add1(a)
