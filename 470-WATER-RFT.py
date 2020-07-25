import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, train_test_split

def combine(df_id,df_train,df2_train):
    df = df_train
    df2 = df2_train
    c02=0
    c20=0
    c12=0
    c21=0
    c10=0
    c01=0
    if df.shape[0] == df2.shape[0]:
        print("boyutlar uygun")
    else:
        print("error")
    y_pred = []
    for i in range(0, df.shape[0]):
        if (df[i] == df2[i]):
            y_pred.append(df[i])
        elif (df[i] == 0 and df2[i] == 1):
            y_pred.append(0)
            c01=c01+1
        elif (df[i] == 1 and df2[i] == 0):
            y_pred.append(1)
            c10=c10+1
        elif (df[i] == 2 and df2[i] == 1):
            y_pred.append(1)
            c21=c21+1
        elif (df[i] == 1 and df2[i] == 2):
            y_pred.append(1)
            c12=c12+1
        elif (df[i] == 0 and df2[i] == 2):
            y_pred.append(0)
            c02=c02+1
        elif (df[i] == 2 and df2[i] == 0):
            y_pred.append(0)
            c20=c20+1

    print("c02",c02," c20",c20," c12",c12," c21",c21," c01",c01," c10",c10)
    submission = pd.DataFrame({
        "id": df_id,
        "status_group": y_pred
    })
    submission.to_csv("submission1.csv",index=False)


df=pd.read_csv("train_value470.csv")
dfY=pd.read_csv("train_label470.csv")

status_group = ["functional", "non functional", "functional needs repair"]
features = list(df.columns)

features.remove("id")
features.remove("date_recorded")
dfY=dfY['status_group']

df=df[features]

df_test=pd.read_csv("test_value470.csv")
df_id=df_test["id"]


f= df["waterpoint_type"]
f1=df["water_quality"]
f2=f1*f
df["f"]=f
df["f1"]=f1
df["f2"]=f2
features.append("f")
features.append("f1")
features.append("f2")

ftest=df_test["waterpoint_type"]
ftest1=df_test["water_quality"]
ftest2=ftest*ftest1


df_test["f"]=ftest
df_test["f1"]=ftest1
df_test["f2"]=ftest2


tree=RandomForestClassifier(n_estimators=200,n_jobs=-1)
tree.fit(df,dfY)
y_pred=tree.predict(df_test[features])
#scores = cross_val_score(tree, df, dfY, cv=5)


#print("RandomForest: ",scores,scores.mean())


model = XGBClassifier()
model.fit(df,dfY)
y_pred2=model.predict(df_test[features])
#scores2=cross_val_score(model, df, dfY, cv=5)

#print("XGBClassifier:",scores2,scores2.mean())
combine(df_id,y_pred,y_pred2)

"""
submission=[]
submission = pd.DataFrame({
        "id": df_id,
        "status_group": y_pred
    })
submission.to_csv("submission1.csv",index=False)
"""




