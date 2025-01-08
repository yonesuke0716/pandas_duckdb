import os
import pandas as pd
from sklearn.datasets import load_diabetes
from tqdm import tqdm

diabetes = load_diabetes()
diabetes_data = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
diabetes_data["target"] = diabetes.target
# 約104万行、11列
for i in tqdm(range(13)):
    diabetes_data = pd.concat([diabetes_data, diabetes_data], axis=0)
diabetes_data = diabetes_data.reset_index(drop=True)

os.makedirs("csv", exist_ok=True)
diabetes_data.to_csv("csv/diabetes_data.csv", index=False)
