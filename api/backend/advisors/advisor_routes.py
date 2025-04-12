from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data
#comment

# This blueprint handles advisor routes
advisor_routes = Blueprint('advisor_routes', __name__)

# ------------------------------------------------------------
@advisor_routes.route('/')
def welcome():
    current_app.logger.info('GET / handler')
    welcome_message = '<h1>ADVISORS'
    response = make_response(welcome_message)
    response.status_code = 200
    return response

# ------------------------------------------------------------
@advisor_routes.route("/payments", methods=["GET"])
def get_payments():
    current_app.logger.info('GET /payments route')
    cursor = db.get_db().cursor()
    query = """SELECT * FROM Transactions"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response
