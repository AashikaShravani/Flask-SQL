from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database of admin credentials
admin_credentials = {'admin': 'password'}

# Mock dashboard data
dashboard_data = {
    'admin': {
        'name': 'Admin User',
        'email': 'admin@example.com',
        'role': 'Administrator',
        'stats': {
            'total_users': 100,
            'total_orders': 500
        }
    }
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in admin_credentials and admin_credentials[username] == password:
        return redirect(url_for('dashboard', username=username))
    else:
        return "Invalid username or password"

@app.route('/dashboard/<username>')
def dashboard(username):
    if username not in dashboard_data:
        return "Unauthorized access"
    return render_template('dashboard.html', user=dashboard_data[username])

if __name__ == '__main__':
    app.run(debug=True)
