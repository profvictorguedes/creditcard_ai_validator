from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import re
import time

VISION_ENDPOINT = "Endpoint_goes_here"
VISION_KEY = "Your_key"


def extract_text_from_image(image_url):
    client = ComputerVisionClient(
        VISION_ENDPOINT,
        CognitiveServicesCredentials(VISION_KEY)
    )

    response = client.read(image_url, raw=True)
    operation_id = response.headers["Operation-Location"].split("/")[-1]

    while True:
        result = client.get_read_result(operation_id)
        if result.status.lower() not in ["notstarted", "running"]:
            break
        time.sleep(1)

    extracted_text = []

    if result.status.lower() == "succeeded":
        for page in result.analyze_result.read_results:
            for line in page.lines:
                extracted_text.append(line.text)

    return extracted_text
