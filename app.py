# -*- coding:utf-8 -*-


from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/arbitrage', methods=['GET','POST'])
def arbitrage():
    if request.method == 'POST':
        results = request.form
        return render_template("results.html",result=results)
    return render_template("arbitrage.html")
if __name__ == '__main__':

    app.run(host="0.0.0.0" , port=5000 )