from flask import Flask, render_template, request
from flask import jsonify
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__, template_folder='../templates')
model = pickle.load(open('../model/heart_disease_predict_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Age	 = int(request.form['Age'])
        RestingBP=float(request.form['RestingBP'])
        Cholesterol=int(request.form['Cholesterol'])
        #Kms_Driven2=np.log(Kms_Driven)
        MaxHR=int(request.form['MaxHR'])
        Oldpeak = float(request.form['Oldpeak'])
        Sex_M=request.form['Sex_M']
        if(Sex_M=='M'):
                Sex_M=1
        else:
            Sex_M=0
        ChestPainType=request.form['ChestPainType']
        if(ChestPainType=='ATA'):
            ChestPainType_ATA=1
            ChestPainType_NAP=0
            ChestPainType_TA=0

        elif(ChestPainType== 'NAP'):
            ChestPainType_ATA = 0
            ChestPainType_NAP = 1
            ChestPainType_TA = 0
        elif (ChestPainType == 'TA'):
            ChestPainType_ATA = 0
            ChestPainType_NAP = 0
            ChestPainType_TA = 1
        FastingBS_1=request.form['FastingBS_1']
        if(FastingBS_1==1):
            FastingBS_1=1
        else:
            FastingBS_1=0

        RestingECG = request.form['RestingECG']
        if (RestingECG == 'Normal'):
            RestingECG_Normal = 1
            RestingECG_ST = 0
        elif (RestingECG == 'ST'):
            RestingECG_Normal = 0
            RestingECG_ST = 1

        ExerciseAngina_Y = request.form['ExerciseAngina_Y']
        if (ExerciseAngina_Y == 'Y'):
            ExerciseAngina_Y = 1
        else:
            ExerciseAngina_Y = 0

        ST_Slope_Flat = request.form['ST_Slope_Flat']
        if (ST_Slope_Flat == 'Flat'):
            ST_Slope_Flat = 1
            ST_Slope_Up = 0
        else:
            ST_Slope_Flat = 0
            ST_Slope_Up = 1
        values = np.array([[Age,RestingBP,Cholesterol,MaxHR,Oldpeak,Sex_M,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,FastingBS_1,RestingECG_Normal,\
                                   RestingECG_ST,ExerciseAngina_Y,ST_Slope_Flat,ST_Slope_Up]])
        prediction = model.predict(values)
        output=([prediction[0]])
        if output==[1]:
            return render_template('index.html',prediction_texts="Heart Disease Detected: {}".format(output))
        else:
            return render_template('index.html',prediction_text="No Heart Disease Detected: {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)