import pandas as pd
data = {
    "name" : ["John", "Anna", "Nino", "Invalid Name 123", "Charlie", ""],
    "gender" : ["Male", "Female", "Male", "Unknown", "Male", "Female"],
    "age" : [23, 25, -1, 30, 22, 180]
}

df = pd.DataFrame(data)

print("Original DataFrame with invalid data entries:")
print(df)
df = df[df['name'].apply(lambda x: isinstance(x, str) and x.isalpha())] 
df = df[df['gender'].isin(['Male', 'Female'])] 
df = df[(df['age'] >= 0) & (df['age'] <= 120)] 
print("\nCleaned DataFrame after removing invalid entries:") 
print(df)