from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = []


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # basic duplicate check
        for user in users:
            if user.get('email') == email:
                return 'User already exists', 400

        users.append({'email': email, 'password': password})
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        for user in users:
            if (user.get('email') == email) and (user.get('password') == password):
                return render_template('home.html', email=email)

        return 'Invalid credentials', 401

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)