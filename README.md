# Rental Gateway

## INTRODUCTION

### 1.1. Purpose

• Creating a house rental gateway where property owners,
clients, and customers can easily and affordably
communicate information.
• Landlords can list their property and its images, price,
location, and filters (suitable tenant).
• Tenants can search through the listings according to their
requirements such as location, budget, and availability.

### 1.2. Intended audience

• Students
• Workers
• Property owners
• Families
• Bachelors

### 1.3. Scope

• Seamless listing and searching of properties
• Provides a platform for landlords and tenants to find a
property and earn money respectively.
• It creates a database from the inputs from landlords and
allows tenants to search that database as per their
requirements using a user interface.


## OVERALL DESCRIPTION

### 2.1. User needs

• This website is to cater to the needs of people trying to
make a quick buck by using their property and the
students and workers living away from their families.

### 2.2. Technology and platform used (frontend and
backend)

• Frontend: Html, CSS, javascript , react
• Backend: Flask, sqllite

### 2.3. Assumptions and Dependencies

• Assumptions: - The data entered by the owner is
authentic. Spamming will not happen there.
• Dependencies: - site is client-side dependent, Web-
dependent

### Setup

1)First you need to setup docker compose on your system refer [docker-compose installation](https://docs.docker.com/compose/install/)
2)
```
$   docker-compose up
```

### initialise the db by 

1) Open a new terminal 
```
$   cd app
    python3
    from app.py import db
    db.create_all() 
```
