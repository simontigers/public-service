# -*- coding:utf-8 -*-

import os
import sys
from inspect import getmembers, isclass

from flask import jsonify
from flask_restx import Resource


class APIView(Resource):

    def __init__(self):
        super(APIView, self).__init__()

    @staticmethod
    def jsonify(*args, **kwargs):
        return jsonify(*args, **kwargs)


API_PACKAGE = "api"


def register_resources(resource_path, rest_api):
    for root, _, files in os.walk(os.path.join(resource_path)):
        for filename in files:
            if not filename.startswith("_") and filename.endswith("py"):
                module_path = os.path.join(API_PACKAGE, root[root.index("views"):])
                if module_path not in sys.path:
                    sys.path.insert(1, module_path)
                view = __import__(os.path.splitext(filename)[0])
                if 'disable' not in dir(view):
                    rest_api.add_namespace(view.api)
