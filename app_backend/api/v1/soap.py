from fastapi import APIRouter
from app_backend.schemas.soap import SOAPResponse
from app_backend.services.soap_service import generate_soap_report

router = APIRouter()

@router.get("/soap", response_model=SOAPResponse)
def get_soap_report(user_id:str = "demo-user"):
    soap_report = generate_soap_report(user_id)

    return SOAPResponse(
        soap_report=soap_report,
        disclaimer="This SOAP report is generated for educational purposes only and is not a medical diagnosis."
    )
