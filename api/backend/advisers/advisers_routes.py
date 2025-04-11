from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data

# This blueprint handles some basic routes that you can use for testing
advisers_routes = Blueprint('advisers_routes', __name__)

# ------------------------------------------------------------
@advisers_routes.route('/')
def welcome():
    current_app.logger.info('GET / handler')
    welcome_message = '<h1>ADVISERS'
    response = make_response(welcome_message)
    response.status_code = 200
    return response