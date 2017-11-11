
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dataset.csv')
raw_data = pd.read_table('roundResults.log',sep=':')

raw_data.head()

dataset.head()

now = 0
year = 1901
game_count = 0
D = {"GAME":[], "COUNTRY":[], "YEAR":[], "NAPFLT":[], "GOBFLT":[], "SERAMY":[], "NWYAMY":[], "GASAMY":[], "AEGFLT":[], "TUNAMY":[], "NWYFLT":[], "GASFLT":[], "YORAMY":[], "BUDAMY":[], "ECHFLT":[], "TUNFLT":[], "BALFLT":[], "YORFLT":[], "SILAMY":[], "SEVAMY":[], "STPAMY":[], "SEVFLT":[], "PRUAMY":[], "NTHFLT":[], "TUSAMY":[], "UKRAMY":[], "PRUFLT":[], "TUSFLT":[], "MOSAMY":[], "STPSCS":[], "FINAMY":[], "GOLFLT":[], "WALAMY":[], "SYRAMY":[], "BARFLT":[], "FINFLT":[], "WALFLT":[], "SYRFLT":[], "HELFLT":[], "SWEAMY":[], "BULAMY":[], "PARAMY":[], "BELAMY":[], "APUAMY":[], "SWEFLT":[], "BOHAMY":[], "BELFLT":[], "APUFLT":[], "HOLAMY":[], "BULSCS":[], "VENAMY":[], "STPNCS":[], "VIEAMY":[], "HOLFLT":[], "WARAMY":[], "PICAMY":[], "TYRAMY":[], "VENFLT":[], "ANKAMY":[], "PICFLT":[], "BURAMY":[], "PIEAMY":[], "GREAMY":[], "ANKFLT":[], "TYSFLT":[], "BERAMY":[], "SKAFLT":[], "PIEFLT":[], "CLYAMY":[], "TRIAMY":[], "GREFLT":[], "IONFLT":[], "BERFLT":[], "SPAAMY":[], "CLYFLT":[], "TRIFLT":[], "ADRFLT":[], "ALBAMY":[], "RUHAMY":[], "NWGFLT":[], "SPASCS":[], "ALBFLT":[], "LVNAMY":[], "CONAMY":[], "LVNFLT":[], "PORAMY":[], "LVPAMY":[], "CONFLT":[], "KIEAMY":[], "DENAMY":[], "NAFAMY":[], "BREAMY":[], "SMYAMY":[], "PORFLT":[], "LVPFLT":[], "KIEFLT":[], "WESFLT":[], "DENFLT":[], "NAFFLT":[], "BREFLT":[], "RUMAMY":[], "SMYFLT":[], "ARMAMY":[], "BLAFLT":[], "SPANCS":[], "RUMFLT":[], "EASFLT":[], "MAOAMY":[], "ARMFLT":[], "MAOFLT":[], "IRIFLT":[], "BULECS":[], "MARAMY":[], "ROMAMY":[], "GALAMY":[], "MARFLT":[], "ROMFLT":[], "EDIAMY":[], "EDIFLT":[], "LONAMY":[], "NAPAMY":[], "NAOFLT":[], "MUNAMY":[], "LONFLT":[], "OUTPUT":[]}
for i, v in raw_data.iterrows():
    if v["COUNTRY"].isdigit() == True:
        D["YEAR"] = v["COUNTRY"]
        if v["COUNTRY"] == "1901":
            game_count += 1
    else:
        D["GAME"] = game_count
        D["COUNTRY"] = v["COUNTRY"]
        s = v["ARM"]
        s = s.replace(" ","")
        s = s.replace("[","")
        s = s.replace("]","")
        s = s.split(",")
        for j in s:
            if j in D:
                D[j] = v["COUNTRY"]

        s = v["OWN"]
        s = s.replace(" ","")
        s = s.replace("[","")
        s = s.replace("]","")
        s = s.split(",")
        D["OUTPUT"] = len(s)
        se = pd.Series([D["GAME"], D["COUNTRY"], D["YEAR"], D["NAPFLT"], D["GOBFLT"], D["SERAMY"], D["NWYAMY"], D["GASAMY"], D["AEGFLT"], D["TUNAMY"], D["NWYFLT"], D["GASFLT"], D["YORAMY"], D["BUDAMY"], D["ECHFLT"], D["TUNFLT"], D["BALFLT"], D["YORFLT"], D["SILAMY"], D["SEVAMY"], D["STPAMY"], D["SEVFLT"], D["PRUAMY"], D["NTHFLT"], D["TUSAMY"], D["UKRAMY"], D["PRUFLT"], D["TUSFLT"], D["MOSAMY"], D["STPSCS"], D["FINAMY"], D["GOLFLT"], D["WALAMY"], D["SYRAMY"], D["BARFLT"], D["FINFLT"], D["WALFLT"], D["SYRFLT"], D["HELFLT"], D["SWEAMY"], D["BULAMY"], D["PARAMY"], D["BELAMY"], D["APUAMY"], D["SWEFLT"], D["BOHAMY"], D["BELFLT"], D["APUFLT"], D["HOLAMY"], D["BULSCS"], D["VENAMY"], D["STPNCS"], D["VIEAMY"], D["HOLFLT"], D["WARAMY"], D["PICAMY"], D["TYRAMY"], D["VENFLT"], D["ANKAMY"], D["PICFLT"], D["BURAMY"], D["PIEAMY"], D["GREAMY"], D["ANKFLT"], D["TYSFLT"], D["BERAMY"], D["SKAFLT"], D["PIEFLT"], D["CLYAMY"], D["TRIAMY"], D["GREFLT"], D["IONFLT"], D["BERFLT"], D["SPAAMY"], D["CLYFLT"], D["TRIFLT"], D["ADRFLT"], D["ALBAMY"], D["RUHAMY"], D["NWGFLT"], D["SPASCS"], D["ALBFLT"], D["LVNAMY"], D["CONAMY"], D["LVNFLT"], D["PORAMY"], D["LVPAMY"], D["CONFLT"], D["KIEAMY"], D["DENAMY"], D["NAFAMY"], D["BREAMY"], D["SMYAMY"], D["PORFLT"], D["LVPFLT"], D["KIEFLT"], D["WESFLT"], D["DENFLT"], D["NAFFLT"], D["BREFLT"], D["RUMAMY"], D["SMYFLT"], D["ARMAMY"], D["BLAFLT"], D["SPANCS"], D["RUMFLT"], D["EASFLT"], D["MAOAMY"], D["ARMFLT"], D["MAOFLT"], D["IRIFLT"], D["BULECS"], D["MARAMY"], D["ROMAMY"], D["GALAMY"], D["MARFLT"], D["ROMFLT"], D["EDIAMY"], D["EDIFLT"], D["LONAMY"], D["NAPAMY"], D["NAOFLT"], D["MUNAMY"], D["LONFLT"], D["OUTPUT"]], index = dataset.columns)
        dataset = dataset.append(se,ignore_index=True)                

dataset = dataset.fillna(0) #欠損値を0で穴埋め
dataset.head()

dataset.to_csv("employee.csv")


