from flask import Flask, request, abort
app = Flask(__name__)
import os

@app.route("/")
def hello():
    try:
        id = int(request.args.get('id', 0))
    except ValueError:
        abort(404)
    rs = os.popen('./seed.sh %d'%id)
    return rs.read()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
