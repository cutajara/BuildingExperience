from pathlib import Path

from aws_cdk import CfnOutput, Duration, Stack
from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_sns as sns
from constructs import Construct


class BuildingExperienceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        contact_topic = sns.Topic(
            self,
            "ContactFormTopic",
            display_name="BuildingExperienceContactForm",
        )

        contact_handler = lambda_.Function(
            self,
            "ContactFormHandler",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="contact_form_handler.lambda_handler",
            code=lambda_.Code.from_asset(str(Path(__file__).resolve().parent / "lambda")),
            environment={"CONTACT_TOPIC_ARN": contact_topic.topic_arn},
            timeout=Duration.seconds(30),
        )

        contact_topic.grant_publish(contact_handler)

        api = apigateway.RestApi(
            self,
            "BuildingExperienceApi",
            rest_api_name="building-experience-contact-api",
            description="API Gateway for the Building Experience contact form",
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=[
                    "Content-Type",
                    "X-Amz-Date",
                    "Authorization",
                    "X-Api-Key",
                    "X-Amz-Security-Token",
                ],
            ),
        )

        contact_resource = api.root.add_resource("contact")
        contact_resource.add_method(
            "POST",
            apigateway.LambdaIntegration(contact_handler),
            authorization_type=apigateway.AuthorizationType.NONE,
        )

        CfnOutput(
            self,
            "ApiGatewayUrl",
            value=f"{api.url}contact",
            description="API Gateway endpoint for the website contact form",
        )
