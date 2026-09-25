# AWS Three-Tier Web Application

## Project Overview

This project demonstrates the deployment of a simple three-tier web application on AWS. The goal was to gain hands-on experience with AWS infrastructure, networking, security, compute, database connectivity, and application deployment.

The application uses an Amazon EC2 instance to host the web/application layer and Amazon RDS for the database layer. A Python Flask application connects the web server to the database and displays data through a web interface.

## Architecture

The project follows a three-tier architecture:

1. **Presentation Tier** – Web interface accessible through a browser.
2. **Application Tier** – Python Flask application running on Amazon EC2.
3. **Database Tier** – Amazon RDS database used to store application data.

## AWS Services and Technologies Used

- Amazon EC2
- Amazon RDS
- Amazon VPC
- Security Groups
- Linux
- Apache Web Server
- Python
- Flask
- SQL
- SSH
- GitHub

## Project Implementation

### 1. EC2 Web Server

- Launched an Amazon EC2 instance.
- Configured the instance security group.
- Allowed HTTP traffic on port 80.
- Connected to the EC2 instance using SSH.
- Installed and configured the Apache web server.
- Verified that the web server was accessible from a browser.

### 2. Application Layer

- Installed Python and Flask on the EC2 instance.
- Created a simple Flask web application.
- Configured the application to communicate with the database.
- Tested the application from the web browser.

### 3. RDS Database

- Created an Amazon RDS database.
- Configured database networking and security.
- Created the required database and table.
- Connected the EC2 application server to the RDS database.
- Tested database connectivity from the application layer.

### 4. Security

- Used AWS Security Groups to control network access.
- Allowed HTTP traffic for the web application.
- Restricted database access so that the application server could communicate with the database.
- Used separate security rules for the web/application and database layers.

## Request Flow

User Browser  
↓  
Amazon EC2 / Web Server  
↓  
Python Flask Application  
↓  
Amazon RDS Database

## What I Learned

Through this hands-on project, I practiced:

- Deploying and configuring EC2 instances.
- Working with Amazon RDS.
- Configuring AWS Security Groups.
- Understanding communication between application and database layers.
- Connecting to Linux servers using SSH.
- Installing and configuring a web server.
- Deploying a Python Flask application.
- Troubleshooting connectivity between AWS resources.
- Understanding the fundamentals of three-tier cloud architecture.

## Future Improvements

Future versions of this project can include:

- Application Load Balancer
- Auto Scaling
- Multi-AZ database deployment
- Private subnets for the database layer
- HTTPS using AWS Certificate Manager
- Route 53 DNS
- CloudWatch monitoring
- Infrastructure as Code using AWS CloudFormation or Terraform

## Project Status

Hands-on AWS cloud project completed as part of my AWS learning and cloud engineering portfolio.
