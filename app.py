# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/11/1 下午5:37
"""
from flask import Flask
from flask import jsonify

from const import port
from src.script_exec import exec_script

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'STATUS': "UP"}), 200


@app.route('/restart/<name>')
def reload_name(name):
    return jsonify({'Info': exec_script(name)}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
