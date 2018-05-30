
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

games = pd.read_csv("../data/games.csv")
units = pd.read_csv("../data/units.csv")
orders = pd.read_csv("../data/orders.csv")
turns = pd.read_csv("../data/turns.csv")
players = pd.read_csv("../data/players.csv")

# merge df_dataset
df_dataset = pd.merge(orders, units, on=['game_id', 'unit_id'])
df_dataset = pd.merge(df_dataset, players, on=['game_id', 'country'])
df_dataset = pd.merge(df_dataset, turns, on=['game_id', 'turn_num'])

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

# eng_df_dataset = df_dataset[(df_dataset['country']=='E') & (df_dataset['won']==1)]
eng_df_dataset = df_dataset[(df_dataset['country']=='E')]
fra_df_dataset = df_dataset[(df_dataset['country']=='F')]
ita_df_dataset = df_dataset[(df_dataset['country']=='I')]
rus_df_dataset = df_dataset[(df_dataset['country']=='R')]
tur_df_dataset = df_dataset[(df_dataset['country']=='T')]
ger_df_dataset = df_dataset[(df_dataset['country']=='G')]
aus_df_dataset = df_dataset[(df_dataset['country']=='A')]

tyear = df_dataset["year"].unique()
tseason = df_dataset["season"].unique()
tcountry = df_dataset["country"].unique()
tlocation = df_dataset["location"].unique()
tstate = df_dataset["state"].unique()
tunit_order = ["MOVE", "HOLD", "SUPPORT"] #df_dataset["unit_order"].unique()


# In[ ]:


df_new = pd.DataFrame(columns=["in","out1","out2"])


# In[ ]:


# 特定の条件におけるデータ抽出
i = 0
for xyear in tyear:
    for xseason in tseason:
        for xcountry in tcountry:
            for xstate in tstate:
                data = df_dataset[(df_dataset["year"]==xyear)
                    & (df_dataset["season"]==xseason)
                    & (df_dataset["success"]==1)
                    & (df_dataset["country"]==xcountry)
                    & (df_dataset["state"]==xstate)]
                # データ抽出の際の条件
                inputs = str(xyear) + str(xseason) + str(xcountry)+ str(xstate)# + str(xunit_order)
                print(inputs)

                # 行動と勝率を求める
                out1 = data[(data["won"]==1)]["location"].value_counts()
                out2 = data["location"].value_counts()
                df2 = pd.DataFrame({'in': [inputs], 'out1': [out1], 'out2':[out2]})
                df_new = df_new.append(df2)
    if xyear > 1920:
        break;

df_new.to_csv("df_dataset.csv")
