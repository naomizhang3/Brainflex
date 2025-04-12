from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data

# This blueprint handles some basic routes that you can use for testing
tutors_routes = Blueprint('tutors_routes', __name__)

# ------------------------------------------------------------
@tutors_routes.route('/transactions', methods=["GET"])
def get_transactions():
    current_app.logger.info('GET / transactions route')
    cursor = db.get_db().cursor()
    query = """SELECT * FROM Transactions"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

@tutors_routes.route("/tutors", methods=["POST"])
def post_transactions():
    data = request.json
    current_app.logger.info(data)

    user_id = data["user_id"]
    nu_id = data["nu_id"]
    first_name = data["fn"]
    last_name = data["ln"]
    bio = data["bio"]

    cursor = db.get_db().cursor()
    query = """INSERT INTO Students (user_id, nu_id, first_name, last_name) 
    VALUES (%s, %s, %s, %s)"""
    current_app.logger.info(query)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (user_id, nu_id, first_name, last_name))
        db.get_db().commit()

        response = make_response("Successfully added student")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to add student")
        response.status_code = 400
        return response