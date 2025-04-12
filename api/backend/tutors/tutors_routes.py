from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data


# This blueprint handles some basic routes that you can use for testing
tutors_routes = Blueprint('tutors_routes', __name__)


# ------------------------------------------------------------
# GET /transactions/{tutor_id} -------------------------------


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


# POST /tutors/{tutor_id} --------------------------------
@tutors_routes.route("add_bio", methods=["POST"])
def post_transactions():
    data = request.json
    current_app.logger.info(data)


    # change
    first_name = data["first_name"]
    last_name = data["last_name"]
    bio = data["bio"]


    cursor = db.get_db().cursor()
    query = """INSERT INTO Students (first_name, last_name, bio)
    VALUES (%s, %s, %s)"""
    current_app.logger.info(query)


    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, bio))
        db.get_db().commit()


        response = make_response("Successfully added bio")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to add bio")
        response.status_code = 400
        return response
   
# PUT /tutors/{tutor_id} ---------------------------------------------


# DELETE /bookings/{user_id}/{booking_id} ----------------------------


# GET /bookings/{user_id} ---------------------------------------------
