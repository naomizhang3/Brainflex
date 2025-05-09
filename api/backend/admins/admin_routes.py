from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

admin_routes = Blueprint('admin_routes', __name__)

# -------------3.3 get relevant system logs data---------------
@admin_routes.route("/systemlogs", methods=['GET'])
def get_system_logs():
    current_app.logger.info('GET /systemlogs route')
    cursor = db.get_db().cursor()
    query = """SELECT sl.creation_date, sl.resolved_date, lt.type_name
    FROM SystemLogs sl JOIN LogTypes lt ON sl.type_id = lt.type_id 
    ORDER BY sl.creation_date ASC"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# ------------3.5 get all backup schedule data----------------
@admin_routes.route("/backupschedule", methods=["GET"])
def get_backup_schedule():
    current_app.logger.info('GET /backupschedule route')
    cursor = db.get_db().cursor()
    query = """SELECT b.backup_date, b.backup_status, a.first_name, a.last_name
      FROM Backups b JOIN Admins a ON b.admin_id = a.admin_id"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# -------------3.6 get all advisor requests data-------------------
@admin_routes.route("/advrequests", methods=["GET"])
def get_admin_requests():
    current_app.logger.info('GET /advrequests route')
    cursor = db.get_db().cursor()
    query = """SELECT r.descr, r.review_status, rt.request_name 
    FROM Requests r JOIN RequestTypes rt ON r.type_id = rt.type_id"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# ------------3.4 get all student data-------------------------------
@admin_routes.route("/studentdata", methods=["GET"])
def get_student_data():
    current_app.logger.info('GET /studentdata route')
    cursor = db.get_db().cursor()
    query = """SELECT * FROM Students"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# ------------3.2 post new inputted student data--------------------
@admin_routes.route("/studentdata", methods=["POST"])
def post_student_data():
    data = request.json
    current_app.logger.info(data)

    nu_id = data["nu_id"]
    first_name = data["fn"]
    last_name = data["ln"]

    cursor = db.get_db().cursor()
    query = """INSERT INTO Students (nu_id, first_name, last_name) 
    VALUES (%s, %s, %s)"""
    current_app.logger.info(query)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (nu_id, first_name, last_name))
        db.get_db().commit()

        response = make_response("Successfully added student")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to add student")
        response.status_code = 400
        return response
    
# ---------3.1 delete student data at the inputted user ID------------
@admin_routes.route("/studentdata", methods=["DELETE"])
def delete_student_data():
    data = request.json
    current_app.logger.info(data)

    user_id = data["user_id"]

    cursor = db.get_db().cursor()
    query = """DELETE FROM Students WHERE user_id = %s"""
    current_app.logger.info(query)
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (user_id,))
        db.get_db().commit()

        response = make_response("Student data successfully deleted.")
        response.status_code = 200
        return response
    except:
        response = make_response("Failed to delete student data.")
        response.status_code = 400
        return response