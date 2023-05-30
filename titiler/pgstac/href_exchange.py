import copy
import logging
import requests
from titiler.pgstac.settings import HrefExchangeSettings
href_exchange_settings = HrefExchangeSettings()
from urllib.parse import urljoin


def change_hrefs(input_json: str) -> str:
    base_url = href_exchange_settings.stac_fastapi_url
    new_output = copy.deepcopy(input_json)
    new_output["features"] = []

    for i in input_json["features"]:
        item_id = i["id"]
        collection_id = i["collection"]

        url = urljoin(base_url, f"/collections/{collection_id}/items/{item_id}")
        response = requests.get(url)

        if response.status_code != 200:
            logging.error(f"Error searching for item {item_id} in collection {collection_id}")
            return input_json

        item = response.json()
        new_output["features"].append(item)
        logging.info(f"Successfully changed hrefs for item {item_id} in collection {collection_id}")

    return new_output
