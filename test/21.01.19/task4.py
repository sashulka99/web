def twice(a,b):
    count=0
    for i in range(len(a)):
        if a[i]==b:
            #print(a[i])
            count+=1
    print("Cтолько раз в списке встречается ваш элемент: ",count)
x=[s for s in input().split()]
y=input("Введите какой элемент хотите проверить:")
twice(x,y)

