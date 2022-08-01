import datetime

from flask_restx import Namespace, Resource, reqparse
from flask import current_app

from api.lib.train import query_train

api = Namespace('train', description='火车票')


@api.route('/')
class ViewAccount(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('_from', type=str, required=True, default='',
                            help='', location='args')
    get_parser.add_argument('_to', type=str, required=True, default='',
                            help='', location='args')

    get_parser.add_argument('_date', type=str, required=True, default='',
                            help='', location='args')

    @api.expect(get_parser)
    def get(self):
        """
        查询火车票
        """
        data = self.get_parser.parse_args()
        try:
            datetime.datetime.strptime(data['_date'], '%Y-%m-%d')
        except Exception as e:
            return {f'message': f"{data['_date']}, 不是日期格式 %Y-%m-%d"}, 400

        try:
            return query_train(**data)
        except Exception as e:
            return {
                       'message': str(e)
                   }, 400
