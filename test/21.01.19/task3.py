def pal(word):
    a=list(word)
    count=0
    print(a)
    for i in range(0,int(len(a)/2)):
        if a[i]==a[-i-1]:
            count+=1
        #print(count)
        #print(a[i])
        #print(a[-i-1])
    if count==(int(len(a)/2)):
        print("true")
    else:
        print("false")
pal(input())
