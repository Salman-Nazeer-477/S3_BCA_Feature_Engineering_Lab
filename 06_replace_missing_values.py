import pandas as pd
data = {
    "age" : [23, 25, None, 28, 22, None],
    "height" : [5.5, 5.8, 5.6, None, 5.9, 5.7],
    "weight" : [70, 80, None, 60, 65, None],
    "grade" : ["A", "B", "C", "A", None, "B"]
}
df = pd.DataFrame(data)
print("Original Dataframe with missing values:")
print(df)

print("\nColumns with missing values:")
print(df.isnull().sum())

df["age"].fillna(df["age"].mean(), inplace=True)
df["height"].fillna(df["height"].median(), inplace = True)
df["weight"].fillna(df["weight"].mean(), inplace = True)
df["grade"].fillna(df["grade"].mode()[0], inplace = True)

print("\nDataFrame after missing values:")
print(df)