from app import app
from flask import request
import ctypes

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/',methods=['GET','POST'])
def render():
    if request.method == 'POST':
        dll = ctypes.windll.LoadLibrary( 'CloudFunction.dll' )
        data=request.data
        result=Cloud_Process(data)
        return result
    else:
        return "hello"
