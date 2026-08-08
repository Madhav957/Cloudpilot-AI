import boto3


def get_identity():
    sts = boto3.client("sts")
    return sts.get_caller_identity()