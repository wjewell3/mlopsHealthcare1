# 1-hot encode source data

import pandas as pd
import numpy as np
df = pd.read_csv('data/1_source/diabetic_data.csv')
df['readmitted'] = np.where(df.readmitted=='<30',1,0)
features = [i for i in df.columns if i!='readmitted']
encoded_df = pd.get_dummies(df.loc[:,features])