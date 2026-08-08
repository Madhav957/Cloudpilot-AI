from aws.ec2 import list_instances
from aws.ec2 import list_instances, get_instance


def get_instances():
    return list_instances()


def get_instance_details(instance_id):
    return get_instance(instance_id)