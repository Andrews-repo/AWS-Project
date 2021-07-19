These didn't fit in nicely anywhere but are important AWS topics you should also explore:

IAM: You should really learn how to create complex IAM Policies. You would have had to do basic roles+policies for for the EC2 Instance Role and Lambda Execution Role, but there are many advanced features.

Networking: Create a new VPC from scratch with multiple subnets (you'll learn a LOT of networking concepts), once that is working create another VPC and peer them together. Get a VM in each subnet to talk to eachother using only their private IP addresses.

KMS: Go back and redo the early EC2 instance goals but enable encryption on the disk volumes. Learn how to encrypt an AMI.

