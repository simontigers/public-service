import os

from flask_restx import Api

from api.resource import register_resources


desc = """
"""

api = Api(
    title='PublicService',
    doc='/swagger',
    version='1.0',
    description=desc,
)

HERE = os.path.abspath(os.path.dirname(__file__))
register_resources(os.path.join(HERE, ""), api)
