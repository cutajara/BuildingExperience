#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from building_experience_stack import BuildingExperienceStack

app = App()

BuildingExperienceStack(
    app,
    "BuildingExperienceStack",
    env=Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION", "ap-southeast-2"),
    ),
)

app.synth()
