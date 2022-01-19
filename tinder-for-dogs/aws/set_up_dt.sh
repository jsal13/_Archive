#!/bin/bash

# Run in root of folder
# requires aws cli v2

# TODO: maybe quiet this up?
aws2 dynamodb batch-write-item --request-items file://db/dog_metadata_dynamodb.json
aws2 dynamodb batch-write-item --request-items file://db/test_user_metadata_dynamodb.json