from flask import Flask, render_template, request
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load trained model and scaler
model = pickle.load(open('best_rf_model.pkl', 'rb'))
scaler = pickle.load(open('ss.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        year = int(request.form['year'])
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        fuel_type = int(request.form['fuel_type'])
        seller_type = int(request.form['seller_type'])
        transmission = int(request.form['transmission'])
        owner = int(request.form['owner'])

        # Arrange input in same order as training data
        input_data = np.array([[year,
                                present_price,
                                kms_driven,
                                fuel_type,
                                seller_type,
                                transmission,
                                owner]])

        # Scale the input
        scaled_input = scaler.transform(input_data)

        # Predict price
        prediction = model.predict(scaled_input)[0]

        prediction = round(prediction, 2)

        return render_template(
            'index.html',
            prediction_text=f"Estimated Selling Price: ₹ {prediction} Lakhs"
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
