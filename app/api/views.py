from flask import request, jsonify
from ..crowler import get_data
from . import api


@api.route('/<string:content>', methods=['GET'])
def index(content):
    sig = {
        content:get_data(content)
    }
    return jsonify(sig), 200