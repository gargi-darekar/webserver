# Web Server

This project is developed in fulfillment of the "Project Based Learning" course of the fourth semester of the Bachelor of Computer Engineering degree from Savitribai Phule Pune University (formerly Pune University).

## Overview

The Web Server Project is a containerized application that consists of a Flask backend and an NGINX reverse proxy. The project leverages Docker to simplify deployment and ensure consistency across environments.

## Project Structure

The project is organized as follows:

- **`docker-compose.yml`**: Defines the multi-container application, including the backend service and the NGINX reverse proxy.
- **`Dockerfile`**: Specifies the build instructions for the backend service, which is implemented in Python.
- **`backend/`**: Contains the backend application code and its dependencies.

## Components

### Backend Service

The backend service is built using Python 3.11 and is defined in the `Dockerfile`. It includes the following features:

- A working directory set to `/app`.
- Dependencies managed via a `requirements.txt` file.
- The application is exposed on port `5000` and executed using the `app.py` script.

### NGINX Reverse Proxy

The NGINX service acts as a reverse proxy for the backend. It is configured using the `default.conf` file, which is mounted into the container at `/etc/nginx/conf.d/default.conf`. The NGINX service listens on port `80` and forwards requests to the backend service.

## Prerequisites

To run this project, ensure the following software is installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Usage

Follow these steps to build and run the project:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to start the services:

   ```bash
   docker-compose up --build
   ```

4. Access the application in your browser at `http://localhost`.

## File Descriptions

### `docker-compose.yml`

This file defines the services required for the application:

- **`backend`**: The Python-based backend service.
- **`nginx`**: The NGINX reverse proxy service.

### `Dockerfile`

The `Dockerfile` contains the instructions to build the backend service image. It installs the required dependencies and sets up the application to run on port `5000`.

## Acknowledgments

This project was developed as part of the academic curriculum of Savitribai Phule Pune University. Special thanks to the faculty and peers for their guidance and support.