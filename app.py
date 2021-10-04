#!/usr/bin/env python3
from aws_cdk import core as cdk

from csv_importer.csv_importer_stack import CsvImporterStack


app = cdk.App()
CsvImporterStack(
    app,
    "CsvImporterStack",
    env=cdk.Environment(account="251999085741", region="eu-central-1"),
)

app.synth()
