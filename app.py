import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

# @app.route('/predict',methods=['POST'])
# def predict():
#     data=[float(x) for x in request.form.values()]
#     final_input=scalar.transform(np.array(data).reshape(1,-1))
#     print(final_input)
#     output=regmodel.predict(final_input)[0]
#     return render_template("home.html",prediction_text="The House price prediction is {}".format(output))


@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    data = [float(x) for x in request.form.values()]
    # Transform the input data using the scaler
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    # Get the model's prediction
    output = regmodel.predict(final_input)[0]
    # Format the output to 2 decimal places
    output_formatted = f"{output:.2f}"
    # Render the result on the home page
    return render_template("home.html", prediction_text=f"The predicted house price is ${output_formatted}")


# if __name__=="__main__":
#     app.run(debug=True)
    
if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

   
     
