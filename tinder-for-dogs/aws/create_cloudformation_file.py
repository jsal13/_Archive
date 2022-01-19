import os
import re
import json


class CreateCFTemplate:
    def __init__(self):
        self.result_json = dict()

        self.header()
        self.create_section_bucket()

        self.build_result_json()

    def add_payload(self, payload):
        self.result_json = {**self.result_json, **payload}

    def header(self):
        payload = {
            "AWSTemplateFormatVersion": "2010-09-09",
            "Transform": "AWS::Serverless-2016-10-31",
        }
        self.add_payload(payload)

    def create_section_bucket(self):
        payload = {
            "S3Bucket": {
                "DeletionPolicy": "Delete",
                "Metadata": {"Comment": "Bucket to store dog pics."},
                "Properties": {
                    "AccessControl": "Private",
                    "BucketName": "Fn::Sub(cf-simple-s3-origin-${AWS::StackName}-${AWS::AccountId})",
                },
                "Type": "AWS::S3::Bucket",
            }
        }
        self.add_payload(payload)

    def build_result_json(self):
        with open("./aws/result_template.json", "w+") as rtemp:
            json.dump(self.result_json, rtemp)


c = CreateCFTemplate()
