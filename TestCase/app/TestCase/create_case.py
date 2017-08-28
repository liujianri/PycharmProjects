import sys
from flask import request, render_template
from . import case

@case.route('/')
def index():
    return "hello hahah"