#!/usr/bin/env python
# coding: utf-8

# # Exemplo de tratamento de dados: Steam

# In[66]:


import pandas as pd

dados = pd.read_csv('STC_set_data.csv')
dados.head()


# ## Remover os dados inúteis para o tratamento (trabalharemos com cartas e boosters)

# In[67]:


dados = dados.drop(["# Owned", "# Unique", "Badge Lvl", "Emote Avg", "BG Avg", "Added"], axis=1)
dados.head()


# ## Verificar os tipos presentes nas colunas estão aceitáveis:

# In[64]:


formato_dos_dados = dados.dtypes
formato_dos_dados


# In[ ]:




