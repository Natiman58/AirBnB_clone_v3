#!/usr/bin/python3
"""
    A module that contains index.py
"""

from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/status', methods=['GET'])
def status():
    """
        Displays the a json format message
    """
    if request.method == 'GET':
        response = {"status": "OK"}
        return jsonify(response)
