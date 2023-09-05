from config import SOAP_SERVICE
from utils.request import APIRequest


class CovidSoapClient:

    def __init__(self):
        self.soap_service = SOAP_SERVICE
        self.request = APIRequest()

    def get_soap_response(self):
        return self.request.get(self.soap_service)
