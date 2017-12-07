import flask
from flask import Flask, request
import hashlib
app = Flask(__name__)

TOKEN = "ATGUOHAELKiubahiughaerGOJAEGj"
@app.route("/")
def index():
    return  "Hello world"

@app.route('/validate', methods=['GET'])
def validate():
    # 微信加密签名，signature结合了开发者填写的token参数和请求中的timestamp参数、nonce参数。
    signature = request.args.get('signature')
    # 时间戳
    timestamp = request.args.get('timestamp')
    # 随机数
    nonce = request.args.get('nonce')
    # 随机字符串
    echostr = request.args.get('echostr')

    token = TOKEN
    if validate_signature(token=token, signature=signature, timestamp=timestamp, nonce=nonce):
        return echostr
    return False


def validate_signature(token, signature, timestamp, nonce):
    # 检验signature
    # 1）将token、timestamp、nonce三个参数进行字典序排序
    # sorted([token, timestamp, nonce])
    # 2）将三个参数字符串拼接成一个字符串进行sha1加密
    # "".join()
    # hashlib.sha1().hexdigest()
    # 3）开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    if hashlib.sha1(''.join(sorted([token, timestamp, nonce]))).hexdigest() == signature:
        return True
    return False