from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object for students
student_routes = Blueprint("student_routes", __name__)


#-----1.1---------As a student, I need to be able to filter-search for tutors so that I can see tutors (and their bios) for the classes I’m enrolled in.


@student_routes.route('/tutors/<course_id>/<course_num>', methods=['GET'])
def get_bookings(course_id, course_num):
    # response.status_code = 200

    
    # return 'HIII'
    current_app.logger.info('GET /tutors/<course_id>/<course_num> route')
    cursor = db.get_db().cursor()
    query = """SELECT t.first_name, t.last_name, t.bio
               FROM Tutors t
               JOIN RegisteredCourses rc ON t.user_id = rc.user_id
               WHERE course_id = %s AND course_num = %s;"""
    cursor.execute(query, (course_id, course_num))
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# ---------1.4---------------------------------------------------
@student_routes.route('/bookings/<userID>', methods=['GET'])
def get_student_bookings(userID):
    current_app.logger.info('GET /bookings/<userID> route')
    cursor = db.get_db().cursor()
    query = """
    SELECT b.booking_id, b.scheduled_time
    FROM Bookings b
         JOIN BookingParticipants bp ON b.booking_id = bp.booking_id
         JOIN Students s ON bp.student_id = s.user_id
    WHERE s.user_id = %s;
    """

    cursor.execute(query, (userID))
    
    data = cursor.fetchall()
    
    the_response = make_response(jsonify(data))
    the_response.status_code = 200
    return the_response

#1.2---------------------------------------------------------
@student_routes.route("/createbookings", methods=["POST"])
def post_bookings_data():
    data = request.json
    current_app.logger.info('POST /createbookings route')
    cursor = db.get_db().cursor()

    booking_id = data["booking_id"]
    completion_status = data["completion_status"]
    creation_time = data["creation_time"]
    scheduled_time = data["scheduled_time"]

    tutor_id = data["tutor_id"]
    student_id = data["student_id"]
    rating = data["rating"]

    query_bookings = """INSERT INTO Bookings (booking_id, completion_status, creation_time, scheduled_time)
    VALUES (%s, %s, %s, %s);"""

    query_bparticipants = """INSERT INTO BookingParticipants (tutor_id, student_id, booking_id, rating)
    VALUES (%s, %s, %s, %s);"""

    current_app.logger.info(query_bookings)
    current_app.logger.info(query_bparticipants)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query_bookings, (booking_id, completion_status, creation_time, scheduled_time))
        cursor.execute(query_bparticipants, (tutor_id, student_id, booking_id, rating))
        db.get_db().commit()

        response = make_response("Successfully scheduled a booking")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to schedule a booking")
        response.status_code = 400
        return response
# Get all customers from the system
# @customers.route("/bookings/", methods=['GET'])
# def get_customers():

#     cursor = db.get_db().cursor()
#     cursor.execute('''SELECT id, company, last_name,
#                     first_name, job_title, business_phone FROM customers
#     ''')
    
#     theData = cursor.fetchall()
    
#     the_response = make_response(jsonify(theData))
#     the_response.status_code = 200
#     return the_response

# #------------------------------------------------------------
# # Update customer info for customer with particular userID
# #   Notice the manner of constructing the query.
# @customers.route('/customers', methods=['PUT'])
# def update_customer():
#     current_app.logger.info('PUT /customers route')
#     cust_info = request.json
#     cust_id = cust_info['id']
#     first = cust_info['first_name']
#     last = cust_info['last_name']
#     company = cust_info['company']

#     query = 'UPDATE customers SET first_name = %s, last_name = %s, company = %s where id = %s'
#     data = (first, last, company, cust_id)
#     cursor = db.get_db().cursor()
#     r = cursor.execute(query, data)
#     db.get_db().commit()
#     return 'customer updated!'

# #------------------------------------------------------------
# # Get customer detail for customer with particular userID
# #   Notice the manner of constructing the query. 
# @customers.route('/customers/<userID>', methods=['GET'])
# def get_customer(userID):
#     current_app.logger.info('GET /customers/<userID> route') 
#     cursor = db.get_db().cursor()
#     cursor.execute('SELECT id, first_name, last_name FROM customers WHERE id = {0}'.format(userID))
    
#     theData = cursor.fetchall()
    
#     the_response = make_response(jsonify(theData))
#     the_response.status_code = 200
#     return the_response

# #------------------------------------------------------------
# # Makes use of the very simple ML model in to predict a value
# # and returns it to the user
# @customers.route('/prediction/<var01>/<var02>', methods=['GET'])
# def predict_value(var01, var02):
#     current_app.logger.info(f'var01 = {var01}')
#     current_app.logger.info(f'var02 = {var02}')

#     returnVal = predict(var01, var02)
#     return_dict = {'result': returnVal}

#     the_response = make_response(jsonify(return_dict))
#     the_response.status_code = 200
#     the_response.mimetype = 'application/json'
#     return the_response