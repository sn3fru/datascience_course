del wine_a['Unnamed: 0']
wine_a.rename(
    columns={
        'fixed.acidity':'fixed_acidity',
        'volatile.acidity':'volatile_acidity',
        'citric.acid':'citric_acid',
        'residual.sugar':'residual_sugar',
        'free.sulfur.dioxide':'free_sulfur_dioxide',
        'total.sulfur.dioxide':'total_sulfur_dioxide'},
    inplace=True)