import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={
    "names":["Rahma","Amine","eya","Sami","Salma","Karim"],
    "math":[13,6,10,8.5,11.75,16],
    "arabe":[17,11,12.5,7,9.5,14],
    "francais":[5,11,18,8,15,12.25]
}
df=pd.DataFrame(data)

print("std math :",df["math"].std())
print("std arabe :",df["arabe"].std())
print("std francais :",df["francais"].std())

print("moyenne math:",df["math"].mean())
print("moyenne arabe:",df["arabe"].mean())
print("moyenne francais:",df["francais"].mean())

print("max math",df["math"].max())
print("min math",df["math"].min())

print("max arabe",df["arabe"].max())
print("min arabe",df["arabe"].min())

print("max francais",df["francais"].max())
print("min francais",df["francais"].min())

df["moyenne"]=df[["math","arabe","francais"]].mean(axis=1)

df["result"]=df["moyenne"].apply(lambda x :"admis" if x>=10 else "refusé")

best=df.loc[df["moyenne"].idxmax()]
print(df)
df.to_csv("data.csv",index=False)
print(best)

plt.bar(df["names"],df["moyenne"])
x=np.arange(len(df["moyenne"]))
for i in range(len(df["moyenne"])):
    plt.text(x[i],df["moyenne"][i]+0.2,f"{df["moyenne"][i]:.2f}",ha='center')
plt.title("les resultats du concours")
plt.xlabel("names")
plt.ylabel("moyenne")
plt.show()