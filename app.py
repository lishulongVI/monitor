# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/11/1 下午5:37
"""
from flask import Flask
from flask import jsonify

from src.script_exec import exec_script

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'STATUS': "UP"}), 200


@app.route('/reload/web')
def health():
    return jsonify({'Info': exec_script()}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)
