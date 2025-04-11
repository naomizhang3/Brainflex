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