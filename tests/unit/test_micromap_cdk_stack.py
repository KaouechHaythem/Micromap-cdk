import aws_cdk as core
import aws_cdk.assertions as assertions

from micromap_cdk.micromap_cdk_stack import MicromapCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in micromap_cdk/micromap_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MicromapCdkStack(app, "micromap-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
