print(diabetes.columns)
for column in diabetes.columns:
    print('Mean and Standard Dev for ', column,' levels by Outcome')
    print('Mean:')
    print(diabetes.groupby('Outcome')[column].mean())
    print('Standard Dev:')
    print(diabetes.groupby('Outcome')[column].std())
    print("="*30)