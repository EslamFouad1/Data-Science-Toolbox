# Target variable "Class"

#Split values
x = training_df.iloc[:, 0: -1]
y = training_df.iloc[:, -1]

# Use the smote method and SMOTE is special library that will be assisting us in making dataset balanced.¶
from imblearn.over_sampling import SMOTE
smt = SMOTE()
trainx, trainy=smt.fit_resample(x,y)

#Use standard scaler for stndardizing the data
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

X=scaler.fit_transform(trainx)
X
