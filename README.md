# Graduation Admission Prediction Web App
Graduation Amission Prediction is used to predict the chance of admission using the GRE Score, TOEFL Score, University Rating, SOP, LOR Rating, CGPA, Research which will predict the chance of Admission.

:pushpin:**Data set Used :**

* The data set was Obtained from Kaggle Datasets.
* The dataset contains 500 Records with 6 attributes.
* Attributes of the Dataset are :
    * GRE Score  (Ranging from 290 to 340)
    * TOEFL Score  (Ranging from 90 to 120)
    * University Rating  (Ranging from 1 to 5)
    * SOP Rating  (Ranging from 1 to 5)
    * LOR Rating  (Ranging from 1 to 5)
    * CGPA  (Ranging from 6.8 to 9.92)
    * Research  (0/1)
    * Chance of Admit  (Ranging from 0.34 to 0.97)

:pushpin:**Flowchart :**

![fc](https://user-images.githubusercontent.com/67002556/209352481-e26effb4-002c-4d7a-97a9-b66977a98a4e.png)

:pushpin:**Implementation :**
  
  ***1. IMPORTING LIBRARIES AND DATA SET :***
  
  * Data Set is being imported which consists of 8 features and 500 Records of data.
  * Dataset is of .CSV format which read using a read_csv function which is available in the Pandas Library.
  * All the Necessary Python Modules and Libraries such as sklearn, NumPy, Pandas will be imported.
 
 ***2. DATA ANALYSIS  :***
 
   * Checking Null Values in the dataset if there is any Null Values is present in the data set then Data Cleaning is performed
   * Checking info of the Dataset i.e., No of columns and type of columns present in the dataset.
   * Statistics of the data present in the dataset is being calculated using describe function in pandas Library

 ***3. DATA VIUSALIZATION  :***
 
   * For all the features of a dataset, visualization has been done to understand the data and to identify any outliers present in the data set.
   * Histograms for all features present in the dataset  had plotted using the hist function available in matplot library.
   
   ![image](https://user-images.githubusercontent.com/67002556/219555734-bc37541c-be3f-4b58-bb63-2b558a503c50.png)

***4. DATA PREPROCESSING  :***

   * In Data Pre processing stage, Feature Scaling will be performed.
   * Feature Scaling is necessary for this data since the features that are GRE Score, TOEFL Score have a greater values than other values such as SOP Rating, LOR      Rating, University Rating and CGPA.
   * So, Feature Scaling is done to convert all the values into the same range so as to avoid the dominance of the variables while prediction.
   * Featuring Scaling is done using Standard Scaler
   
![image](https://user-images.githubusercontent.com/67002556/219556455-cd159cb7-b8fe-4b02-859b-60ed5553c6e8.png)

***5. MODELLING AND EVALUATION :***

   **1. Random Forest Classifier:**
   
   * Random Forest  is a powerful and versatile supervised machine learning algorithm that  grows and combine multiple decision trees.
   * The greater number of trees in the forest leads to the higher accuracy and prevents the problem the problem of overfitting.
   
   **2. Gradient Boosting Classifier:**
   
   * Gradient Boosting is a popular boosting algorithm. In gradient boosting, each predictor corrects its predecessor’s error.
   * GBC help us to combine the predictions from various learner models and build a final predictive model having the correct prediction. 
   
   ![image](https://user-images.githubusercontent.com/67002556/219557289-4f8967f1-929b-452a-afec-57b2354e8d24.png)
   
   * Among Random Forest and Gradient Boost Classifiers, the Gradient Boosting classifier have more accuracy score so, we use it for the prediction.

***6. PREDICTION OF DATA :***
   
   * Prediction of data Using the Gradient Boosting Classifier is implemented by taking the GRE Score, TOEFL Score, University Rating, SOP, LOR Rating, Research that gives output 0/1 which is having a chance for admission or not.
   
   ![image](https://user-images.githubusercontent.com/67002556/219557856-d69c0010-a211-401a-824a-ffa53c47c101.png)
   
***7. FLASK IMPLEMENTATION :***

   * Web Page is created using HTML and CSS and it is linked to Machine Learning model using Flask module.
   * The Webpage has a form that takes input values and it will give output as “You have chance of Admission” or “You don’t have a chance of Admission”.
   
   ![image](https://user-images.githubusercontent.com/67002556/219558032-09044bb5-c25a-4295-9080-965052928ad4.png)
   

:pushpin:**Conclusion :**

   * Graduation admission prediction will help the student to know whether he has a possibility of getting a chance in the graduation using their GRE Score, TOEFL score , University Rating, SOP Rating, LOR Rating, GPA, Research. In this Project the user can give the input values of attributes through the form of the webpage and it displays output as “You have a Chance of Admission” or “You do not have a chance of Admission” i.e., Having chance for the admission in the Graduation or not.

__ This project done by the prasad Reddy.





