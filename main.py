import pandas as pd
df = pd.read_csv("applications.csv")

shortlisted = df[
    (df["CGPA"] >= 8.0) &
    (df["Skills"].str.contains("Python", na=False)) &
    (df["Availability"] == "Full-time")
]

print("Shortlisted Candidates:")
print(shortlisted)

shortlisted.to_csv("shortlisted.csv", index=False)

incomplete = df[df.isnull().any(axis=1)]

print("\nIncomplete Applications:")
print(incomplete)

incomplete.to_csv("incomplete.csv", index=False)

duplicates = df[df.duplicated(subset="Email", keep=False)]

print("\nDuplicate Applications:")
print(duplicates)

duplicates.to_csv("duplicates.csv", index=False)


print("\nAll files generated successfully ✅")

