from marshmallow import Schema, fields

class CallInput(Schema):
    call_duration = fields.Int(required=True)


class BillingOutput(Schema):
    call_count = fields.Int(required=True)
    block_count = fields.Int(required=True)


call_input_schema = CallInput()
billing_output_schema = BillingOutput()