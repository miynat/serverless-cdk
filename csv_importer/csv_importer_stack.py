from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
    aws_s3 as _s3,
    aws_s3_notifications,
)


class CsvImporterStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = ddb.Table(
            self,
            "Students",
            partition_key={"name": "studentId", "type": ddb.AttributeType.STRING},
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        bucket = _s3.Bucket(
            self,
            "CsvBucket",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        lambdaFunc = _lambda.Function(
            self,
            "CsvHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="CsvImporter.handler",
            environment={
                "DYNAMODB_TABLE_NAME": table.table_name,
                "BUCKET_NAME": bucket.bucket_name,
            },
        )

        bucket.grant_read(lambdaFunc)
        table.grant_write_data(lambdaFunc)

        notification = aws_s3_notifications.LambdaDestination(lambdaFunc)

        bucket.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)
