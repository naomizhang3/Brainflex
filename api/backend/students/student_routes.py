from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object for students
student_routes = Blueprint("student_routes", __name__)


#--------------1.1 Get tutors data for specific courses----------------
@student_routes.route('/tutors/<course_id>/<course_num>', methods=['GET'])
def get_bookings(course_id, course_num):
    current_app.logger.info('GET /tutors/<course_id>/<course_num> route')
    cursor = db.get_db().cursor()
    query = """SELECT t.user_id, t.first_name, t.last_name, t.bio
               FROM Tutors t
               JOIN RegisteredCourses rc ON t.user_id = rc.user_id
               JOIN Courses c ON rc.course_id = c.course_id
               WHERE c.dept_id = %s AND c.course_num = %s;"""
    cursor.execute(query, (course_id, course_num))
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# ----------------1.4 Get all bookings associated with the student-----------
@student_routes.route('/bookings/<userID>', methods=['GET'])
def get_student_bookings(userID):
    current_app.logger.info('GET /bookings/<userID> route')
    cursor = db.get_db().cursor()
    query = """
    SELECT b.booking_id, t.first_name, t.last_name, b.scheduled_time
    FROM Bookings b
         JOIN BookingParticipants bp ON b.booking_id = bp.booking_id
         JOIN Students s ON bp.student_id = s.user_id
         JOIN Tutors t ON bp.tutor_id = t.user_id
    WHERE s.user_id = %s;
    """

    cursor.execute(query, (userID))
    
    data = cursor.fetchall()
    
    the_response = make_response(jsonify(data))
    the_response.status_code = 200
    return the_response

# ------------------ 1.2 create a new booking--------------------------
@student_routes.route("/createbookings", methods=["POST"])
def post_bookings_data():

    data = request.json
    current_app.logger.info('POST /createbookings route')
    cursor = db.get_db().cursor()

    completion_status = data["completion_status"]
    creation_time = data["creation_time"]
    scheduled_time = data["scheduled_time"]
    
    tutor_id = data["tutor_id"]
    student_id = data["student_id"]

    query_bookings = """INSERT INTO Bookings (completion_status, creation_time, scheduled_time)
    VALUES (%s, %s, %s);"""

    query_bparticipants = """INSERT INTO BookingParticipants (tutor_id, student_id, booking_id)
    VALUES (%s, %s, %s);"""

    current_app.logger.info(query_bookings)
    current_app.logger.info(query_bparticipants)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query_bookings, (completion_status, creation_time, scheduled_time))

        booking_id = cursor.lastrowid
        cursor.execute(query_bparticipants, (int(tutor_id), int(student_id), int(booking_id)))
        db.get_db().commit()

        response = make_response("Successfully scheduled a booking.")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to schedule a booking.")
        response.status_code = 400
        return response


# -------------------1.3 update booking data----------------------
@student_routes.route('/bookings/<userID>/<booking_id>', methods=['PUT'])
def update_bookings(booking_id):
    data = request.json
    current_app.logger.info('PUT /bookings/<userID>/<booking_id> route')
    time = data['time']

    query = """UPDATE Bookings
    SET scheduled_time = %s
    WHERE booking_id = %s;"""
    
    try:
        cursor = db.get_db().cursor()
        r = cursor.execute(query, (time, booking_id))
        db.get_db().commit()
        response = make_response("Successfully rescheduled a booking.")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to reschedule a booking.")
        response.status_code = 400
        return response
    
# ------------------1.3 delete booking data---------------------------
@student_routes.route('/cancel-bookings/<booking_id>', methods=["DELETE"])
def delete_tutor_bookings(booking_id):
    current_app.logger.info("delete /cancel-bookings/<booking_id>")

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