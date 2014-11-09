from flask import Flask, request, abort
app = Flask(__name__)
import os
from flask import render_template


@app.route("/list")
def hello():
    try:
        id = int(request.args.get('id', 0))
    except ValueError:
        abort(404)
    rs = os.popen('./seed.sh %d'%id)
    records = rs.read().decode('utf-8').split('\n')
    return render_template('hello.html', records = records)

@app.route("/")
def rmd():
    rs = os.popen('./readkv.py rmd')
    records = rs.read().decode('utf-8').split(';')
    return render_template('hello.html', records = records)
    #return rs.read()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9999)
