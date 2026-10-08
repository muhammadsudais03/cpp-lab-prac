import numpy as np
import time
import matplotlib.pyplot as plt

# a=np.array([1,2,3,4],dtype=complex)
# print(a)

# a=np.array([1,2,3,4],dtype=float)
# print(a)

# a=np.array([1,2,3,4],dtype=bool)
# print(a)
# # print(type(a))

# b=np.array([[1,2,3,4],[5,6,7,8]])
# print(b)

# c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c)

# a=np.arange(1,21)
# a=a.reshape(2,10)
# print(a)

# a=np.ones((2,4))
# print(a)

# b=np.zeros((5,10))
# print(b)

# a=np.random.random((4,5))
# print(a)

# a=np.linspace(-1,9,10)
# print(a)

# a=np.identity(5)
# print(a)

# a1=np.arange(10, dtype=np.int32)
# a2=np.arange(12, dtype=float).reshape(3,4)
# a3=np.arange(64).reshape(4,4,4)
# print(a1.ndim)
# print(a2.ndim)
# print(a3)
# print(a3.shape)
# print(a3.size)
# print(a2.itemsize)
# print(a1.dtype)
# print(a2.dtype)
# print(a2.dtype)

# a2=a2.astype(np.int32)
# print(a2.dtype)


# a2=np.arange(10,22).reshape(3,4)
# a3=np.arange(30,42).reshape(3,4)
# print(a2==15) 
# a1=a2**a3
# print(a1)

# a1=np.random.random((3,4))
# a1=np.round(a1*100)
# print(a1)
# print(np.max(a1))
# print(np.min(a1))
# print(np.mean(a1))
# print(np.prod(a1))
# print(np.sum(a1))
# print(np.max(a1,axis=1))
# print(np.min(a1,axis=0))
# print(np.prod(a1,axis=0))
# print(np.mean(a1,axis=1))

# a1=np.round(np.random.random((2,3)))
# a2=np.ceil(np.random.random((2,3)))
# a3=np.floor(np.random.random((2,3)))
# a3=np.random.random((3,3)).view(int)
# a2=np.round(a2*1)
# a3=np.round(a3*1)
# print(np.dot(a2,a3))
# print(a1)
# print(a2)
# print(a3)

# a1=np.arange(12,68,5)
# print(a1[4:8])

# a2=np.arange(12).reshape(3,4)
# print(a2)
# print(a2[1,:])
# print(a2[:,2])
# print(a2[1,1:4])
# print(a2[2,1:4])
# print(a2[:2,:3])
# print(a2[::2,1::2])
# print(a2[1,::3])
# print(a2[:2,1:4])



# a3=np.arange(8).reshape(2,2,2)
# print(a3)
# print(a3[0,1,0])
# print(a3[1,0,1])
# print(a3[1,1,0])
# print(a3[0,0,0])

# a3=np.arange(27).reshape(3,3,3)
# print(a3[2,1:,1:])
# print(a3[::2,0,::2])


# a3=np.arange(27).reshape(3,3,3)
# for i in np.nditer(a3):
#     print(i)

# a2=np.arange(12).reshape(3,4)
# print(a2)
# a2=np.transpose(a2)
# a2=a2.T
# print(a2)

# a2=np.arange(12).reshape(3,4)
# a2=a2.ravel()
# print(a2)

# a4=np.arange(12).reshape(3,4)
# a5=np.arange(12,24).reshape(3,4)
# b=np.hstack((a4,a5))
# c=np.vstack((a4,a5))
# d=np.hsplit(b,2)
# e=np.vsplit(c,2)
# print(b)
# print(c)
# print(e)
# print(d)

# a=[i for i in range(10000000)]
# b=[i for i in range(10000000,20000000)]
# c=[]
# start=time.time()
# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print(time.time()-start)
# import sys
# a=np.arange(10000000)
# b=np.arange(10000000,20000000)
# c=[]
# start=time.time()
# c=a+b
# print(time.time()-start)
# print(sys.getsizeof(a)/1024**2)

# import sys
# a=[i for i in range(10000000)]
# print(sys.getsizeof(a)/1024**2)
# a=np.arange(10000000,dtype=np.int8)
# print(sys.getsizeof(a)//1024**2)
# a=np.arange(24).reshape(6,4)
# print(a[[0,2,4,5]])
# print(a[:5,[0,2,3]])

# a=np.random.randint(1,100,24).reshape(6,4)
# print(a>50)
# print(a%2==0)
# print(a[a>50])
# print(a[a%2==0])
# print((a>50) & (a%2==0))
# print(a[(a>50) & (a%2==0)])
# print(a%7==0)
# print(a[a%7==0])
# a=np.arange(12).reshape(4,3)
# b=np.arange(3)
# print(a)
# print(b)
# print(a+b)
# a=np.arange(12).reshape(3,4)
# b=np.arange(3)
# print(a)
# print(b)
# print(a+b)
# a=np.arange(3).reshape(1,3)
# b=np.arange(3).reshape(3,1)
# print(a)
# print(b)
# print(a+b)
# a=np.arange(3).reshape(1,3)
# b=np.arange(4).reshape(4,1)
# print(a)
# print(b)
# print(a+b)
# a=np.array([1])
# b=np.arange(4).reshape(2,2)
# print(a)
# print(b)
# print(a+b)
# a=np.arange(12).reshape(3,4)
# b=np.arange(12).reshape(4,3)
# print(a)
# print(b)
# print(a+b)
# a=np.arange(16).reshape(4,4)
# b=np.arange(4).reshape(2,2)
# print(a)    
# print(b)
# print(a+b)

# a=np.arange(10)
# def sigmoid(array):
#     return 1/(1+np.exp(-(array)))
# print(sigmoid(a))

# actual=np.array([0,1,0])
# predicted=np.array([0.1,0.8,0.1])

# def mse(act,pre):
#     return np.mean((act-pre)**2)
# print(mse(actual,predicted))

# def cce(act,pre):
#     return np.mean(act*-np.log(pre))

# print(cce(actual,predicted))

# a=np.array([1,2,3,4,5,np.nan,4,3,2,np.nan,5,5,3,1,np.nan])
# print(a[~np.isnan(a)])

# x=np.linspace(-4,7,28)
# y=x**2
# plt.plot(x,y)
# plt.show()

# x=np.linspace(-4,7,28)
# y=np.sin(x)
# plt.plot(x,y)
# plt.show()

# x=np.linspace(-4,7,28)
# y=x*np.log(x)
# plt.plot(x,y)
# plt.show()

# x=np.linspace(-4,7,28)
# y=1/(1+np.exp(-x))
# plt.plot(x,y)
# plt.show()

# a=np.random.randint(1,100,15)
# print(a)
# print(np.sort(a))

# b=np.random.randint(1,100,24).reshape(6,4)
# print(b)
# print(np.sort(b,axis=0))
# print(np.append(b,np.ones((b.shape[0],1)),axis=1))
# print(np.append(b,np.random.random((b.shape[0],1)),axis=1))

# a=np.arange(6).reshape(2,3)
# b=np.arange(6).reshape(2,3)
# print(np.concatenate((a,b),axis=0))
# print(np.concatenate((a,b),axis=1))

# e=np.array([1,2,2,3,3,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8])
# print(np.unique(e))

# a=np.random.randint(1,100,15)
# b=np.random.randint(1,100,12).reshape(3,4)
# print(np.where(a>50))
# print(np.where(a>50,101,a))
# print(np.where(a%2==0,0,a))
# print(np.argmax(a))
# print(a)
# print(np.cumsum(a))
# print(np.cumsum(a))
# print(b)
# print(np.cumprod(b))
# print(np.cumprod(b))

# a=np.random.randint(1,100,15)
# print(a)
# print(np.percentile(a,100))
# print(np.percentile(a,0))
# print(np.percentile(a,50))
# print(np.percentile(a,75))
# print(np.percentile(a,65))

# a=np.random.randint(1,100,15)
# print(a,np.histogram(a,bins=[0,30,60,90,100]))

# salary=np.array([1000,3000,9000,27000,81000])
# exp=np.array([1,2,3,4,5])
# print(np.corrcoef(salary,exp))

# a=np.arange(1,100,15)
# b=np.arange(12).reshape(3,4)
# items=[12,45,32,56,32,67,98,47,68,74,27,42]
# print(a,np.flip(a))
# print(b,np.flip(b))
# print(b,np.flip(b),axis=0)
# print(b)

# a=np.random.randint(1,100,15)
# a=np.random.randint(1,100,15)
# print(a,np.put(a,[0,1,5,8,7,10,13],[45,76,23,99,32,34,78]))
# print(np.delete(a,[0,6,2,7,10]))

# a=np.random.randint(1,100,5)
# b=np.random.randint(1,100,5)
# print(a,b,np.union1d(a,b))
# print(np.intersect1d(a,b))
# print(np.setdiff1d(a,b))
# print(np.setxor1d(a,b))
# print(np.in1d(a,5))

a=np.random.randint(1,100,15)
print(a,np.clip(a,a_min=20,a_max=95))