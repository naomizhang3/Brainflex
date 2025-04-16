from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db


# This blueprint handles some basic routes that you can use for testing
tutors_routes = Blueprint('tutors_routes', __name__)

# 2.1 --- POST /registeredcourses/{tutor_id} --------------------------
@tutors_routes.route("/register-couses/<user_id>", methods=["POST"])
def post_bookings_data(user_id):

    data = request.json
    current_app.logger.info('POST /register-couses/<user_id>')
    cursor = db.get_db().cursor()

    course_id = data["course_id"]
    course_num = data["course_num"]
    
    query_bookings = """INSERT INTO RegisteredCourses
    (user_id, course_id, course_num)
    VALUES (%s, %s, %s);
    """
    current_app.logger.info(query_bookings)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query_bookings, (int(user_id), course_id, course_num))
        db.get_db().commit()

        response = make_response("Successfully added a tutorable class.")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to add a tutorable class.")
        response.status_code = 400
        return response
    
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


        response = make_response("Successfully added bio.")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to add bio.")
        response.status_code = 400
        return response
   
# 2.3 --- GET /bookings/{user_id} --------------------------------------
@tutors_routes.route('/bookings/<tutor_id>', methods=["GET"])
def get_bookings(tutor_id):
    current_app.logger.info('GET / bookings route')
    cursor = db.get_db().cursor()
    query = """SELECT b.booking_id, b.scheduled_time, s.first_name, s.last_name 
        FROM Bookings b JOIN BookingParticipants bp ON b.booking_id = 
        bp.booking_id JOIN Tutors t ON bp.tutor_id = t.user_id JOIN Students s 
        ON bp.student_id = s.user_id WHERE t.user_id = %s;"""
    cursor.execute(query, (tutor_id))
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
@tutors_routes.route('/deletebookings', methods=["DELETE"])
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