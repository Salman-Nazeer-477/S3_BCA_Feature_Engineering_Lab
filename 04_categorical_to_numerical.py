import pandas as pd
data = {
    "Gender" : ["Male", "Female", "Male"]
}
df = pd.DataFrame(data)
df["Gender"] = df["Gender"].map({
    "Male" : 0,
    "Female" : 1
})
print(df)