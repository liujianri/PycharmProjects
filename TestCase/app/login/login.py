#!/usr/bin/env python
# coding=utf-8
import sys
from flask import request, render_template
from . import auth
from ..models import Role
from ..models import User
from app import db

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

@auth.route('/')
def index():
    admin_role = Role(name='Admin',pwd = '1234')
    user_name = User(username="Adminer",status="tttt",role=admin_role)
    db.session.add_all([admin_role,  user_name, ])
    db.session.commit()

    return "hello hahah"