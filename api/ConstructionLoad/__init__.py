# Empty file - logic is in function_app.py
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        "Backend reachable",
        status_code=200
    )
