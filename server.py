from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "i am not sure"

@app.route('/')
def test():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def test2():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)