from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Create folders if they don't exist
os.makedirs('uploads/homeworks', exist_ok=True)
os.makedirs('uploads/submissions', exist_ok=True)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/teacher', methods=['GET', 'POST'])
def teacher_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads/homeworks', filename))
            return redirect(url_for('home'))
    return render_template('teacher_upload.html')

@app.route('/student', methods=['GET', 'POST'])
def student_submit():
    if request.method == 'POST':
        student_name = request.form['name']
        file = request.files['file']
        if file:
            filename = secure_filename(student_name + '_' + file.filename)
            file.save(os.path.join('uploads/submissions', filename))
            return redirect(url_for('home'))
    return render_template('student_submit.html')

if __name__ == '__main__':
    app.run(debug=True)
