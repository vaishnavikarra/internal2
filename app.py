from flask import Flask,render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/submit',methods=['POST'])
def submit():
    uname=request.form.get('uname')
    email=request.form.get('email')
    year=request.form.get('year')

    return render_template('result.html',name=uname,email=email,year=year)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port="5001",debug=True)