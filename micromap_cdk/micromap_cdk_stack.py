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
         # Create an IAM Role to be assumed by admins
        masters_role = iam.Role(
            self,
            'EksMastersRole',
            assumed_by=iam.AccountRootPrincipal()
        )
        # Attach an IAM Policy to that Role so users can access the Cluster
        masters_role_policy = iam.PolicyStatement(
            actions=['eks:DescribeCluster'],
            resources=['*'],  # Adjust the resource ARN if needed
        )
        masters_role.add_to_policy(masters_role_policy)
        cluster=eks.Cluster(
        self, 
        "testEnv",
        version=eks.KubernetesVersion.V1_27,
  )
        cluster.aws_auth.add_masters_role(masters_role)
        
        # Add the user to the cluster's admins
        admin_user = iam.User.from_user_arn(self, "AdminUser", user_arn="arn:aws:iam::772713293594:user/cloud_user")
        cluster.aws_auth.add_user_mapping(admin_user, groups=["system:masters"])

     

     
     
