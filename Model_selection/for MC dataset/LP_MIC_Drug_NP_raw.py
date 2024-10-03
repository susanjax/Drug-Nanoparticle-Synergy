import pandas as pd
from lazypredict.Supervised import LazyRegressor
from Models import data_transform
from sklearn.model_selection import train_test_split

df_MIC_Drug_NP = pd.read_csv(r'C:\Users\user\Desktop\Synergy_project_2024\data\raw\separate_datasets\synergy_MC_Drug_NP_data.csv')

df_model = df_MIC_Drug_NP.drop_duplicates()
df_model.reset_index(drop= True)
df_x = df_model.drop(['MIC_drug_NP (μg/ml)'], axis=1)
df_y = df_model[['MIC_drug_NP (μg/ml)']].copy()
df_scaled, le_dict, scaler  = data_transform.df_fit_transformer(df_x)
df_scaled.info()

X_train, X_test, Y_train, Y_test = train_test_split(df_scaled, df_y, test_size=0.2, random_state = 42)
clf = LazyRegressor(verbose=0,ignore_warnings=True, custom_metric=None)
train,test = clf.fit(X_train, X_test, Y_train, Y_test)

train_mod = train.iloc[:-0, :]
test.to_csv('Model_comparision_raw_MIC_drug_NP.csv')
print(train)