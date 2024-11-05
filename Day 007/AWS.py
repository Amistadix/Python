import random
import time

# List of AWS services questions and answers
aws_questions = [
    ("What is Amazon EC2 used for?", "Amazon EC2 is a service that provides resizable compute capacity in the cloud."),
    ("What does Amazon S3 stand for?", "Amazon S3 stands for Amazon Simple Storage Service."),
    ("What is AWS Lambda used for?", "AWS Lambda lets you run code without provisioning or managing servers."),
    ("What is Amazon RDS?", "Amazon RDS is a managed relational database service that makes it easy to set up, operate, and scale a relational database."),
    ("What is the primary purpose of Amazon CloudFront?", "Amazon CloudFront is a content delivery network (CDN) that delivers data, videos, applications, and APIs globally with low latency."),
    ("What does Amazon IAM stand for?", "Amazon IAM stands for Identity and Access Management, used for controlling access to AWS resources."),
    ("What is AWS Elastic Beanstalk?", "AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services."),
    ("What is Amazon VPC?", "Amazon VPC stands for Virtual Private Cloud, allowing users to create isolated networks within AWS."),
    ("What is Amazon DynamoDB?", "Amazon DynamoDB is a managed NoSQL database service offering fast and flexible performance."),
    ("What is AWS CloudTrail?", "AWS CloudTrail is a service that enables governance, compliance, and operational and risk auditing of your AWS account."),
]

def ask_question():
    question, answer = random.choice(aws_questions)
    print("Question:", question)
    time.sleep(3)  # Pause for 3 seconds to give the user time to think
    print("Answer:", answer)
    print()

# Main program to ask a series of questions
num_questions = 5
for _ in range(num_questions):
    ask_question()
