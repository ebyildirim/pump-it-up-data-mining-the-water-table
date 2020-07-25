import pandas as pd
import numpy as np

train_value = pd.read_csv("X_train.csv")
test=pd.read_csv("X_test.csv")

features = list(train_value.columns.values)
constant_columns=[]

features.remove("public_meeting") #after p test 0.05
constant_columns.append("public_meeting")
features.remove("recorded_by") #after p test 0.05
constant_columns.append("recorded_by")

features.remove("scheme_name") #too many missing value
features.remove("num_private") # ?

constant_columns.append("scheme_name")
constant_columns.append("num_private")

features.remove("payment_type") #similar with payment
constant_columns.append("payment_type")

features.remove("wpt_name") #too many unique  values
constant_columns.append("wpt_name")

features.remove("extraction_type_group") #similar with extraction_type_class
features.remove("extraction_type")

constant_columns.append("extraction_type_group")
constant_columns.append("extraction_type")

features.remove("district_code")  #Long and lat should be sufficient to account for location.
features.remove("region")
features.remove("region_code")
features.remove("subvillage")
features.remove("ward")

constant_columns.append("district_code")
constant_columns.append("region")
constant_columns.append("region_code")
constant_columns.append("subvillage")
constant_columns.append("ward")

features.remove("installer") #too many unique values
constant_columns.append("installer")

features.remove("waterpoint_type_group") #similiar with waterpoint_type
constant_columns.append("waterpoint_type_group")

features.remove("quantity_group") #duplicate of quantitiy
constant_columns.append("quantity_group")

train_value.drop(labels=constant_columns, axis=1, inplace=True)
test.drop(labels=constant_columns, axis=1, inplace=True)


features.remove("id")
features.remove("amount_tsh")
features.remove("date_recorded")
features.remove("gps_height")
features.remove("longitude")
features.remove("latitude")
features.remove("population")
features.remove("construction_year")



for i in features:
	unique_value = list(set(np.concatenate((train_value[i].unique() , test[i].unique()))))
	print(unique_value)
	size = len(unique_value)
	for j in range(size):
		if unique_value[j] != "nan":
			train_value.loc[train_value[i] == unique_value[j], i] = j
			test.loc[test[i] == unique_value[j], i] = j

train_value = train_value.fillna(train_value.median())
test = test.fillna(test.median())

train_value.to_csv("train_value470.csv", index = False)
test.to_csv("test_value470.csv", index = False)
