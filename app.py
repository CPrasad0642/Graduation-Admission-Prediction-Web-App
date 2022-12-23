from flask import Flask, render_template,request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

app  = Flask(__name__)

#Load the pickle model
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET','post'])
def predict():
    GRE_Score = int(request.form['GRE Score'])
    TOEFL_Score = int(request.form['TOEFL Score'])
    University_Rating = int(request.form['University Rating'])
    SOP = float(request.form['SOP'])
    LOR = float(request.form['LOR'])
    CGPA = float(request.form['CGPA'])
    Research = float(request.form['Research'])
    
    data = pd.read_csv("Admission_Predict_Ver1.1.csv")
    df = data.drop("Serial No.",axis=1)
    X = df.drop('Chance of Admit ',axis=1)
    y = df['Chance of Admit ']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    final_features = pd.DataFrame(sc.transform([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]]))
    
    predict = model.predict(final_features)
    
    output = predict[0]
    
    if output==1:
        output = "You have a Chance Of Admission"
    else:
        output = "You do not have a Chance of Admission"
    
    return render_template('index.html',result=output)
    
if __name__ == "__main__":
    app.run(debug=True)
    