import requests
import logging
import copy

from titiler.pgstac import model


def change_hrefs(input_json: str) -> str:
    base_url = "http://stac-fastapi-assets-signing-proxy.os-eo-platform-rg-staging.azure.com"
    new_output = copy.deepcopy(input_json)
    new_output["features"] = []
    for i in input_json["features"]:
        item_id = i["id"]
        collection_id = i["collection"]

        response = requests.get(f"{base_url}/collections/{collection_id}/items/{item_id}")
        if response.status_code != 200:
            logging.error(f"Error searching for item {item_id} in collection {collection_id}")
            return input_json
        item = response.json()
        new_output["features"].append(item)
        logging.info(f"Successfully changed hrefs for item {item_id} in collection {collection_id}")
    return new_output
