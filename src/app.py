# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:38:40 2020

@author: Admin
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to CI Project"


if __name__ == "__main__":
    app.run()