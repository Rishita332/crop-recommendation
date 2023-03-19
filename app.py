
from flask import Flask, render_template, request
import joblib

# load the trained model
model = joblib.load("RandomForest.pkl")

# create Flask app
app = Flask(__name__)

# define route for index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get form data
        nitrogen = float(request.form['Nitrogen'])
        potassium = float(request.form['Potassium'])
        phosphorus = float(request.form['Phosphorus'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])
        temperature = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])

        # make prediction
        prediction = model.predict([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

        # get the crop name
        crop = prediction[0]

        return render_template('crop.html', prediction_text=f'The most suitable crop to grow in your farm is {crop}')
    else:
        return render_template('crop.html')

# run the app
if __name__ == '__main__':
    app.run(debug=True)