import json
import azure.functions as func
from .estimator import read_materials, calculate_total_weight

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        file = req.files.get('file')

        if not file:
            return func.HttpResponse(
                json.dumps({"error": "No file uploaded"}),
                status_code=400,
                mimetype="application/json"
            )

        # Read file content
        content = file.read().decode('utf-8')
        lines = content.splitlines()

        # Process materials
        materials = []
        for line in lines:
            clean = line.split("#")[0].strip()
            if not clean:
                continue

            parts = clean.split()
            if len(parts) != 3:
                continue

            name, weight, qty = parts
            try:
                weight = float(weight)
                qty = int(qty)
            except:
                continue

            materials.append((name, weight, qty))

        if not materials:
            return func.HttpResponse(
                json.dumps({"error": "Invalid or empty file"}),
                status_code=400,
                mimetype="application/json"
            )

        total_weight = calculate_total_weight(materials)
        overhead = total_weight * 0.2
        final_weight = total_weight + overhead

        result = {
            "total_weight": total_weight,
            "overhead": overhead,
            "final_weight": final_weight
        }

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
