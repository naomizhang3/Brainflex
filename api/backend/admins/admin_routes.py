from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data

admin_routes = Blueprint('admin_routes', __name__)

# ------------------------------------------------------------
@admin_routes.route("/systemlogs", methods=['GET'])
def get_system_logs():
    current_app.logger.info('GET /systemlogs route')
    cursor = db.get_db().cursor()
    query = """SELECT sl.creation_date, sl.resolved_date, lt.name
    FROM SystemLogs sl JOIN LogTypes lt ON sl.type_id = lt.type_id 
    ORDER BY sl.creation_date ASC"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# ------------------------------------------------------------
@admin_routes.route("/backupschedule", methods=["GET"])
def get_backup_schedule():
    current_app.logger.info('GET /backupschedule route')
    cursor = db.get_db().cursor()
    query = """SELECT * FROM Backups"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# ------------------------------------------------------------
@admin_routes.route("/advrequests", methods=["GET"])
def get_admin_requests():
    current_app.logger.info('GET / advrequests route')
    cursor = db.get_db().cursor()
    query = """SELECT * FROM Requests"""
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

# ------------------------------------------------------------
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

# ------------------------------------------------------------
@admin_routes.route("/studentdata", methods=["POST"])
def post_student_data():
    data = request.json
    current_app.logger.info(data)

    user_id = data["user_id"]
    nu_id = data["nu_id"]
    first_name = data["fn"]
    last_name = data["ln"]

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
    
# ------------------------------------------------------------
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