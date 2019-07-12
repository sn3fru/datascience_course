aggr_df = df.groupby('published')[['url']].count()
aggr_df.columns = ['posts']