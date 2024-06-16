import logging
import json
import requests
import os
import dotenv
import datetime
from pytz import timezone

dotenv.load_dotenv()

shouldLogToKibana = os.getenv("LOG_TO_KIBANA", "false") == "true"


def setup_logger():
    # Create a logger
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    # Create a handler for logging to stdout
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Set the formatter for the handler
    stdout_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(stdout_handler)

    return logger


# Call setup_logger() to configure the logger immediately when this module is imported
logger = setup_logger()
logger.info(f"Loggin to kibana {shouldLogToKibana} : {
            os.getenv('LOG_TO_KIBANA')}")

logFunctionsByLevel = {
    "info": logger.info,
    "warning": logger.warning,
    "error": logger.error,
    "debug": logger.debug
}


def try_convert_to_str_dict(obj):
    """Attempts to convert an object to a dictionary with string keys and values.

    Args:
        obj: The object to be converted.

    Returns:
        A dictionary with string keys and values if the conversion is successful,
        or an empty dictionary otherwise.
    """

    if isinstance(obj, dict):
        # If it's already a dictionary, convert keys recursively if necessary
        return {str(k): try_convert_to_str_dict(v) for k, v in obj.items()}
    elif isinstance(obj, str):
        return {"message": obj}
    elif isinstance(obj, int):
        return {"value": obj}
    elif hasattr(obj, "__dict__"):
        # If it has a __dict__ attribute (like classes or instances), use it
        return {str(k): try_convert_to_str_dict(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, (list, tuple)):
        # If it's a list or tuple, convert elements recursively
        return [try_convert_to_str_dict(v) for v in obj]
    else:
        # Try converting the object itself to a string
        try:
            return {"value": str(obj)}
        except (AttributeError, ValueError):
            # If conversion fails, return an empty dictionary
            return {}


def log(level: str, event: str, details=None):
    logFunction = logFunctionsByLevel.get(level, None)
    if logFunction is None:
        return

    # details = try_convert_to_str_dict(details)

    details = dict()

    details["event"] = event
    details["level"] = level

    # details = json.dumps(details)

    try:
        if shouldLogToKibana:
            indexKibana("etl-logs", details)
            logger.info("Log indexed in Kibana")
        logFunction(event)

    except Exception as e:
        logger.error("Failed to index log in Kibana")
        logger.error(e)


def indexKibana(index, object, retries=3):
    elasticIngestURL = os.getenv("ELASTIC_INGEST_URL") + "/" + index + "/_doc"

    headers = {
        'Content-Type': 'application/json'
    }

    username = os.getenv("ELASTIC_USERNAME")
    password = os.getenv("ELASTIC_PASSWORD")

    # Replace with your city's time zone if needed
    local_timezone = timezone('America/Bogota')
    timestamp = datetime.datetime.now(local_timezone).isoformat()
    object["timestamp"] = timestamp

    response = requests.request(
        "POST", elasticIngestURL, headers=headers, data=json.dumps(object), auth=(username, password))

    if response.status_code != 201:
        logger.debug(f"Unexpected response:\n status code {
                     response.status_code}\n text: {response.text}")
        # retry opt
        if retries > 0:
            return indexKibana(index, object, retries - 1)

        raise Exception("Failed to index object in Kibana")
