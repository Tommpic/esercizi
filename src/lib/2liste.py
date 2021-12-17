import math

a=[0,1,2,3,4,5,6,7]

print(a[0:5])
print(a[0:5:2])
print(a[0::2])

b=list(range(6))
print(b) 
print(type(b)) 

import time
l=list(range(100000000))
v=list(range(1000000))
T1=time.perf_counter()
s=l+v
T2=time.perf_counter()
print(' + execution time: :' , T2-T1, 's' )
T3=time.perf_counter()
list.extend(s)
T4=time.perf_counter()
print('extend execution time:', T4-T3 , 's')

stack=[1, 2, 3, 4]
print('Initial Stack : ', stack)
for i in list(range(5,7)):
    stack.append(i)
print ('Append: ', stack)
stack.pop()
print ('Pop: ' , stack)
queue=[ 'a','b','c','d' ]
print('Initial Queue : ', queue)
queue.append('e')
queue.append('f')
print('Append : ', queue)
queue.pop(0)
print('Pop : ', queue)