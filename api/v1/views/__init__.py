#!/usr/bin/python3
"""
    A module that contains views folder
    __init__.py

"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *

