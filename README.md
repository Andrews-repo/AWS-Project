# Hello
Hey,
Thanks for checking out my repo.
This repo is where I store all the code I write and use to build things within AWS.
I didnt have any forethought in the way the directories were named, and how they would appear long term, so I will attempt to guide you through what you're looking at with links below.

Quick tip: The "Code" links take you to the code used for each assignment/step, as well as the description of each assignment/step.
The "Title" links, take you to a brief descrption of what I needed to do/learn. 

# Table of Contents

* [Project Overview](#Project-Overview) 

* [Account Basics](#Account-Basics): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Account%20Basics) "Done"

* [Web Hosting Basics](#Web-hosting-basics): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Basic%20Web%20Host) "Done"

* [Auto Scaling](#auto-scaling): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/AutoScaling) "Done"

* [External Data](#External-Data): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/External%20Data) "Done"

* [Web Hosting Platform as a Service](#web-hosting-platform-as-a-service): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Web%20Hosting%20-%20Platform%20as%20a%20Service) "Done"

* [Microservices](#Microservices): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Microservices) "Done"

* [Serverless](#Serverless): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Serverless)

* [Cost Analysis](#Cost-Analysis): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Cost%20Analysis)

* [Automation](#Automation)

* [Continuous Delivery](#Continuous-Delivery): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/CICD)

* [Miscellaneous and Bonus](#Miscellaneous-and-Bonus): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Miscellaneous%20and%20Bonus)

# Project Overview
I needed a project to learn AWS services after being certified. I found this [post](https://www.reddit.com/r/sysadmin/comments/8inzn5/so_you_want_to_learn_aws_aka_how_do_i_learn_to_be/), which roughly states:
"This uses a website as an excuse to use a number of AWS technologies. Its a rough guide of the the maturity process of the most basic webpafe, to an extremely cheap and scalable web application." Essectially its a list of tasks I *should* be able to do while building an app on AWS, but doesnt provide any directions on how to do so.

The idea for said web appliaction, is a "Fortune of the day" site. A page that, on site load, loads a random fortune from a database, and allows users to add their own fortune to said database.  

# Account Basics
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Account%20Basics) "Done" 

This section was focused around setting up a new account and establishing basic AWS security and account recomendations. It has been automated via CloudFormation, but I do need to come back and document how to do some of these things via the CLI.

# Web Hosting Basics
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Basic%20Web%20Host) "Done"   

Learned NGINX, and set up a reverse proxy. Learned VPC. Automated the set up of a basic site, VPC, and the install of an NGINX server. 

# Auto Scaling
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/AutoScaling) "Done"

I have two scripts that automate the previous website, from an AMI, into both target tracking, and simple scaling policies from a launchtemplate.

# External Data
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/External%20Data) "Done"

Leaned how to set up a NodeJS app. Really learned how to use CloudFormation to set up servers and install software. Learned front end development and built 4-5 webpages. 

# Web Hosting Platform as a Service "Done"
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Web%20Hosting%20-%20Platform%20as%20a%20Service) "Done"

Got to move the project into Elastic Beanstalk. There was some challenges as far as getting the configuration files set properly. Got to learn how to serve files from private S3 buckets. Learned Route53 and setting domain names. Learned TLS/SSl and forcing https in AWS. 

# Microservices
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Microservices) "Done"

Built an API with NodeJS, and another with api gateway. Really had to figure out how to use express. Learned a little bit of jQuery. Learned how to host sites in S3 that run css and JS. Learned how to set domains to CloudFront and resolve CNAME to Cloudfront Distributions. The backend of the code Is done, the front end needs a little tidying up that I will do soon. 

# Serverless
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Serverless)

Ok so far this has been fun. Issues so far:
- i dont know python
    - "fixed" I can read it and i wrote my first lambda function in Python.
- "Handler 'lambda_handler' missing on module 'lambda_function" 
    - "fixed" by putting the code In the correct place in a lambda function.
- "errorMessage": "name 'boto3' is not defined" 
    - "fixed" becasue Im silly and forgot to import boto3
- "errorMessage": "An error occurred (AccessDenied) when calling the SendEmail operation" 
    - "fixed" by adding the proper IAM privileges.
- python "return" exits function after returning first item
    - "fixed" using yield and appending items to a variable in python. 

# Cost Analysis
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Cost%20Analysis)

Havent Started. 

# Automation

Theres no link to this section as part of the entire point of working with the cloud is automation, and thats all listed here. If I do add this section it will be to showcase some new automation technology I havent done before like ansible. 

# Continuous Delivery
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/CICD)

Havent started, but ive used CodePipeline before so Im brainstorming when i could start implementing it again. 

# Miscellaneous and Bonus
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Miscellaneous%20and%20Bonus)

Im half way through this section will update with more details. 


