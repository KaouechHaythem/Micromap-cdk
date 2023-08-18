


from micromap_cdk.micromap_cdk_stack import MicromapEKSStack
import os
import aws_cdk as cdk
app = cdk.App()



MicromapEKSStack(
    app, 
    'MicromapEKSStack')

# synthesize it
print ('Synthesizing stack')
app.synth()
