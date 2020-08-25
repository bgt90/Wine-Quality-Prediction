#dashboard for predict target

from flask import Flask, render_template, request
import joblib

app= Flask(__name__)

#halaman home
@app.route('/')

def home():
    return render_template('home.html')

#halaman dataset
@app.route('/database',methods=['POST','GET'])
def dataset():
    return render_template('dataset.html')

#halaman visualisasi
@app.route('/visualize',methods=['POST','GET'])
def visual():
    return render_template('plot.html')

#halaman input prediksi
@app.route('/predict',methods=['POST','GET'])
def predict():
    return render_template('predict.html')

#halaman hasil prediksi
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        input = request.form
        prediksi= model.predict([[
            float(input['fa']), 
            float(input['va']), 
            float(input['ca']), 
            float(input['rs']),
            float(input['c']),
            float(input['fsd']),
            float(input['tsd']),
            float(input['d']),
            float(input['ph']),
            float(input['s']),
            float(input['a']),
            ]])[0]
        return render_template('result.html', data= input, pred=round(prediksi,0))


if __name__=='__main__':
    model= joblib.load('modelRidge')
    app.run(debug=True)