import azure.functions as func
from azure.functions import HttpRequest, HttpResponse
import json

app = func.FunctionApp()

@app.function_name(name="ConstructionLoad")
@app.route(route="ConstructionLoad", methods=["GET", "POST"])
def construction_load(req: HttpRequest) -> HttpResponse:
    try:
        # Read materials file
        materials = []
        with open("materials.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                name, weight = line.split(":")
                materials.append({"name": name.strip(), "weight": float(weight.strip())})

        # Calculate total weight
        total_weight = sum(item["weight"] for item in materials)

        # Add 20% overhead
        final_weight = total_weight * 1.2

        result = {
            "materials": materials,
            "total_weight": total_weight,
            "final_weight_with_overhead": final_weight
        }

        return HttpResponse(
            json.dumps(result),
            mimetype="application/json"
        )

    except Exception as e:
        return HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
