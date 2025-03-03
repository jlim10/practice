'''
    Python Programming
    Book Study
    Jaehwan Lim
'''

# #p49
# var = 'hi py'   # 주석
# print(var)

# var = 5; print(var)
# var = 12.3
# print(var)

# #p50
# print(7, type(7))
# print(7.2, type(7.2))
# print(3+4j, type(3+4j))
# print(True, type(True))

# print('abc', type('abc'))
# print([1], type[1])
# print((1,),type((1,)))
# print({1}, type({1}))
# print({'key':'value'}, type({'key':'value'}))

# print(10, oct(10), hex(10), bin(10))
# print(10, 0o12, 0xa, 0b1010)
# a='12'
# print(int(a,8))
# print(int(a,16)) 

# #p53
# v1= 3
# v1=v2=v3=5
# print(v1,v2,v3)

# v1, v2=10,20
# print(v1, v2)
# v2, v1=v1, v2
# print(v1, v2)

# v1, *v2 = 1,2,3,4,5
# print(v1)
# print(v2)

# *v1, v2 = 1,2,3,4,5
# print(v1)
# print(v2)

# *v1, v2, v3 = 1,2,3,4,5
# print(v1)
# print(v2)
# print(v3)

# v1, *v2, v3 = 1,2,3,4,5
# print(v1)
# print(v2)
# print(v3)

# #p54
# print(5+3,5-3)
# print(5*3,5/3)
# print(5//3,5%3)
# print(5**3)
# print("나누기에서 몫과 나머지 얻기", divmod(5,3))
# print('\n연산 우선순위:', 3+4*5, (3+4)*5)

# print(5>3,5==3,5!=3)
# print(5>3 and 4<3, 5>3 or 4<3, not(5>=3))

# a=10
# a=a+1
# a+=1
# print(a)

# print('한'+'국'+'만세')
# print('한국 '*3)
# print("\n부호변경: ", a*-1, -a, a)
# b=-10
# print(-b, +b)
# print(abs(b))

# #p55
# print('불린1:', bool('Hello'), bool(1), bool(-2), bool(3.2), bool(0),bool(-1))
# print('불린2: ',bool(0),bool(None),bool(''), bool(),bool([]),bool({}),bool(()))

# print(type(None))
# print(None==False,None==None)

# print('a\nb\tc\rd')
# print('aaaa\fbbbb\b\b')
# print('aaa\000bbb\n22')
# print('aa\\bb\'\"')

# print(r'a\nb\tc\rd')
# print(r'aaaa\fbbbb\b\b')
# print(r'aaa\000bbb\n22')
# print(r'aa\\bb\'\"')

# #p58
# a='Hello'
# a="안녕"
# print(a)

# b='Python'
# print(b[1])
# print(b[-1])

# # ss='대한민국'
# print(ss[0:1])
# print(ss[0:2])
# print(ss[1:2])

# print(ss[2:])
# print(ss[:2])
# print(ss[-2:-1])
# print(ss[-3:-1])
# print(ss[-2:1])
# print(ss[0:3:2])
# print(ss[:])
# print(ss[::-1])

# # p61
# a=' Hello Python '
# print(a.count('e'))
# print(a.find('e'))
# print(a.find('l'))
# print(a.rfind('l'))
# print(a.index('l'))
# print(a.rindex('l'))
# print(a.find('x'))
# print(a.rfind('x'))
# print(a.index('x')) #error 발생
# print('s'.join(a))
# print(a.join('ssss'))
# print(a.lower())
# print(a.upper())
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())
# print(a.replace('l','abc'))
# print(a.split('e'))
# print(a.split('l'))
# print(a.split(' '))
# print(a.swapcase())
# print(a.startswith('H'))
# print(a.startswith(' H'))
# print(a.startswith(' '))
# print(len(a))

# #p62
# s='sequence'
# print(len(s))
# print(s.count('e'))
# print(s.find('e'),s.find('e',5),s.rfind('e'),s.rfind('e',4)) #find 두번째 인자는 찾기 시작 index, rfind에서 두번째 인자는 의미 없음
# print(s.startswith('seq'), s.startswith('b'), s.startswith(s))
# print('e' in s)

# print(s[0],' ',s[7])
# print(s[1:], ' ', s[1::2])
# print(s[:3], ' ', s[3:])
# print(s[-1], ' ', s[-8])
# print(s[-4:], ' ', s[::3])
# print(s[1:7:1], ' ', s[1:7])

# print(id(s))
# s='fre'+s[2:]
# print(s)
# print(id(s))

# s1='kbs mbc'
# s1=' '+s1[:4]+'sbs '+s1[4:]+' '
# # print(s1, len(s1))
# # print(s1.strip(), len(s1.strip()))
# s2=s1.strip().split(sep=' ')
# print(s2)
# print('&'.join(s2))

# ss="대한민국 만세"
# print(ss.replace('대한민국', '파이썬'))

# a=(1,2,3,4,5)
# b=['a','b','c']
# c=[1,'a',2,'b']
# d=[1,2,3,4]
# e=('a','b')
# f={'a','b','c'}
# g={'key1':'a', 'key2':'b', 'key3':'c'}
# # print(''.join(a)) #a,b,d는 에러
# print(''.join(b))
# print(''.join(e))
# print(' '.join(e))
# print(' '.join(f)) #set이라 실행마다 순서가 바뀜
# print(' '.join(g)) #key로 string 생성됨

# mixed_list = [1, "hello", 3.14, "world", 42]
# print(" ".join([str(x) for x in mixed_list]))
# print(" ".join(map(str, mixed_list)))
# print(list(map(lambda x: str(x), mixed_list)))

# #p64
# a=[1,2,3]
# a.insert(0,0)
# print(a)
# a.insert(4,10)
# print(a)
# a.append(20)
# print(a)
# a.extend([5,6,7])
# print(a)
# a.extend('abc123')
# print(a)
# a+=[50,20]
# print(a)

# #p65
# a=[1,2,3]
# b=[10,a,20.5,True,'string']
# print(b)
# print(id(a),id(b))
# b.insert(3, 10)
# print(b)
# b.remove(10)
# print(b)
# b.append(10)
# print(b)
# b.extend(['aa','bb'])
# print(b)
# b+=['p','l']
# print(b)
# print(b.index(True))
# print(b.index(10,3))
# print([1,2,3] in b)
# print('p' in b)
# print('x' in b)
# print([1,2] in b)


# #p66
# x=[1,2,3]
# y=['a','b','c']
# # x.append(y)
# x.extend(y)
# print(x)

# aa=[1,2,3,4,5]
# print(aa[0:2])

# aa=[1,2,3,['a','b','c','b','c'],4,5]
# aa[0]=100
# aa[3][0]='good'
# print(aa)
# print(aa[0],aa[3])
# print(aa[3][:2])
# print(aa[3][2])

# aa.remove(4)
# del aa[4]
# print(aa)
# aa[3].remove('c')
# del aa[3][0]
# print(aa)

# #p67
# aa= [3,1,5,2,4]
# aa.sort()
# print(aa)
# aa.sort(reverse=True)˜
# print(aa)

# aa2=['123', '34', '234', '151', '13']
# aa2.sort()
# print(aa2)
# aa2.sort(key=int)
# print(aa2)

# aa2= [3,1,2]
# aa3=sorted(aa2)
# print(aa3)

# #p68
# var1=[10,20,30]
# var2=[2,3]
# print(var1+var2)
# print(var1*2)

# name1=['Tom', 'John']
# name2 = name1
# print(name1, id(name1))
# print(name2, id(name2))
# name1[0]='Jay'
# print(name1)
# print(name2)

# import copy
# name3=copy.deepcopy(name1)
# name1[0]='Paul'
# print(name1, id(name1))
# print(name2, id(name2))
# print(name3, id(name3))

# #p69
# print('Process stack(LIFO) in list')
# sbs=[10,20,30]
# sbs.append(40)
# print(sbs)
# print(sbs.pop())
# print(sbs)
# print(sbs.pop())
# print(sbs)

# print('Process queue(FIFO) in list')
# sbs=[10,20,30]
# sbs.append(40)
# print(sbs.pop(0))
# print(sbs)
# print(sbs.pop(0))
# print(sbs)

# from collections import deque
# d = deque([1,2,3,4,5])
# print(d.popleft())
# print(d)
# print(d.pop())
# print(d)
# d.appendleft(10)
# print(d)
# d.append(20)
# print(d)

# from queue import Queue
# q = Queue(3)
# # for item in [1,2,3,4,5]:
# #     q.put(item)
# print(q.put(10))
# print(q.put(20))
# print(q.put(30))
# print(q.get())
# print(q.put(40))
# q.put(50)

# #p71
# t=('a','b','c','a')
# print(t)

# print(len(t))
# print(t.count('a'))
# print(t.index('b'))

# p=(1,2,3)
# q=list(p)
# print(q)
# q[1]=10
# p=tuple(q)
# print(p,q)
# print(p[1:])

# t1=(10,20)
# a,b=t1
# print(t1, id(t1))
# b,a=a,b
# t1=a,b
# print(t1, id(t1))

# #p72
# a={1,2,3,1}
# print(a)
# print(len(a))
# b={3,4}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# print(a|b)
# print(a&b)
# print(a-b)
# print(b-a)

# b.add(5)
# print(b)

# b.update({6,7})
# print(b)
# b.update([8,9])
# b.update((10,11))
# print(b)

# b.discard(2)
# b.remove(6)
# print(b)

# a={1,2,3,1}
# print(a)
# print(tuple(a))
# print(list(a))

# li=[1,2,2,3,1]
# print(set(li))
# print(a==set(li))

# #p74
# mydic=dict(k1=1,k2='abc',k3=3.4)
# print(mydic)

# coffee={'mocha':'moch', 'latte':'late'}
# print(coffee)
# print(len(coffee))
# print(coffee['mocha'])

# print(coffee.keys())
# print(coffee.values())
# print(coffee.items())

# for x in coffee.keys():
#     print(x)
#     print(coffee[x])

# print(list(coffee.keys()))
# print(list(coffee.values()))

# print(coffee.get('latte'))
# print('latte' in coffee)

# coffee['lungo']='long'
# print(coffee)
# del coffee['lungo']
# print(coffee)

# drink={'cola': 'coke'}
# # water = {**coffee, **drink}
# water=coffee|drink
# print(water)

# print(coffee.pop('mocha'))
# print(coffee)

# #p79
# a=[1,2,3]
# if 2 in a and 3 in a and 4 in a:
#     print('있')
# elif 1 in a:
#     pass
# else:
#     print('없')

# score = int(input('Input score: '))
# if score >= 90 and score <= 100:
#     result='A'
# elif 80 <= score < 90:
#     result='B'
# else:
#     result='C'
# print('result: ', result)

# #p86
# a = 5
# res = 'true' if a>3 else 'false'
# print(res)
# res2 = (lambda: 'false',lambda: 'true')[a>3]()
# print(res2)
# res3={True: 'true', False: 'false'}[a>3]
# print(res3)
# res4=(a>3) and 'true' or 'false'
# print(res4)
# res5=((a>3) and ['true'] or ['false'])[0]
# print(res5)

# #p90
# colors=['red','green','blue','yello']
# a=0
# while a<len(colors):
#     print(colors[a])
#     a+=1
# while colors:
#     print(colors.pop())
# print(len(colors))

# a=0
# while a<10:
#     a+=1
#     if a==5: continue
#     # if a==7: break
#     print(a)
# else:
#     print('over')

# #p94
# for i in [1,2,3,4,5]:
#     print(i, end=' ')
# print()
# for i in ['red','green','blue']:
#     print(i, end=' ')
# print()
# for n in {'one', 'two', 'three'}:
#     print(n, end=' ')
# print()
# for n in ('one', 'two', 'three'):
#     print(n, end=' ')
# print()
# dic={'key1':'one', 'key2':'two', 'key3':'three'}
# for d in dic.items():
#     print(d, end=' ')
# print()
# for d in dic.keys():
#     print(d, end=' ')
# print()
# for d in dic.values():
#     print(d, end=' ')
# print()

# chars=[]
# sentence = 'string python'
# for k in sentence:
#     chars.append(k)
# print(chars)

# datas=[1,2,3]
# for i, d in enumerate(datas):
#     print(i, d)
# else:
#     print('over')

# print([a+10 for a in [1,2,3]])
# print([[a+1,a*2] for a in [1,2,3]])
# li1=[2,3]
# li2=[4,5]
# print([a*b for a in li1 for b in li2])

# price={'apple':2000, 'banana':1000, 'pine':500}
# my={'apple':2, 'pine':3}
# imsi = (f for f in my)
# for i in imsi:
#     print(i)
#     print('price: {}, my: {}'.format(price[i],my[i]))
# bill=sum(price[f]*my[f] for f in my)
# print('{}'.format(bill))

# import re

# ss= """Python[3] is presented in 1991.
# Python
# """

# ss1=re.sub(r'[^a-zA-Z\s]','',ss)
# print(ss1)

# ss2=ss1.split(' ')
# print(ss2)

# cou = {}
# for i in ss2:
#     if i in cou:
#         cou[i]+=1
#     else:
#         cou[i]=1
# print(cou)

# pnum = ['111-3456', '일이삼-사오륙칠', '222-123']
# for test_str in pnum:
#     if re.match(r'^\d{3}-\d{4}$', test_str):
#         print(test_str, 'is Phone num')
#     else:
#         print(test_str, 'no pnum')


# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(0, n):
#         a, b = b, a+b
#     return a
# print(fibonacci(4))

# print(list(range(1,6)))
# print(list(range(0,11,3)))
# print(list(range(-10, -100, -20)))
# print(list(range(6)))
# print(set(range(1,6)))
# print(tuple(range(1,6)))

# for i in range(6):
#     print(i, end=' ')

# #p107 Problem

# #3-1
# a=1
# result=0
# while a<=100:
#     if a%3 == 0:
#         result+=a
#     a+=1
# print(result)

# #3-2
# a=1
# result=0
# while a<=100:
#     if a%2 != 0 and a%3 != 0:
#         print(a, end=' ')
#         result+=a
#     a+=1
# print()
# print(result)

# print(sum(range(11,100)))

# a=1
# while a<6:
#     b=0
#     while b<a:
#         print('s', end='')
#         b+=1
#     print()
#     a+=1

# a=2
# while a<=9:
#     b=1
#     while b<=9:
#         print(a,' * ',b,' = ',a*b)
#         print()
#         b+=1
#     a+=1

# import random
# num = random.randint(1,10)
# print(num)
# i=0
# while i != num:
#     i=int(input('Type: '))

# while True:
#     inp = str(input('사번,이름,기본급,입사년 입력: '))
#     inyn = str(input('Continue?[y/n] '))
#     (num, name, salary, years) = inp.split(',')
#     sudang = 50000 if int(years)<=3 else 1000000 if int(years)<=8 else 1500000
#     rate = 0.03 if int(salary)+sudang>=5000000 else 0.02 if int(salary)+sudang>4000000 else 0.01
#     print('{}, {}, {}, {}, {}, {}, {}'.format(num, name, salary, years, sudang, rate*(int(salary)+sudang), (1-rate)*(int(salary)+sudang)))
#     if inyn!='n': break

# su1=[55,67,100]
# su2=[50,60,100]
# for i in range(len(su1)):
#     print(su1[i]-su2[i])

# for a in range(1, 101):
#     if a%3==0 and a%5==0:
#         print(a)

# for a in range(2,10):
#     for b in range(1,10):
#         print(a,' * ',b,' = ',a*b, end=' ')
#     print()

# #p111
# print(sum([3,5,7]))
# print(sum({3,5,4}))
# print(sum((13,5,4)))
# input('input: ')
# print(globals())
# print(int(1.7))
# print(float(3))
# print(str(5)+'num five')

# a=10
# print('eval: ', eval('a+5'))
# print(hex(50),oct(50),bin(50), 0xab)
# print(int(round(1.2)), round(1.6))

# li1=[True, 1, False]
# print(all(li1))
# print(any(li1))

# li2=[1,3,2,5,7,6]
# print(all(a<10 for a in li2))
# print(any(a<3 for a in li2))

# x=[10,20,30]
# y=['a','b']
# for i in zip(x,y):
#     print(i)

# import math
# print(math.ceil(1.2), math.floor(1.6))

# #p115
# def dofunc1():
#     print('dofunc1 call')

# def dofunc2(name):
#     print(name)

# def dofunc3(arg1,arg2):
#     res = arg1+arg2
#     return res

# dofunc1()
# dofunc1()
# print(dofunc1())
# other = dofunc1
# other()

# print(dofunc2('korean'))
# print(dofunc3(10,20))
# print(dofunc3('py','good'))

# print(globals())

# def area_tri(a,b):
#     c=a*b/2
#     print('order2')
#     area_print(c)
#     print('order4')

# def area_print(c):
#     print('order3')
#     print('tri area: ', c)

# print('order1')
# area_tri(20, 30)
# print('order5')

# def isodd(arg):
#     return arg%2 == 1

# print({x: x*2 for x in range(1,11) if isodd(x)})

# def outerfunc():
#     def innerfunc():
#         print('inner')
#     innerfunc()
    
# outerfunc()

# def swapfunc(a,b):
#     return b,a

# a=1
# b=2
# print(swapfunc(a,b))

# player='natiaonal'
# def funcsoccer():
#     name='hong'
#     player='rep'
#     print(name, player)
# funcsoccer()

# def kbs():
#     a=1
#     def mbc():
#         nonlocal a
#         print(a)
#         a=2
#     mbc()
#     print(a)
# kbs()

# a=1
# def mbc():
#     global a
#     print(a)
#     a=2
# mbc()
# print(a)

# a=10; b=20; c=30
# print(f'a:{a}, b:{b}, c:{c}')
# def foo():
#     a=40
#     b=50
#     def bar():
#         # b=60
#         # c=70
#         nonlocal b
#         global c
#         print(f'bar1 : a:{a}, b:{b}, c:{c}')
#         b=80
#         print(f'bar2 : a:{a}, b:{b}, c:{c}')
#         c=90
#         print(f'bar3 : a:{a}, b:{b}, c:{c}')
        
#         def bar2():
#             nonlocal b
#             b=10
#         bar2()
        
#     bar()
#     print(f'foo print: a:{a}, b: {b}, c:{c}')
    
# foo()
# print(f'after func: a:{a}, b: {b}, c:{c}')

# #p122
# def showplus(start=2,end=5):
#     print(start+end)

# showplus(2,3)
# showplus(3)
# showplus()
# showplus(end=4,start=3)

# def func1(arg1, *args):
#     print(arg1, args, type(args))
#     for i in args:
#         print(f'args: {i}')

# func1('a','b','c',1)

# def func(w, h, **other):
#     print(f'weight: {w}, height: {h}')
#     print(other)
#     other['from']='islay'
#     print(other)

# dic = {'name':'Kei', 'age':'23'}
# func(65, 175, **dic)
# print(dic)

# def functotal (a,b,*v1, **v2):
#     print(a,b)
#     print(v1)
#     print(v2)

# functotal(1,2)
# functotal(1,2,3,4,5)
# functotal(1,2,3,4,5,m=6,n=7)

# def outer():
#     count =0
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner
# var1=outer()
# print(var1())
# print(var1())

# var2=outer()
# print(var2())

# def outer2(tax):
#     def inner2(su, dan):
#         amount = su*dan*tax
#         return amount
#     return inner2

# q1=outer2(0.1)
# print(q1(5,10000))
# print(q1(10,20000))
# q2=outer2(0.05)
# print(q2(5,10000))
# print(q2(10,20000))

# a = lambda x,y : x*y
# print(a(3,5), a, type(a))

# def hap(x,y):
#     return x+y
# print(hap(1,2))
# print((lambda x,y: x+y)(1,2))

# aaa= lambda x,y: x+y
# print(aaa(3,4))

# bbb= lambda a,su=10: a+su
# print(bbb(5))
# print(bbb(5,6))

# ccc = lambda a, *tu, **di : print(a,tu,di)
# ccc(1,2,3,4,m=5,n=6)

# result = list(filter(lambda a: a<5, range(10)))
# print(result)
# print(list(filter(lambda a: a%2, range(10))))

# def func1(a,b):
#     return a+b

# func2=func1
# print(func1(3,4))
# print(func2(3,4))

# def func3(func):
#     def func4():
#         print('inner func!')
#     func4()
#     return func

# mbc=func3(func1)
# print(mbc(3,4))

# #p132
# def make2(make1fn):
#     return lambda : 'hello '+make1fn()
# def make1(hellofn):
#     return lambda : 'nice to meet you '+hellofn()

# def hello():
#     return 'jay'

# hi=make2(make1(hello))
# print(hi())

# @make2
# @make1
# def hello2():
#     return 'amazing'

# hi2=hello2()
# print(hi2)

# def outer(func):
#     print('outer process')
#     def inner(no1, no2):
#         print('inner process')
#         print(f'result: {func(no1,no2)}')
#     return inner

# @outer
# def func(n1, n2):
#     print('func process')
#     return n1+n2

# func(3,4)

# #p132
# def countdown(n):
#     if n==0:
#         print('complete')
#     else:
#         print(n, end=' ')
#         countdown(n-1)

# countdown(5)

# def tot(n):
#     if n==1:
#         return 1
#     else:
#         return n+tot(n-1)
# print(tot(10))

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(10))

# #p135 practice
# #4-1
# datas=[1,3,5,7,9,2,4,6]

# def checkfunc(datas, num):
#     print(f'{num}:', end=' ')
#     print('exist') if num in datas else print('not exist')
# checkfunc(datas,2)

# #4-2
# def inputfunc():
#     gdatas = []
#     while(True):
#         datas=input('지역코드, 상품명, 수량 입력: ')
#         conyn=input('계속할까요?[y/n]: ')
        
#         def processfunc(datas: str):
#             nonlocal gdatas
#             gdatas.append(datas.split(','))
        
#         processfunc(datas)
#         if conyn=='y':
#             continue
#         elif conyn=='n':
#             tot=0
#             for data in gdatas:
#                 if data[0]=='100':
#                     print('강북', end=' ')
#                 elif data[0]=='200':
#                     print('강남', end=' ')
#                 price=450 if data[1]=='새우깡' else 300 if data[1]=='감자깡' else 0
#                 print(data[1], data[2], price, end=' ')
#                 print(int(data[2])*price)
#                 tot+=int(data[2])*price
#             print('총 건수: ', len(gdatas), '총액: ', tot)
#             break
#         else:
#             continue

# inputfunc()

# #4-3
# def gugu(n, i=1):
#     if i<10:
#         print(n,' * ',i,' = ',n*i)
#         gugu(n,i+1)
# gugu(3)

# #p138
# print('use module')
# import sys
# print('module path:', sys.path)
# import math
# print(math.pi)
# print(math.sin(math.radians(30)))

# import calendar
# calendar.setfirstweekday(6)
# calendar.prmonth(2025,3)
# del calendar

# import os
# print(os.getcwd())
# print(os.listdir('/'))

# #p140
# print('경로지정방법 -> import 패키지명.모듈명')
# import pack.mymod1
# print(dir(pack.mymod1))
# print('mymod1 함수')
# list1=[1,3]
# list2=[1,2]
# pack.mymod1.listhap(list1,list2)
# print('mod1 tot:', pack.mymod1.tot)

# from pack import mymod1
# mymod1.kbs()
# print('mod1 tot:', mymod1.tot)

# from pack.mymod1 import mbc
# mbc()

# import pack.mymod2
# re_hap = pack.mymod2.hap(5,3)
# print('hap:', re_hap)
# print('cha:', pack.mymod2.cha(5,3))

# from pack.mymod2 import hap, cha
# print('hap:', hap(5,3))
# print('cha:', cha(5,3))

# from pack.mymod4 import func
# func()

# import turtle
# def func():
#     a=turtle.Pen()
#     a.pendown()
#     a.forward(100)
#     a.right(90)
#     a.forward(100)
#     a.right(90)
#     a.forward(100)
#     a.right(90)
#     a.forward(100)
    
#     a.pencolor('blue')
#     a.circle(50, 360)
#     a.up()
#     a.forward(100)
#     a.pendown()
    
#     a.write('string draw', True, 'left', font=('돋움',24,"normal"))
#     turtle.done()

# if __name__=='__main__':
#     func()


# #p157
# class Car:
#     handle=1
#     def play(self):
#         pass
# myCar = Car()

# class Nice:
#     name='init_name'
#     def __init__(self, name):
#         print(self.name)
#         self.name=name
#         print('Constructor에 의해 ', name, '객체 생성됨')
#     def __del__(self):
#         del self.name

# obj = Nice('Tom')
# print(obj.name, obj)

# class Dog:
#     kind = 'canine'
#     def __init__(self, name):
#         self.name=name

# dog1=Dog('Shepherd')
# dog2=Dog('SiberianHusky')
# print(dog1.kind)
# print(dog2.kind)
# print(dog1.name)
# print(dog2.name)

# class TestClass:
#     aa=1
#     def __init__(self):
#         print('Constructor')
#     def __del__(self):
#         pass
#     def printMessage(self):
#         name='Korean'
#         print(name, self.aa)
# print(TestClass.aa)
# test=TestClass()
# print(test.aa)
# test.printMessage()
# print('Class type:', isinstance(test,TestClass))

# class Car:
#     handle=0
#     speed=0
    
#     def __init__(self, name, speed):
#         self.name=name
#         self.speed=speed
    
#     def showData(self):
#         km='Kilometer'
#         msg='Speed'+str(self.speed)+km
#         return msg

# car1=Car('tom',10)
# print(car1.handle, car1.name, car1.speed)
# car1.color='black'
# print(car1.color)

# car2=Car('james',20)
# print(car2.handle, car2.name, car2.speed)
# print(id(Car), id(car1),id(car2))

# print(car1.showData())
# print(car2.showData())
# car1.speed=50
# print(car1.showData())
# print(car1.speed)
# print(car2.speed)

# #p163
# kor=100
# def abc():
#     print('I\'m function')
# class My:
#     kor=90
#     def abc(self):
#         print('I\'m method')
#     def show(self):
#         print(self.kor)
#         print(kor)
#         self.abc()
#         abc()
# obj=My()
# obj.show()

# class Singer:
#     title_song='arirang'
    
#     def sing(self):
#         msg='Sing is'
#         print(msg, self.title_song, 'lulu~')

# boys=Singer()
# print('title song is', Singer.title_song)
# boys.sing()

# girls=Singer()
# girls.sing()
# girls.title_song='dancing queen'
# girls.sing()
# girls.co = 'FM'
# print(girls.co)

# print(Singer.title_song)
# Singer.title_song='beautiful'
# print(Singer.title_song)
# boys.sing()
# girls.sing()

# class PohamCar:
#     turnShow='stop'
#     def __init__(self,ownerName):
#         self.ownerName=ownerName
#         self.handle=PohamHandle()
#     def turnHandle(self, q):
#         if q>0:
#             self.turnShow = self.handle.rightTurn(q)
#         elif q<0:
#             self.turnShow = self.handle.leftTurn(q)
#         elif q==0:
#             self.turnShow = 'straight'

# class PohamHandle:
#     quantity=0
#     def leftTurn(self,quantity):
#         self.quantity=quantity
#         return 'left turn'
#     def rightTurn(self,quantity):
#         self.quantity=quantity
#         return 'right turn'

# tom=PohamCar('tom')
# tom.turnHandle(10)
# print(tom.ownerName, '의 회전량은',tom.turnShow, str(tom.handle.quantity))

# oscar=PohamCar('oscar')
# oscar.turnHandle(-25)
# print(oscar.ownerName, '의 회전량은',oscar.turnShow, str(oscar.handle.quantity))

# class Fridge:
#     isOpened=False
#     foods=[]
    
#     def open(self):
#         self.isOpened = True
#         print("Fridge Opened!")
#     def put(self, food):
#         if self.isOpened:
#             self.foods.append(food)
#             print('Something is put in firdge')
#             self.list()
#         else:
#             print('Cannot put the food')
#     def close(self):
#         self.isOpened = False
#         print("Fridge Closed!")
#     def list(self):
#         for f in self.foods:
#             print(f.irum, end=' ')
#         print()

# class FoodData:
#     def __init__(self,irum, expiry_date):
#         self.irum=irum
#         self.expiry_date=expiry_date

# f=Fridge()

# apple=FoodData('apple','2025-09-25')
# f.open()
# f.put(apple)
# f.close()

# cola=FoodData('cola','2025-10-10')
# f.put(cola)
# f.open()
# f.put(cola)
# f.close()

# class Animal:
#     def move(self):
#         print('moving creature')
# class Dog(Animal):
#     def my(self):
#         print('I\'m dog')
# dog1=Dog()
# dog1.my()
# dog1.move()
# class Horse(Animal):
#     pass
# horse1=Horse()
# horse1.move()

# class Person:
#     say='I\'m a person'
#     age=20
#     def __init__(self,age):
#         print('Person Constructor')
#         self.age=age
#     def printInfo(self):
#         print(self.say, self.age)

# # person=Person('22')
# # person.printInfo()

# class Employee(Person):
#     say='working man'
#     subject='work'
#     def __init__(self):
#         print('employee constructor')
    
#     def eprintInfo(self):
#         self.printInfo()
#         super().printInfo()
#         print(self.say)
#         print(super().say)
    
#     def printInfo(self):
#         print('Override printInfo')

# empl = Employee()
# empl.eprintInfo()

# class Worker(Person):
#     def __init__(self, age):
#         print('worker constructor')
#         super().__init__(age)
#     def wprintInfo(self):
#         self.printInfo()

# work= Worker('31')
# print(work.say, work.age)
# work.wprintInfo()

# class Programmer(Worker):
#     def __init__(self,age):
#         print('Programmer constructor')
#         Worker.__init__(self, age)
#     def pprintInfo(self):
#         self.printInfo()
#         super().printInfo()

# pr=Programmer(33)
# print(pr.say, pr.age)
# pr.pprintInfo()

# print(type(pr), Programmer.__bases__, Person.__bases__, Programmer.__mro__)

# #p178
# class Parent:
#     def printData(self):
#         print('Parent에서 실행')
# class Child1(Parent):
#     def printData(self):
#         print("Child1의 override")
# class Child2(Parent):
#     def printData(self):
#         print("Child2의 override")
#         print('Parent method와 이름은 같으나 기능이 다름')

# c1=Child1()
# c1.printData()
# c2=Child2()
# c2.printData()

# par=c1
# par.printData()
# par=c2
# par.printData()

# plist=[c1,c2]
# for item in plist:
#     item.printData()

# class ElecProduct:
#     volume=0
#     def volumeControl(self, volume):
#         pass
# class ElecTv(ElecProduct):
#     def volumeControl(self, volume):
#         self.volume+=volume
#         print('TV volume:',self.volume)
# class ElecRadio(ElecProduct):
#     def showProduct(self):
#         print("radio unique method")
#     def volumeControl(self, volume):
#         vol=volume
#         self.volume+=vol
#         print('radio volume:', self.volume)

# tv=ElecTv()
# tv.volumeControl(5)
# tv.volumeControl(-3)

# radio=ElecRadio()
# radio.volumeControl(7)
# radio.showProduct()

# product=tv
# product.volumeControl(3)
# product=radio
# product.volumeControl(3)

# class Donkey:
#     data='donkey the best'
#     def skill(self):
#         print('donkey: moving burden')
# class Horse:
#     def skill(self):
#         print("horse: running")
#     def hobby(self):
#         print('Horse\'s hobby is running')

# class Mule1(Donkey,Horse):
#     pass
# mu1=Mule1()
# print(mu1.data)
# mu1.skill()
# mu1.hobby()

# class Mule2(Horse,Donkey):
#     def play(self):
#         print("노새 고유 메서드")
#     def hobby(self):
#         print('노새는 걷기를 즐김')
#     def showhobby(self):
#         self.hobby()
#         super().hobby()
#     def showdata(self):
#         print(self.data)
#         print(super().data)

# mu2=Mule2()
# mu2.skill()
# mu2.play()
# mu2.showhobby()
# mu2.showdata()

# from abc import *

# class AbstractClass(metaclass=ABCMeta):
#     @abstractmethod
#     def abcMethod(self):
#         print('실행될 일 없음')
#         pass
    
#     def normalMethod(self):
#         print('추상클래스 내 일반 메소드')

# class Child1(AbstractClass):
#     name='I\'m child1'
    
#     def abcMethod(self):
#         print('추상메서드를 Child1에서 override')

# c1=Child1()
# print(c1.name)
# c1.abcMethod()
# c1.normalMethod()

# class Child2(AbstractClass):
#     def abcMethod(self):
#         print('추상클래스의 메소드를 Child2에서 override')
#     def normalMethod(self):
#         print('추상클래스의 일반 메소드 재정의')

# c2=Child2
# c2.abcMethod(c2)
# c2.normalMethod(c2)

# parent=c1
# parent.abcMethod()
# parent.normalMethod()

# parent=c2
# parent.abcMethod(parent)
# parent.normalMethod(c2)

# from abc import *
# class Employee(metaclass=ABCMeta):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @abstractmethod
#     def pay(self):
#         pass
    
#     @abstractmethod
#     def data_print(self):
#         pass
    
#     def nameage_print(self):
#         print(self.name, self.age, end=' ')

# class Temporary(Employee):
#     def __init__(self, name, age, ilsu, ildang):
#         Employee.__init__(self, name, age)
#         self.ilsu=ilsu
#         self.ildang=ildang
#     def pay(self):
#         return self.ilsu*self.ildang
#     def data_print(self):
#         self.nameage_print()
#         print(',월급: ', str(self.pay()))

# class Regular(Employee):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary=salary
#     def pay(self):
#         return self.salary
#     def data_print(self):
#         self.nameage_print()
#         print(',월급: ', str(self.pay()))

# t=Temporary('Hong',25, 20, 150000)
# r=Regular('Korean', 27, 350000)

# t.data_print()
# r.data_print()

# #p189
# #5-1
# class Machine:
#     cupCount=0
#     def showData(self):
#         print(self.coin, self.change)

# class Coinin(Machine):
#     coin=0
#     change=0
#     def __init__(self, coin):
#         self.coin=coin
    
#     def calc(self, cupCount):
        
#         pass

# c=Coinin(int(input('동전을 입력하세요:')))
# c.calc(int(input('몇 잔을 원하세요:')))
# c.showData()

# #5-2
# from abc import *
# class Pen(metaclass=ABCMeta):
#     # @abstractmethod
#     def writeLetter(self):
#         print('Write words')

# class Pencil(Pen):
#     def writeLetter(self):
#         print('Write words with pencil')

# class Ballpen(Pen):
#     def writeLetter(self):
#         print('Write words with ballpen')

# class Fountainpen(Pen):
#     pass

# a=Fountainpen()
# a.writeLetter()

# #p192
# try:
#     su=0
#     5/su
# except ZeroDivisionError as err:
#     print('Error:', err)
# finally:
#     print('over')

# def divideFunc(a,b):
#     return a/b

# c=divideFunc(5,2)
# # c=divideFunc(5,0)
# print(c)

# try:
#     c=divideFunc(5,2)
#     print(c)
    
#     c=divideFunc(5,0)
#     print(c)
    
#     aa=[1,2]
#     print(aa[0])
#     print(aa[3])
    
#     f=open('./hihi.txt')
    
# except ZeroDivisionError:
#     print('0으로 못나눔')
# except IndexError as e:
#     print('참조 범위 오류:', e)
# except Exception as e:
#     print('Error:', e)
# finally:
#     print('Over')

# def func(str):
#     datas=['kbs','mbc']
#     if str not in datas:
#         raise ValueError
#     print('good')

# try:
#     func('kbs')
#     func('mbc')
#     func('sbs')
# except ValueError:
#     print('잘못된 값!')

# obj=open('./test.txt','w')
# for i in range(1,6):
#     obj.write(f'Hi {i} ')
# obj.write('\n')
# obj.writelines(['Lagavulin', 'Laphroaig', 'Ardbeg'])
# obj.close()

# import os
# print(os.getcwd()+'/test.txt')
# try:
#     letter=open(os.getcwd()+'/test.txt',mode='r', encoding='UTF-8')
#     print('1', letter.read())
#     letter.close()
    
#     letter2=open(os.getcwd()+'/test.txt',mode='r', encoding='UTF-8')
#     # for i in range(1,3):
#     #     line = letter2.readline()
#     #     print('2', line)
#     for line in letter2:
#         print('2', line.rstrip())
#     letter2.close()
    
#     letter3=open(os.getcwd()+'/test.txt',mode='r', encoding='UTF-8')
#     lines = letter3.readlines()
#     print('3', lines)
#     letter3.close()
    
# except Exception as e:
#     print('File error:', e)

# import os
# try:
#     letter=open(os.getcwd()+'/test2.txt', mode='w', encoding='UTF-8')
#     letter.write('My friend')
#     letter.close()
    
#     letter=open(os.getcwd()+'/test2.txt', mode='w', encoding='UTF-8')
#     letter.write('My computer')
#     letter.write('\n')
#     letter.write('I need GPU')
#     letter.close()
    
#     f=open('test2.txt')
#     print(f.read())
#     f.close()
    
# except Exception as e:
#     print(e)

# try:
#     letter=open('test3.txt', 'w')
#     letter.write('My friend')
#     letter.write('\n')
#     letter.close()
    
#     letter=open('test3.txt', 'a')
#     letter.write('How ar you?')
#     letter.write('\n')
#     letter.write('I am fine')
#     letter.close()
    
#     letter=open('test3.txt', 'a')
#     letter.write('\nGood job')
#     letter.close()
    
#     f=open('test3.txt')
#     print(f.read())
#     f.close()
    
# except Exception as e:
#     print(e)

# with open('test4.txt', 'w', encoding='UTF-8') as f1:
#     f1.write('Python')
#     f1.write('\nGood')
#     f1.write('\nGreat')

# with open('test4.txt','r') as f2:
#     print(f2.read())

# import re

# def replaceFunc(fname, source, target):
#     with open(fname, 'r', encoding='UTF-8') as f3:
#         ss=f3.read()
#         ss=re.sub(source,target,ss)
#     return ss

# result=replaceFunc('test4.txt','G','GgG')
# print(result)

# import pickle

# with open('test.pickle', 'wb') as fobj:
#     phones={'tom':'111-1111', '길동':'222-2222'}
#     li=['마우스','키보드']
#     t=(phones, li)
#     pickle.dump(t,fobj)
#     pickle.dump(li,fobj)

# with open('test.pickle', 'rb') as fobj:
#     a,b=pickle.load(fobj)
#     c=pickle.load(fobj)

# print(a)
# print(b)
# print(c)

# #p205
# #6-1
# with open('zipcode.txt','w',encoding='UTF-8') as f:
#     f.write(
# '''135-985\t서울\t강남구\t역삼1동\tGS
# 135-769\t서울\t강남구\t역삼1동\tKTB
# 135-984\t서울\t강남구\t역삼2동\t하하하
# 135-703\t서울\t강남구\t역삼2동\t과학
# 121-726\t서울\t마포구\t대흥동\t한국'''
#     )


# with open('zipcode.txt','r',encoding='UTF-8') as f:
#     # s=f.read()
#     # parse=list(map(lambda x: x.split('\t'), s.split('\n')))
    
#     dong=input('동이름 입력:')
#     # result = list(filter(lambda x: x[3]==dong, parse))
    
#     line=f.readline()
#     while line:
#         parse=line.rstrip().split('\t')
#         if parse[3] == dong:
#             print(f'[{parse[0]}]{parse[1]} {parse[2]} {parse[3]} {parse[4]}')
#         line=f.readline()

# #6-2
# with open('number.txt','w') as f:
#     f.write(
# '''10 5
# 10 -5
# 10 5.3
# 10 -5.3
# 10 20 30 40 50''')

# with open('number.txt', 'r') as f:
#     for line in f:
#         print(eval('+'.join(line.rstrip().split(' '))))

