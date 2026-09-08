import pandas as pd
data = {
    "Age" : [20, None, 30]
}
df = pd.DataFrame(data)
print(df)
print("\n")
df["Age"] = df["Age"].fillna(0)
print(df)