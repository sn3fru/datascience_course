from sklearn.preprocessing import StandardScaler

stscaler = StandardScaler().fit(df)
df = stscaler.transform(df)