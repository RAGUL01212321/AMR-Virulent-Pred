from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/amr', methods=['GET', 'POST'])
def amr_page():
    if request.method == 'POST':
        # Handle uploaded file or sequence
        file = request.files.get('file')
        sequence = request.form.get('sequence')
        
        # Placeholder logic
        result = "Prediction results coming soon!"
        return render_template('amr.html', result=result)
    
    return render_template('amr.html')  # Just show the form on GET

@app.route('/virulence')
def virulence_page():
    return "Protein Virulence Page Coming Soon!"

if __name__ == "__main__":
    app.run(debug=True)
