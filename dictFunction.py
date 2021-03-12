def dict(**n):
    lst=[]
    lst1 = []
    for x,y in n.items():
        lst.append(x)
        lst1.append(y)
    for i in range(3):
        print(f"You {lst[i]} is {lst1[i]}")
dict(name="Caaqil",Age=21,countery="Somalia")



