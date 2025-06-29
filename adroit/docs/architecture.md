# Adroit Services - Architecture Overview

## Purpose

Adroit Services is a collection of RESTful business APIs designed to expose core business functionality to clients in a secure and scalable way.

## Components

- **API Gateway**: Handles client requests and routes them to the correct service.
- **Authentication Service**: Manages client authentication and authorization.
- **Business Services**: Implements business logic for various domains.
- **Data Layer**: Interfaces with databases and other persistent storage systems.

## Technology Stack

- Python 3.12
- Flask
- TODO Add reverse proxy (e.g. Caddy)
- TODO Add WSGI (e.g. Waitress)

## Deployment

The system will be deployed to an AWS EC2 container.  

## Future Enhancements

- API documentation with Swagger
- Automated CI/CD pipelines
- Monitoring with Prometheus + Grafana TO DO Investigate Datadog
- HTTPS

_Last updated: 2025-06-28_