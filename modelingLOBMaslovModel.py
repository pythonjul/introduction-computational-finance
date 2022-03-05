import random
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf



askList=[] #we buy
askSaved=[]
bidList=[] #we sell
bidSaved=[]
K=1; r=0.5;N=1000
p=[]
pp=50#prix'
p.append(pp)
time=range(0, N)

for i in range(0,N):
        t1=random.randint(0, 1) #1 means we buy, 0 means we sell
        t2=np.random.binomial(n=1, p= r)
        
        if t1==1:
            if not askList:
                t2=1
        if t1==0:
            if not bidList:
                t2=1
        
        if t1==1 and t2==1:
            p.append(pp)
            bidList.append(pp-K)
            bidList.sort(reverse = True) #trie de manière decroissant
            if not askList:
                askSaved.append(pp)
            else:
                askSaved.append(askList[0])
            if not bidList:
                bidSaved.append(pp)
            else:
                bidSaved.append(bidList[0])
        if t1==1 and t2==0:
            pp=askList.pop(0)
            p.append(pp)
            if not askList:
                askSaved.append(pp)
            else:
                askSaved.append(askList[0])
            if not bidList:
                bidSaved.append(pp)
            else:
                bidSaved.append(bidList[0])
            
        if t1==0 and t2==1:
            p.append(pp)
            askList.append(pp+K)
            askList.sort() #trie de facon croissante
            if not askList:
                askSaved.append(pp)
            else:
                askSaved.append(askList[0])
            if not bidList:
                bidSaved.append(pp)
            else:
                bidSaved.append(bidList[0])

        if t1==0 and t2==0:
            pp=bidList.pop(0)
            p.append(pp)
            if not askList:
                askSaved.append(pp)
            else:
                askSaved.append(askList[0])
            if not bidList:
                bidSaved.append(pp)
            else:
                bidSaved.append(bidList[0])

del p[0]
soustr=np.subtract(askSaved,bidSaved)
f = plt.figure(1)
plt.plot(time, p, 'b-', label='prix')
plt.plot(time, askSaved, 'g-', label='ask')
plt.plot(time, bidSaved, 'r-', label='bid')
plt.xlabel('temps')
plt.ylabel('valeur')  
plt.title('evolution du prix')
plt.legend(loc='upper left')
f.show()

g = plt.figure(2)
plt.plot(time,soustr)
plt.xlabel('temps')
plt.ylabel('valeur')  
plt.title('evolution du spread')
g.show()

ret=[0]
for i in range(1,N):
    ret.append((p[i]/p[i-1])-1)
    
h=plt.figure(3)
plt.plot(time,ret)
plt.xlabel('temps')
plt.ylabel('valeur')  
plt.title('evolution des returns')
h.show()

i=plt.figure(4)
nlags=N
temp=acf(ret, unbiased=True, nlags=nlags-1)
plt.plot(time,temp)
plt.xlabel("lag")
#plt.ylim([-1.2, 1.2])
plt.ylabel("value")
plt.title('ACF')
i.show()

j=plt.figure(5)
mid1=np.add(askSaved,bidSaved)
mid2=np.divide(mid1,2)
soustr2=np.subtract(mid2,p)
plt.plot(time,soustr2)
plt.xlabel('temps')
plt.ylabel('valeur')  
plt.title('midprice-marketprice')
j.show()



#np.savetxt('R/testArray1000.txt', ret, fmt='%f')


# In[3]:


import random
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf



askList=[] #we buy
askSaved=[]
bidList=[] #we sell
bidSaved=[]
K=0.1; r=0.5;N=1000
p=[]
pp=50#prix'
p.append(pp)
time=range(0, N)

for i in range(0,N):
        t1=random.randint(0, 1) #1 means we buy, 0 means we sell
        t2=np.random.binomial(n=1, p= r)
        
        if t1==1:
            if not askList:
                t2=1
        if t1==0:
            if not bidList:
                t2=1
        
        if t1==1 and t2==1:
            p.append(pp)
            bidList.append(pp-K)
            bidList.sort(reverse = True) #trie de manière decroissant
            if not askList:
                askSaved.append(pp)
            else:
                askSaved.append(askList[0])
            if not bidList:
                bidSaved.append(pp)
            else:
                bidSaved.append(bidList[0])
        if t1==1 and t2==0:
            pp=askList.pop(0)
            p.append(pp)
            if not askList:
                askSaved.append(pp)
            else:
                askSaved.append(askList[0])
            if not bidList:
                bidSaved.append(pp)
            else:
                bidSaved.append(bidList[0])
            
        if t1==0 and t2==1:
            p.append(pp)
            askList.append(pp+K)
            askList.sort() #trie de facon croissante
            if not askList:
                askSaved.append(pp)
            else:
                askSaved.append(askList[0])
            if not bidList:
                bidSaved.append(pp)
            else:
                bidSaved.append(bidList[0])

        if t1==0 and t2==0:
            pp=bidList.pop(0)
            p.append(pp)
            if not askList:
                askSaved.append(pp)
            else:
                askSaved.append(askList[0])
            if not bidList:
                bidSaved.append(pp)
            else:
                bidSaved.append(bidList[0])

del p[0]
soustr=np.subtract(askSaved,bidSaved)
f = plt.figure(1)
plt.plot(time, p, 'b-', label='prix')
plt.plot(time, askSaved, 'g-', label='ask')
plt.plot(time, bidSaved, 'r-', label='bid')
plt.xlabel('temps')
plt.ylabel('valeur')  
plt.title('evolution du prix')
plt.legend(loc='upper left')
f.show()

g = plt.figure(2)
plt.plot(time,soustr)
plt.xlabel('temps')
plt.ylabel('valeur')  
plt.title('evolution du spread')
g.show()

ret=[0]
for i in range(1,N):
    ret.append((p[i]/p[i-1])-1)
    
h=plt.figure(3)
plt.plot(time,ret)
plt.xlabel('temps')
plt.ylabel('valeur')  
plt.title('evolution des returns')
h.show()

i=plt.figure(4)
nlags=N
temp=acf(ret, unbiased=True, nlags=nlags-1)
plt.plot(time,temp)
plt.xlabel("lag")
#plt.ylim([-1.2, 1.2])
plt.ylabel("value")
plt.title('ACF')
i.show()

j=plt.figure(5)
mid1=np.add(askSaved,bidSaved)
mid2=np.divide(mid1,2)
soustr2=np.subtract(mid2,p)
plt.plot(time,soustr2)
plt.xlabel('temps')
plt.ylabel('valeur')  
plt.title('midprice-marketprice')
j.show()



np.savetxt('R/K0_1testArray1000.txt', ret, fmt='%f')

