import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import pickle

#Load CSV file
data = pd.read_csv("Admission_Predict_Ver1.1.csv")

#Drop the serial no column
df = data.drop("Serial No.",axis=1)

#Storing feature matrix in X and y
X = df.drop('Chance of Admit ',axis=1)
y = df['Chance of Admit ']

#Splitting train and test data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)



#Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Converting target variable from continuous variable to categorical variable
y_train=[1 if value>0.8 else 0 for value in y_train]
y_test= [1 if value>0.8 else 0 for value in y_test]

#Initialize the model
gbc=GradientBoostingClassifier()

#Training Model
gbc.fit(X_train,y_train)

#Make pickle file of our model and saving it.
pickle.dump(gbc,open("model.pkl","wb"))
