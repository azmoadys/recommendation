#!/usr/bin/env python
# coding: utf-8

# In[4]:


from googletrans import Translator


# In[11]:


class translator:
    def ToKorean(self, t):
        trns = Translator()
        return trns.translate(t, dest='ko').text

# In[12]:


if __name__=='__main__':
    a = c_trans()
    print(a.trans('hello, world!'))


# In[ ]:




