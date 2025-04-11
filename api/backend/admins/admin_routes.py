from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db
from backend.simple.playlist import sample_playlist_data

# This blueprint handles some basic routes that you can use for testing
admin_routes = Blueprint('admin_routes', __name__)

# ------------------------------------------------------------
@admin_routes.route("/systemlogs", methods=['GET'])
def get_customers():

    current_app.logger.info('GET /systemlogs route')
    cursor = db.get_db().cursor()
    query = "SELECT * FROM SystemLogs"
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response