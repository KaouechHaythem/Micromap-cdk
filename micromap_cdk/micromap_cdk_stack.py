import os
from aws_cdk import (
    Stack,
    aws_ec2,
    aws_iam as iam,

)
import aws_cdk.aws_eks as eks
import aws_cdk.aws_ec2 as ec2
from constructs import Construct




class MicromapEKSStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
       
        cluster=eks.Cluster(
        self, 
        "MICROMAP",
        version=eks.KubernetesVersion.V1_27,
        default_capacity=2,
        default_capacity_instance=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO)
  )
        user_arn = os.environ.get('USER_ARN')

        # Add the user to the cluster's admins
        admin_user = iam.User.from_user_arn(self, "AdminUser", user_arn=user_arn)
        cluster.aws_auth.add_user_mapping(admin_user, groups=["system:masters"])

     

     
     
