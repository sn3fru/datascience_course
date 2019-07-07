daily_df = aggr_df.resample('D').apply(sum)
daily_df.head(n=3)