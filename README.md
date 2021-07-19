# Hello
Hey,
Thanks for checking out my repo.
This repo is where I store all the code I write and use to build things within AWS.
I didnt have any forethought in the way the directories were named, and how they would appear long term, so I will attempt to guide you through what you're looking at with links below.

Quick tip: The "Code" links take you to the code used for each assignment/step, as well as the description of each assignment/step.
The "Title" links, take you to a breif descrption of what I needed to do/learn. 

# Table of Contents

[Project Overview](#Project-Overview) 

[Account Basics](#Account-Basics): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Account%20Basics)

[Web Hosting Basics](#Web-hosting-basics): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Basic%20Web%20Host)

[Auto Scaling](#auto-scaling): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/AutoScaling)

[External Data](#External-Data): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/External%20Data)

[Web Hosting Platform as a Service](#web-hosting-platform-as-a-service): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Web%20Hosting%20-%20Platform%20as%20a%20Service)

[Microservices](#Microservices): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Microservices)

[Serverless](#Serverless): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Serverless)

[Cost Analysis](#Cost-Analysis): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Cost%20Analysis)

[Automation](#Automation)

[Continuous Delivery](#Continuous-Delivery): [Code](https://github.com/Andrews-repo/AWS-Project/tree/master/CICD)

[Miscellaneous and Bonus](#Miscellaneous-and-Bonus)

# Project Overview
I needed a project to learn AWS services after being certified. I found this [post](https://www.reddit.com/r/sysadmin/comments/8inzn5/so_you_want_to_learn_aws_aka_how_do_i_learn_to_be/), which roughly states:
"This uses a website as an excuse to use a number of AWS technologies. Its a rough guide of the the maturity process of the most basic webpafe, to an extremely cheap and scalable web application."

The idea for said web appliaction, is a "Fortune of the day" site. A page that, on site load, loads a random fortune from a database, and allows users to add their own fortune to said database.  

# Account Basics
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Account%20Basics)

This section was focused around setting up a new account and establishing basic AWS security and account recomendations. It has been automated via cloudformation, but I do need to come back and document how to do some of these things via the CLI.

# Web Hosting Basics
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Basic%20Web%20Host)

I think "web hosting basics" is pretty vague. This could incorporate reverse proxies, as well as being able to create a VPC network. I am going to assume both, and need to add script to automate both of these. What is done, is the script to automate a basic static website hosted with apache.  I would like to add the automation of an AMI snapshot. 

# Auto Scaling
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/AutoScaling)

I have two scripts that automate the previous website, from an AMI,  into both target target tracking and simple scaling policies from a launchtemplate.

# External Data
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/External%20Data)

This one has been tough, i got stuck a couple different times. Once i was troubleshooting a syntax error for far too long, simply overlooking the error. The other issue, is that secondary instances of my website overwrite each others entries. I have some ideas on how to solve it, seemingly issues with my node.js, but ill save that for later when I do deep dives on different code languages. 

# Web Hosting Platform as a Service
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Web%20Hosting%20-%20Platform%20as%20a%20Service)

Done. Will be updating a small description here soon.

# Microservices
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Microservices)

Half way done. need to get rid of server.

# Serverless
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Serverless)

Havent Started. 

# Cost Analysis
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/Cost%20Analysis)

Havent Started. 

# Automation

Theres no link to this section as part of the entire point of working with the cloud is automation, and thats all listed here. If I do add this section it will be to showcase some new automation technology I havent done before like ansible. 

# Continuous Delivery
[Code](https://github.com/Andrews-repo/AWS-Project/tree/master/CICD)

Havent started, but ive used CodePipeline before so Im brainstorming when i could start implementing it again. 

# Miscellaneous and Bonus

Im half way through this section will update with more details. 


