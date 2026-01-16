from pydantic import BaseModel

class SOAPResponse(BaseModel):
    soap_report:str
    disclaimer:str