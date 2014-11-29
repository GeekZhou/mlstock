#coding=utf-8
from flask import Flask, g, request, make_response, abort
app = Flask(__name__)
import os
from flask import render_template
import hashlib 
import xmltodict as xd

@app.route('/stock', methods = ['GET', 'POST'] )  
def wechat_auth():  
    if request.method == 'GET':  
        token = 'juzi' # your token  
        query = request.args  
        signature = query.get('signature', '')  
        timestamp = query.get('timestamp', '')  
        nonce = query.get('nonce', '')  
        echostr = query.get('echostr', '')  
        s = [timestamp, nonce, token]  
        s.sort()  
        s = ''.join(s)  
        print s
        if ( hashlib.sha1(s).hexdigest() == signature ):    
            return make_response(echostr)  
    wxreq = xd.parse(request.data).get('xml')
    try:
        id = int(wxreq.get('Content','0'))
        rs = os.popen('/root/mlstock/seed.sh %d'%id)
        records = rs.read().decode('utf-8')
    except:
        records = u"请输入股票代码"
    if not records:
        records = u"请输入股票代码"

#    print records
    res = {
            'xml': {
                'ToUserName': wxreq.get('FromUserName'),
                'FromUserName': wxreq.get('ToUserName'),
                'CreateTime': wxreq.get('CreateTime'),
                'MsgType': 'text',
                'Content': records,
                'MsgId': wxreq.get('MsgId'),
                }
            }
    return make_response(xd.unparse(res))





@app.route("/stock/weixin")
def welist():
    print "fuck"
    f = open("log", "a+")
    f.write("debug\n")
    f.write(request.data)
    f.close()
    wxreq = xd.parse(request.data).get('xml')
    f.write(str(wxreq))
    res = {
            'xml': {
                'ToUserName': wxreq.get('FromUserName'),
                'FromUserName': wxreq.get('ToUserName'),
                'CreateTime': wxreq.get('CreateTime'),
                'MsgType': 'text',
                'Content': wxreq.get('Content'),
                'MsgId': wxreq.get('MsgId'),
                }
            }
    return HttpResponse(xd.unparse(res))



@app.route("/stock/list")
def list():
    try:
        id = int(request.args.get('id', 0))
    except ValueError:
        sys.stderr.write("error, %d"%id)
        abort(404)
    rs = os.popen('/root/mlstock/seed.sh %d'%id)
    records = rs.read().decode('utf-8').split('\n')
    return render_template('hello.html', records = records)

@app.route("/stock/rmd")
def rmd():
    rs = os.popen('/root/mlstock/readkv.py rmd')
    records = rs.read().decode('utf-8').split(';')
    return render_template('hello.html', records = records)
#return rs.read()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
