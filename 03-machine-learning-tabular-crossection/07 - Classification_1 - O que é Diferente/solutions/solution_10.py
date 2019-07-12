diabetes_data_copy_0 = diabetes_data_copy[diabetes_data_copy.Outcome==0]
diabetes_data_copy_1 = diabetes_data_copy[diabetes_data_copy.Outcome==1]
diabetes_data_copy_0 = diabetes_data_copy_0.sample(n=268, replace=True)
diabetes_data_copy = pd.concat([diabetes_data_copy, diabetes_data_copy_1], ignore_index=True)