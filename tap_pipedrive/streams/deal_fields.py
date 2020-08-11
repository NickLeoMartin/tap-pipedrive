from tap_pipedrive.stream import PipedriveStream


class DealFieldsStream(PipedriveStream):
    endpoint = 'dealFields'
    schema = 'deal_fields'
    key_properties = ['id']
    state_field = None
