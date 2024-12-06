# mlopsHealthcare1

Data from:
https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008

Objective:
Predict 30 day readmission for diabetes patients with meds and labs and LOS>14 days

Steps:
0. Data prep (One-hot encode features)
1. k-folds cross validation for training/validation on first 2 years
2. Test model on remaining 8 years, with threshold for performance re-evaluation
3. If model performance dips, re-train and re-deploy