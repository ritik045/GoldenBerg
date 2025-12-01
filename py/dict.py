# x={10,20,30,40}
# y={10,20,50,60}
# print(x.union(y))
# print(x or y)

# x={10,20,30,40}
# print(10 in x)
# print(50 in x)

# x={10,20,30,40}
# y={10,20,50,60}
# print(x.intersection(y))
# print(x & y)

# d={}
# print(type(d))
# d[111]='aaa'
# d[222]='bbb'
# d[333]='ccc'
# print(d)
# print(d[111])
# print(d[222])

# wap to display the names and marks of a student

# d={}
# d['Shahrukh']=87
# d['Akshay']=83
# d['Salman']=89
# d['Kareena']=92
# print(d)


# input method

# d={}
# while True:
#     name=input('enter the name: ')
#     marks=int(input('enter marks: '))
#     d[name]=marks
#     option=input('would you like to insert more values: ')
#     if option.lower()=='no':
#         break
# print(d)



# updation

# d={111:'aaa', 222:'bbb'}
# d[444]='ddd'
# print(d)
# d[111]='ccc'
# print(d)



# d={111:'aaa', 222:'bbb', 333:'ccc'}
# print(len(d))
# print(d.get(111))
# print(d.get(444))
# print(d.get(444,'xxx'))
# print(d)


# d={111:'aaa', 222:'bbb', 333:'ccc'}
# print(d.pop(111))
# print(d)
# print(d.pop(444))
# print(d)


# def add(a,b):
#     return a+b

# sum=add(10,20)
# print(sum)

def add(a,b):
    print(a+b)

c=add(5,10)
print(c)