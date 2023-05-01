import pandas
df = pandas.read_csv("brightest_stars.csv")
df = df.dropna()
df = df.drop_duplicates()

for i in range(len(df)):
    try:
        df["radius"][i] *= 0.102763
        df["mass"][i] *= 0.000954588
    except:
        continue

df.to_csv("brightest_stars_formatted.csv", index=False)

del df

df = pandas.read_csv("brown_dwarfs.csv")
df = df.dropna()
df = df.drop_duplicates()

for i in range(len(df)):
    try:
        df["radius"][i] *= 0.102763
        df["mass"][i] *= 0.000954588
    except:
        continue

df.to_csv("brown_dwarfs_formatted.csv", index=False)
