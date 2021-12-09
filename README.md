# cloudreach-demo

This is just a sketch for an example solution detailed in the assessment.

The idea is to

## REST API1:

* set up an API gateway that proxies data into AWS Kinesis Firehose
* use AWS Kinesis firehose to store the data in S3 for future processing and simultaneously channel it into Kinesis Data Analysis. 
* Within Kinesis Data Analysis we should collect the incoming GPS coordinates by user within a 5 minute timeframe. We should use Thumbling Windows here
* We then send the collected data into Kinesis data streams
* Kinesis data streams sends the data to a Lambda function that is storing it into DynamoDb
* The lambda function also takes care about marking if the user is entering a hotspot
* The API would use AWS Cognito token


## REST API2 : 

* API gateway with a lambda function
* Using the Dynamodb application described above
* The API could be secured with Cognito with IAM

## Experinment

As an experiment I would also consider using AWS Timestream. This could potentially remove a couple elements from our architecture above.