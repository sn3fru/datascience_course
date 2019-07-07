
df = daily_df.reset_index()
df.columns = ['ds', 'y']
df.tail(n=3)