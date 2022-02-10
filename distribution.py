#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as sms
import seaborn as s
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[30]:


n_size_1 = 1000
rang = np.random.default_rng(50)

# s.set_style('white')
# f, axes=plt.subplots(2,2, figsize=(30,20),sharex=True,sharey=True)

# #normal distribution
distribution1=np.random.normal(20.3, 2.2, n_size_1)
distribution2=np.random.normal(22, 6, n_size_1)
distribution3=np.random.normal(30.5, 5, n_size_1)
distribution4=np.random.normal(40, 2, n_size_1)

axes[0,0].hist(distribution1,bins=10,color='orange')
axes[0,0].set_title('Normal Distribution')
axes[0,0].set_xlabel('n = 1000, Mu=20.3 , Sigma = 2.2 ')
axes[0,0].set_ylabel('Range')


axes[1,0].hist(distribution2,bins=10,color='orange')
axes[1,0].set_title('Normal Distribution')
axes[1,0].set_xlabel('n = 1000, Mu=22.6 , Sigma = 6 ')
axes[1,0].set_ylabel('Range')

axes[0,1].hist(distribution3,bins=10,color='orange')
axes[0,1].set_title('Normal Distribution')
axes[0,1].set_xlabel('n = 1000, Mu=30.5 , Sigma = 5 ')
axes[0,1].set_ylabel('Range')

axes[1,1].hist(distribution4,bins=10,color='orange')
axes[1,1].set_title('Normal Distribution')
axes[1,1].set_xlabel('n = 1000, Mu=40 , Sigma = 2 ')
axes[1,1].set_ylabel('Range')

#exponential distribution

s.set_style('white')
f, axes1=plt.subplots(2,2, figsize=(30,20),sharex=True,sharey=True)
exponential_distribution1 = sms.expon.rvs(loc=0.5, scale=1.2, size=n_size_1)
exponential_distribution2 = sms.expon.rvs(loc=0.6, scale=5.3, size=n_size_1)
exponential_distribution3 = sms.expon.rvs(loc=0.7, scale=3.5, size=n_size_1)
exponential_distribution4 = sms.expon.rvs(loc=0.8, scale=6.5, size=n_size_1)

axes1[0,0].hist(exponential_distribution1,bins=10,color = 'red')
axes1[0,0].set_title('Exponential Distribution')
axes1[0,0].set_xlabel('n = 1000, Loc = 0.5 , Scale =1.2')
axes1[0,0].set_ylabel('Exponential_Range')

axes1[1,0].hist(exponential_distribution2,bins=10,color = 'red')
axes1[1,0].set_title('Exponential Distribution')
axes1[1,0].set_xlabel('n = 1000, Loc = 0.6 , Scale =5.3')
axes1[1,0].set_ylabel('Exponential_Range')

axes1[0,1].hist(exponential_distribution3,bins=10,color = 'red')
axes1[0,1].set_title('Exponential Distribution')
axes1[0,1].set_xlabel('n = 1000, Loc = 0.7 , Scale =3.5')
axes1[0,1].set_ylabel('Exponential_Range')

axes1[1,1].hist(exponential_distribution4,bins=10,color = 'red')
axes1[1,1].set_title('Exponential Distribution')
axes1[1,1].set_xlabel('n = 1000, Loc = 0.8 , Scale =6.5')
axes1[1,1].set_ylabel('Exponential_Range')


#  binomial distribution
s.set_style('white')
f, axes2=plt.subplots(2,2, figsize=(30,20),sharex=True,sharey=True)
binomial1= np.random.binomial(n=10, p=0.5, size=n_size_1)
binomial2= np.random.binomial(n=20, p=0.9, size=n_size_1)
binomial3= np.random.binomial(n=15, p=0.2, size=n_size_1)
binomial4= np.random.binomial(n=25, p=0.8, size=n_size_1)

axes2[0,0].hist(binomial1,bins=10, color = 'skyblue')
axes2[0,0].set_title('Binomial Distribution')
axes2[0,0].set_xlabel('n = 1000, n= 10 , p = 0.5')
axes2[0,0].set_ylabel('Binomial_Range')

axes2[0,1].hist(binomial2,bins=10, color = 'skyblue')
axes2[0,1].set_title('Binomial Distribution')
axes2[0,1].set_xlabel('n = 1000, n= 20 , p = 0.9')
axes2[0,1].set_ylabel('Binomial_Range')

axes2[1,0].hist(binomial3,bins=10, color = 'skyblue')
axes2[1,0].set_title('Binomial Distribution')
axes2[1,0].set_xlabel('n = 1000, n= 15 , p = 0.2')
axes2[1,0].set_ylabel('Binomial_Range')

axes2[1,1].hist(binomial4,bins=10, color = 'skyblue')
axes2[1,1].set_title('Binomial Distribution')
axes2[1,1].set_xlabel('n = 1000, n= 25 , p = 0.8')
axes2[1,1].set_ylabel('Binomial_Range')

#poisson distribution
s.set_style('white')
f, axes3=plt.subplots(2,2, figsize=(30,20),sharex=True,sharey=True)
poisson1=np.random.poisson(5, n_size_1)
poisson2=np.random.poisson(8, n_size_1)
poisson3=np.random.poisson(10, n_size_1)
poisson4=np.random.poisson(12, n_size_1)

axes3[0,0].hist(poisson1,bins=10, color = 'green')
axes3[0,0].set_title('Poisson Distribution')
axes3[0,0].set_xlabel('n = 1000, Lamda = 5')
axes3[0,0].set_ylabel('Poisson_Range')

axes3[0,1].hist(poisson2,bins=10, color = 'green')
axes3[0,1].set_title('Poisson Distribution')
axes3[0,1].set_xlabel('n = 1000, Lamda = 8')
axes3[0,1].set_ylabel('Poisson_Range')

axes3[1,0].hist(poisson3,bins=10, color = 'green')
axes3[1,0].set_title('Poisson Distribution')
axes3[1,0].set_xlabel('n = 1000, Lamda = 10')
axes3[1,0].set_ylabel('Poisson_Range')

axes3[1,1].hist(poisson4,bins=10, color = 'green')
axes3[1,1].set_title('Poisson Distribution')
axes3[1,1].set_xlabel('n = 1000, Lamda = 12')
axes3[1,1].set_ylabel('Poisson_Range')

#uniform distribution
s.set_style('white')
f, axes4=plt.subplots(2,2, figsize=(30,20),sharex=True,sharey=True)
uniform1= np.random.uniform(-10,0,n_size_1)
uniform2= np.random.uniform(-2,5,n_size_1)
uniform3= np.random.uniform(0,10,n_size_1)
uniform4= np.random.uniform(5,20,n_size_1)

axes4[0,0].hist(uniform1,bins=10, color = 'blue')
axes4[0,0].set_title('Uniform Distribution')
axes4[0,0].set_xlabel('n = 1000, Low = -10 , High =0')
axes4[0,0].set_ylabel('Uniform_Range')

axes4[0,1].hist(uniform2,bins=10, color = 'blue')
axes4[0,1].set_title('Uniform Distribution')
axes4[0,1].set_xlabel('n = 1000, Low = -2 , High =5')
axes4[0,1].set_ylabel('Uniform_Range')

axes4[1,0].hist(uniform3,bins=10, color = 'blue')
axes4[1,0].set_title('Uniform Distribution')
axes4[1,0].set_xlabel('n = 1000, Low = 0 , High =10')
axes4[1,0].set_ylabel('Uniform_Range')

axes4[1,1].hist(uniform4,bins=10, color = 'blue')
axes4[1,1].set_title('Uniform Distribution')
axes4[1,1].set_xlabel('n = 1000, Low = 5 , High =20')
axes4[1,1].set_ylabel('Uniform_Range')

plt.rcParams["figure.figsize"]=[20,10]
plt.show()


# In[ ]:




