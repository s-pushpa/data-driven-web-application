from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('home.html')

@app.route('/beverage')
def beverage():
  return render_template('beverage.html')

@app.route('/salads')
def salads():
  return render_template('salads.html')

@app.route('/pastas')
def pastas():
  return render_template('pastas.html')

@app.route('/steaks')
def steaks():
  return render_template('steaks.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']
        
        # Perform validation and authentication logic here
        # For example, check if the username and password are correct
        
        # Redirect to the home page after successful login
        return redirect('/')
    
    return render_template('login.html')










if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)