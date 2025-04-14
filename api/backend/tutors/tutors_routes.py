from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data


# This blueprint handles some basic routes that you can use for testing
tutors_routes = Blueprint('tutors_routes', __name__)

# 2.1 --- POST /registeredcourses/{tutor_id} --------------------------

# 2.2 --- PUT /tutors/{tutor_id} --------------------------------------
@tutors_routes.route("add_bio", methods=["PUT"])
def update_add_bio():
    data = request.json
    current_app.logger.info(data)

    user_id = data["user_id"]
    bio = data["bio"]

    cursor = db.get_db().cursor()
    query = """
        UPDATE Tutors
        SET bio = %s
        WHERE user_id = %s;
    """
    current_app.logger.info(query)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (bio, user_id))
        db.get_db().commit()


        response = make_response("Successfully added bio")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to add bio")
        response.status_code = 400
        return response
   
# 2.3 --- GET /bookings/{user_id} --------------------------------------
@tutors_routes.route('/Bookings', methods=["GET"])
def get_Bookings():
    current_app.logger.info('GET / Bookings route')
    cursor = db.get_db().cursor()
    query = """SELECT * FROM Bookings"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# 2.5 --- GET /transactions/{tutor_id} --------------------------------
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

# 2.6 --- DELETE /bookings/{booking_id} ---------------------
# delete booking data at the inputted booking ID
@tutors_routes.route('/deletetutorbookings', methods=["DELETE"])
def delete_tutor_bookings():
    data = request.json
    current_app.logger.info(data)

    booking_id = data["booking_id"]

    cursor = db.get_db().cursor()
    query = """DELETE FROM Bookings WHERE booking_id = %s"""
    current_app.logger.info(query)
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (booking_id))
        db.get_db().commit()

        response = make_response("Booking successfully deleted.")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to delete booking.")
        response.status_code = 400
        return response

