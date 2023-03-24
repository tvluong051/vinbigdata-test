from api.app import create_app, db
from api.models import Call, Billing, save_call
from api.inouts import call_input_schema, billing_output_schema
from flask_restful import Resource, Api
from flask import jsonify, request
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.views import MethodResource
from flask_apispec.extension import FlaskApiSpec
from flask_apispec import doc
from marshmallow import ValidationError
from functools import reduce
import math

app = create_app()

class CallApi(MethodResource, Resource):
    @doc(description='Put new call to user.', tags=['Call'])
    def put(self, user_name):
        try:
            call = call_input_schema.loads(request.data)
            app.logger.info(f"PUT - Add new call for user_name: {user_name}, call: {call}")
            call_model = Call(user_name, call['call_duration'])
            save_call(call_model)
            return 'Success', 200
        except ValidationError as err:
            return f"Wrong input format: {err.messages}", 400


class BillingApi(MethodResource, Resource):
    BLOCK_SIZE = 30000

    @doc(description='Get billing for user.', tags=['Billing'])
    def get(self, user_name):
        app.logger.info(f"GET - Request billing for user_name: {user_name}")
        calls = Call.query.filter_by(user_name = user_name).all()
        if not calls:
            return billing_output_schema.dump({}), 404
        block_count = reduce(lambda a, b: a+b, map(lambda c: math.ceil(c.call_duration / self.BLOCK_SIZE), calls))
        bill = Billing(len(calls), block_count)
        return billing_output_schema.dump(bill)

api = Api(app)
api.add_resource(CallApi, '/mobile/<string:user_name>/call')
api.add_resource(BillingApi, '/mobile/<string:user_name>/billing')

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='VinBigdata Call API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)
docs.register(CallApi)
docs.register(BillingApi)
