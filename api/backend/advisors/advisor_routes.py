from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data
#comment

# This blueprint handles advisor routes
advisor_routes = Blueprint('advisor_routes', __name__)

# 4.6 Get all payments-----------------------------------------
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

# 4.2 Get active user minutes-----------------------------------
@advisor_routes.route("/useractivity", methods=["GET"])
def get_useractivity():
    current_app.logger.info('GET /useractivity route')
    cursor = db.get_db().cursor()

    query_tutors = "SELECT user_id, active_min FROM Tutors"
    cursor.execute(query_tutors)
    tutors_data = cursor.fetchall()

    query_students = "SELECT user_id, active_min FROM Students"
    cursor.execute(query_students)
    students_data = cursor.fetchall()

    response_data = {
        "tutors": tutors_data,
        "students": students_data
    }

    response = make_response(jsonify(response_data))
    response.status_code = 200
    return response
