import pandas as pd

status_group = ["functional", "non functional", "functional needs repair"]
submission=pd.read_csv("submission1.csv")
for i in range(len(status_group)):
	submission.loc[submission["status_group"] == i, "status_group"] = status_group[i]
print("Dataframe as per submission format: successfully")
submission.to_csv("submissionDD.csv",index=False)
