#!/usr/bin/env python
# coding: utf-8

# In[53]:


get_ipython().system('pip3 install numpy')
import numpy as np
print(np)
print(np.__version__)


# In[88]:


#Q1 生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a=np.arange(21)
print("A1. 數列：", a)
type(a)


# In[89]:


#2 呈上題，將以上數列取出偶數。
b=np.arange(0,21,2)
print("A2. 偶數：", b)


# In[90]:


#3 呈1題，將數列取出3的倍數。
c=np.arange(0,21,3)
print("A3. 3的倍數：",c)


# In[91]:


#Q4 [簡答題] 請問下列兩種將 Array 轉換成 List 的方式有何不同？
print("A4. 用list(a)只會轉換整個array的第一層資料，\n用a.tolist可以轉換整個函數裡的資料。")


# In[86]:


#Q5請試著在程式中印出以下三個 NdArray 的屬性？
#（屬性：ndim、shape、size、dtype、itemsize、length、type）
a = np.random.randint(10, size=6) 
b = np.random.randint(10, size=(3,4)) 
c = np.random.randint(10, size=(2,3,2)) 
print("A5.a. 陣列A")
print(a)
print("ndim 陣列中的維度數：", a.ndim)
print("shape 每個維度的大小：", a.shape)
print("size 陣列中的元素數：", a.size)
print("dtype 陣列中元素的資料型態：",a.dtype)
print("itemsize 陣列中每個元素佔的空間：", a.itemsize)
print("length 列表的元素數：", len(a))
print("type 變數的型態：", type(a))
print("A5.b. 陣列B")
print(b)
print("ndim 陣列的維度數：", b.ndim)
print("shape 每個維度的大小：", b.shape)
print("size 陣列中的元素數：", b.size)
print("dtype 陣列中元素的資料型態：", b.dtype)
print("itemsize 陣列中每個元素所佔的空間：", b.itemsize)
print("lenght 列表的元素數：", len(b))
print("type 變數的種類：", type(b))
print("A5.c. 陣列C")
print(c)
print("ndim 陣列的維度數：", c.ndim)
print("shape 每個維度的大小：", c.shape)
print("size 陣列中有幾個元素：", c.size)
print("dtype 陣列中資料的型態：", c.dtype)
print("itemsize 陣列中每個元素佔用的空間：", c.itemsize)
print("length 列表中有幾個元素：", len(c))
print("type 變數的類型：", type(c))


# In[87]:


#Q6 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
a=np.arange(21).reshape(3,7)
print("A6.")
print("一個array如下")
print(a)
print("6.1. 用list(...)的結果如下")
print(list(a))
print("6.2. 用a.tolist()的結果如下")
print(a.tolist())
print("6.3. 用list()來實現s.tolist()的效果如下")
for l in a:
    print(list(l))
    


# In[ ]:




