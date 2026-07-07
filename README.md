
# 🛋️ Furnish Fusion - Cloud-Based Furniture E-Commerce Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask)
![AWS](https://img.shields.io/badge/Cloud-AWS-orange?style=for-the-badge&logo=amazonaws)
![Amazon EC2](https://img.shields.io/badge/Hosting-EC2-yellow?style=for-the-badge)
![Amazon DynamoDB](https://img.shields.io/badge/Database-DynamoDB-blue?style=for-the-badge)
![Amazon SNS](https://img.shields.io/badge/Notification-SNS-success?style=for-the-badge)
![HTML5](https://img.shields.io/badge/Frontend-HTML5-orange?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/Style-CSS3-blue?style=for-the-badge&logo=css3)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap-purple?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 🌟 Project Overview

**Furnish Fusion** is a cloud-based furniture e-commerce platform developed using **Python Flask** and deployed on **Amazon Web Services (AWS)**.

The application enables customers to browse furniture products, manage wishlists and shopping carts, place orders securely, and receive real-time email notifications. An integrated admin dashboard allows administrators to manage products, monitor orders, and oversee the entire platform from a centralized interface.

The project demonstrates practical implementation of modern cloud technologies by integrating **Amazon EC2**, **Amazon DynamoDB**, **Amazon SNS**, and **AWS IAM** into a scalable two-tier web application architecture.

---

## 🎯 Project Objectives

- Develop a complete cloud-based furniture shopping platform.
- Deploy a Flask web application on AWS EC2.
- Store application data using Amazon DynamoDB.
- Implement secure user authentication and authorization.
- Send automated order confirmation emails using Amazon SNS.
- Build an admin dashboard for centralized management.
- Demonstrate practical cloud deployment using AWS services.

---

# 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [AWS Architecture](#-aws-architecture-overview)
- [Technology Stack](#-technology-stack)
- Installation Guide
- Project Structure
- Deployment
- Application Workflow
- Screenshots
- Future Improvements
- Author

---

# ✨ Key Features

## 👤 User Features

- Secure User Registration
- User Login & Authentication
- Browse Furniture Products
- Category-wise Product Listing
- Wishlist Management
- Shopping Cart
- Budget Planner
- Checkout System
- Order Placement
- Order History
- Order Tracking
- Profile Management
- Email Notifications

---

## 🛠️ Admin Features

- Secure Admin Login
- Dashboard Analytics
- Product Management
- Add Products
- Update Products
- Delete Products
- Order Management
- Customer Monitoring
- Revenue Tracking
- Coupon Management
- UPI Configuration

---

## ☁️ Cloud Features

- AWS EC2 Deployment
- Amazon DynamoDB Database
- Amazon SNS Notifications
- IAM Role-Based Access
- Secure Security Groups
- Scalable Cloud Infrastructure

---

# ☁️ AWS Architecture Overview

The application follows a **Two-Tier Cloud Architecture** where the presentation layer and application logic are hosted on an Amazon EC2 instance while application data is stored in Amazon DynamoDB.

```
                    +----------------------+
                    |      Web Browser     |
                    +----------+-----------+
                               |
                               |
                         HTTP Requests
                               |
                               ▼
                    +----------------------+
                    |      AWS EC2         |
                    | Flask Web Application|
                    +----------+-----------+
                               |
         ----------------------------------------------
         |                     |                      |
         ▼                     ▼                      ▼
+----------------+     +----------------+     +----------------+
| DynamoDB       |     | Amazon SNS     |     | AWS IAM        |
| User Data      |     | Email Alerts   |     | Access Control |
| Orders         |     | Order Updates  |     | Permissions    |
| Products       |     | Registration   |     | Security       |
+----------------+     +----------------+     +----------------+
```

---

## 🔄 Application Workflow

```
User Registration
        │
        ▼
User Login
        │
        ▼
Browse Products
        │
        ▼
Add to Cart / Wishlist
        │
        ▼
Checkout
        │
        ▼
Order Stored in DynamoDB
        │
        ▼
SNS Sends Confirmation Email
        │
        ▼
Admin Reviews Order
        │
        ▼
Customer Tracks Order
```

---

# 💻 Technology Stack

| Category | Technologies Used |
|-----------|-------------------|
| Programming Language | Python 3 |
| Backend Framework | Flask |
| Frontend | HTML5, CSS3, Bootstrap, JavaScript |
| Database | Amazon DynamoDB |
| Cloud Platform | Amazon Web Services (AWS) |
| Hosting | Amazon EC2 |
| Notification Service | Amazon SNS |
| Security | AWS IAM |
| Version Control | Git & GitHub |
| IDE | Visual Studio Code |

---

# 🏆 AWS Services Used

| AWS Service | Purpose |
|--------------|---------|
| Amazon EC2 | Hosts the Flask application |
| Amazon DynamoDB | Stores users, products, carts and orders |
| Amazon SNS | Sends registration and order confirmation emails |
| AWS IAM | Controls secure access to AWS resources |
| Security Groups | Protect network traffic to the EC2 instance |

---

## 📌 Repository Status

| Status | Value |
|---------|-------|
| Project Type | Academic Capstone Project |
| Deployment | AWS Cloud |
| Architecture | Two-Tier Architecture |
| Backend | Flask |
| Database | Amazon DynamoDB |
| Cloud Services | EC2, SNS, IAM |
| Current Status | Completed ✅ |



