import pandas as pd
data = {
    "Marks" : [40, 75, 90]
}
df = pd.DataFrame(data)
df["Result"] = ["Fail", "Pass", "Pass"]
print(df)