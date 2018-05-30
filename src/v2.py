
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
sns.set(style='white', context='notebook', palette='Set2')

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


games = pd.read_csv("../dataset/online-data/games.csv")
units = pd.read_csv("../dataset/online-data/units.csv")
orders = pd.read_csv("../dataset/online-data/orders.csv")
turns = pd.read_csv("../dataset/online-data/turns.csv")
players = pd.read_csv("../dataset/online-data/players.csv")


# ## データセットの確認
# https://data.world/maxstrange/diplomacyboardgame

# In[3]:


games.head()


# In[4]:


players.head()


# In[5]:


units.head()


# In[6]:


turns.head()


# In[8]:


orders.head()


# ## データ分析
# ### gameの外観

# In[20]:


# turn数
x = games['num_turns']
sns.distplot(x, kde=False, rug=False, bins=100)


# In[24]:


# プレイヤー数
sns.countplot(x="num_players", data = games)


# In[11]:


# 国ごとの勝率比較
sns.barplot(x="country", y="won", data = players)


# In[19]:


# 国と終了ターンの相関
correlation_matrix = np.corrcoef([players[(players["country"] == "E")]["end_turn"],
           players[(players["country"] == "F")]["end_turn"],
           players[(players["country"] == "I")]["end_turn"],
           players[(players["country"] == "G")]["end_turn"],
           players[(players["country"] == "A")]["end_turn"],
           players[(players["country"] == "T")]["end_turn"],
           players[(players["country"] == "R")]["end_turn"]])
correlation_matrix = pd.DataFrame(correlation_matrix)
correlation_matrix = correlation_matrix.rename(columns={0:"ENG", 1:"FRA", 2:"ITA", 3:"GER", 4:"AUS", 5:"TUR", 6:"RUS"},
                                              index={0:"ENG", 1:"FRA", 2:"ITA", 3:"GER", 4:"AUS", 5:"TUR", 6:"RUS"})

plt.figure(figsize=(7,6))
plt.title("end_turn")
sns.heatmap(correlation_matrix, annot=True, linewidths=0.1, square=True, cmap="RdBu")


# ### 補給地

# In[12]:


# 国ごとの補給地の数（平均, 勝ち負け別）
sns.barplot(x="country", y="num_supply_centers", hue="won", data = players)


# #### 国と補給地数の相関を調べる

# In[13]:


# # 補給地の数の相関，年毎
for i in range(1901, 1920):
    correlation_matrix = np.corrcoef([turns[(turns["year"] == i)]["scs_england"],
           turns[(turns["year"] == i)]["scs_france"],
           turns[(turns["year"] == i)]["scs_italy"],
           turns[(turns["year"] == i)]["scs_russia"],
           turns[(turns["year"] == i)]["scs_turkey"],
           turns[(turns["year"] == i)]["scs_germany"],
           turns[(turns["year"] == i)]["scs_austria"]])
    correlation_matrix = pd.DataFrame(correlation_matrix)
    correlation_matrix = correlation_matrix.rename(columns={0:"ENG", 1:"FRA", 2:"ITA", 3:"GER", 4:"AUS", 5:"TUR", 6:"RUS"},
                                              index={0:"ENG", 1:"FRA", 2:"ITA", 3:"GER", 4:"AUS", 5:"TUR", 6:"RUS"})
    plt.figure(figsize=(18, 6))
    plt.title(i)
    sns.heatmap(correlation_matrix, linewidths=0.1, square=True, cmap="RdBu")


# ### [wip] unit
# ユニットの数からゲームの状態を求める

# In[4]:


# merge dataset
df_dataset = pd.merge(orders, units, on=['game_id', 'unit_id'])
df_dataset = pd.merge(dataset, players, on=['game_id', 'country'])
df_dataset = pd.merge(dataset, turns, on=['game_id', 'turn_num'])

df_dataset['state'] = 0
df_dataset['eng_state'] = 0
df_dataset['fra_state'] = 0
df_dataset['ita_state'] = 0
df_dataset['rus_state'] = 0
df_dataset['tur_state'] = 0
df_dataset['ger_state'] = 0
df_dataset['aus_state'] = 0

# 補給地6以上ある場合を有利状態として，状態を128通りで定める
df_dataset.loc[df_dataset['scs_england'] > 6, ['eng_state']] = 1
df_dataset.loc[df_dataset['scs_france'] > 6, ['fra_state']] = 1
df_dataset.loc[df_dataset['scs_italy'] > 6, ['ita_state']] = 1
df_dataset.loc[df_dataset['scs_russia'] > 6, ['rus_state']] = 1
df_dataset.loc[df_dataset['scs_turkey'] > 6, ['tur_state']] = 1
df_dataset.loc[df_dataset['scs_germany'] > 6, ['ger_state']] = 1
df_dataset.loc[df_dataset['scs_austria'] > 6, ['aus_state']] = 1

df_dataset['state'] = 64*(df_dataset['eng_state'].values) + 32*(df_dataset['fra_state'].values)+ 16*(df_dataset['ita_state'].values)+ 8*(df_dataset['rus_state'].values) +4*(df_dataset['tur_state'].values) + 2 * (df_dataset['ger_state'].values)+ 1 * (df_dataset['aus_state'].values)
df_dataset.drop(columns=['eng_state', 'fra_state', 'ita_state', 'rus_state', 'tur_state', 'ger_state', 'aus_state'])

# eng_dataset = df_dataset[(df_dataset['country']=='E') & (df_dataset['won']==1)]
eng_dataset = df_dataset[(df_dataset['country']=='E')]
fra_dataset = df_dataset[(df_dataset['country']=='F')]
ita_dataset = df_dataset[(df_dataset['country']=='I')]
rus_dataset = df_dataset[(df_dataset['country']=='R')]
tur_dataset = df_dataset[(df_dataset['country']=='T')]
ger_dataset = df_dataset[(df_dataset['country']=='G')]
aus_dataset = df_dataset[(df_dataset['country']=='A')]


# In[31]:


df_dataset['state'].value_counts()


# In[ ]:


df_dataset.to_csv("some")


# #### MOVE

# In[14]:


# Edinburghからの移動先
data = dataset[(dataset["year"]==1901)
               & (dataset["season"]=="Spring")
               & (dataset["success"]==1) 
               & (dataset["location"]=="Edinburgh") 
               & (dataset["unit_order"]=="MOVE")]
sns.barplot(x="target", y="success", data = data, hue="won", estimator=sum)

