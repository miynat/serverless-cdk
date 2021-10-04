# Sample Serverless project with CDK

This project automatically migrates .csv files from S3 to DynamoDB.

Whenever a new file is uploaded to the relevant S3 bucket, and event notification is raised, and that notification triggers a Lambda function. That Lambda function reads the file from S3 bucket, parses it, and then write the data to a DynamoDB table.

The whole project is developed by using AWS Cloud Development Kit (CDK), and Python3 is chosen as the language of the project because Python is the language I'm most familiar with.

### Prerequisites:
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)
* An AWS user with Administrator Access:  
Run `aws configure` with the credentials of this user before running the project
* [Node.js](https://github.com/nodesource/distributions/blob/master/README.md)
* AWS CDK Toolkit:
```
npm install -g aws-cdk
```
* Python3  

<br>In order to test this project locally, follow those steps:

```
$ git checkout https://github.com/miynat/serverless-cdk.git
$ cd serverless-cdk
```

Create a Python virtualenv, and activate it:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Then install the required dependencies.

```
$ pip install -r requirements.txt
```

Deploy the code to AWS with CDK:

```
$ cdk deploy --require-approval never
```

* There are two sample .csv files provided in the **samples** directory. When those files are uploaded to the S3 bucket, their content will be available in the DynamoDB table as soon as possible.