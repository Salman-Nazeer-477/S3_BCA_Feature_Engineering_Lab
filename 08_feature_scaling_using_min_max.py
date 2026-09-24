import pandas as pd
data = {
    "height" : [150, 160, 170, 180, 190],
    "weight" : [50, 65, 75, 85, 100] 
}
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

df["height"] = (df["height"] - df["height"].min()) / (df["height"].max() - df["height"].min())
print("\nNormalized Dataset:") 
print(df) 