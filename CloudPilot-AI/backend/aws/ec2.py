import boto3


def get_instance(instance_id):
    ec2 = boto3.client("ec2")

    response = ec2.describe_instances(
        InstanceIds=[instance_id]
    )

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            return {
                "id": instance["InstanceId"],
                "state": instance["State"]["Name"],
                "type": instance["InstanceType"],
                "ami": instance["ImageId"],
                "availability_zone": instance["Placement"]["AvailabilityZone"]
            }

    return None