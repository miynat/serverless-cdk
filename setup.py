import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="csv_importer",
    version="0.0.1",

    description="CDK Python app for importing CSV files from S3 to DynamoDB",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "csv_importer"},
    packages=setuptools.find_packages(where="csv_importer"),

    install_requires=[
        "aws-cdk.core==1.125.0",
        "aws-cdk.aws-s3==1.125.0",
        "aws_cdk.aws_s3_notifications==1.125.0",
        "aws-cdk.aws-lambda==1.125.0",
        "aws-cdk.aws_dynamodb==1.125.0",
        "boto3==1.18.53",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
