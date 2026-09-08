import pandas as pd
data = {
    "Math" : [80, 70, 90],
    "Science" : [75, 85, 95]
}
df = pd.DataFrame(data)
df["Total"] = df["Math"] + df["Science"]
print(df)