from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

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

# 4.1 Get average tutor ratings per tutor across all bookings-----
@advisor_routes.route("/bookings", methods=["GET"])
def get_bookings():
    current_app.logger.info('GET /bookings route')
    cursor = db.get_db().cursor()
    query = """
    SELECT AVG(rating) AS `Overall Average Rating`, BP.tutor_id, T.first_name, T.last_name
    FROM BookingParticipants as BP
        JOIN Tutors as T ON BP.tutor_id = T.user_id
    GROUP BY BP.tutor_id
    """

    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# Get all request types -----------------------------------------
@advisor_routes.route("/requesttypes", methods=["GET"])
def get_request_types():
    current_app.logger.info('GET /requesttypes route')
    cursor = db.get_db().cursor()
    query = """SELECT MIN(type_id) AS type_id, request_name FROM RequestTypes
    GROUP BY request_name"""
    cursor.execute(query)
    data = cursor.fetchall()
    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# 4.4 Send a request to the system admin-------------------------
@advisor_routes.route("/requests", methods = ["POST"])
def post_request():
    data = request.json
    current_app.logger.info(data)
    
    description = data["description"]
    sent_by = data["sent_by"]
    type_id = data["type_id"]

    cursor = db.get_db().cursor()
    query = "INSERT INTO Requests (descr, sent_by, type_id, reviewed_by) " \
    "VALUES (%s, %s, %s, NULL)"
    current_app.logger.info(query)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (description, int(sent_by), int(type_id)))
        db.get_db().commit()

        response = make_response("Successfully sent request")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to send request")
        response.status_code = 400
        return response
    
# 4.5 Check tutor supplies ---------------------------------------
@advisor_routes.route("/tutorsupplies", methods = ["GET"])
def get_tutor_count():
    current_app.logger.info("GET /tutorsupplies")

    cursor = db.get_db().cursor()
    query = """
    SELECT c.dept_id, c.course_num, COUNT(*) AS `Number of Available Tutors`
    FROM RegisteredCourses rc
         JOIN Tutors t ON rc.user_id = t.user_id
         JOIN Courses c ON rc.course_id = c.course_id
    GROUP BY rc.course_id, c.dept_id, c.course_num
    ORDER BY COUNT(*) DESC
    LIMIT 5;
    """
    current_app.logger.info(query)

    try:
        cursor.execute(query)
        data = cursor.fetchall()

        response = make_response(jsonify(data))
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to send GET")
        response.status_code = 400
        return response
    