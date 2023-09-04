
import json
from boto3.session import Session as boto3_session
from pprint import pprint

AWS_REGIONS = [
    "eu-central-1",
    "eu-west-1",
    "us-west-2"
]
layers = [
    "gdal36",
]


def main():
    results = []
    for region in AWS_REGIONS:
        res = {"region": region, "layers": []}

        session = boto3_session(region_name=region)
        client = session.client("lambda")
        for layer in layers:
            response = client.list_layer_versions(LayerName=layer)
            latest = response["LayerVersions"][0]
            res["layers"].append(dict(
                name=layer,
                arn=latest["LayerVersionArn"],
                version=latest["Version"]
            ))
        results.append(res)

    pprint(results)


if __name__ == '__main__':
    main()
