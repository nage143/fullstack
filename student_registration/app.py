from flask import Flask, render_template, request, redirect
from repository.student_repository import insert_student, fetch_students

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = (
            request.form['name'],
            request.form['email'],
            request.form['dob'],
            request.form['department'],
            request.form['phone']
        )
        insert_student(data)
        return redirect('/students')
    return render_template('register.html')

@app.route('/students')
def students():
    data = fetch_students()
    return render_template('students.html', students=data)

if __name__ == '__main__':
    app.run(debug=True)
