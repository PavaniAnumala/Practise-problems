
def feb(n,lookup):
    if(n<=1):
        return n
    if n not in lookup:

        lookup[n] = feb(n-1,lookup) + feb(n-2,lookup)
    return lookup[n]

if __name__ == '__main__':
    n = int(input(" "))
    lookup = {}
    print(feb(n,lookup))
