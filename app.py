from flask import Flask, render_template, request
from model_utils import predict_amr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/amr', methods=['GET'])
def amr_page():
    return render_template('amr.html')

@app.route('/amr_result', methods=['POST'])
def amr_result():
    sequence = request.form.get('sequence', '')
    if not sequence:
        return render_template('amr_result.html', prediction="No sequence provided.")
    
    result = predict_amr(sequence)
    return render_template('amr_result.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
