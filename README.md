[![.github/workflows/ci.yaml](https://github.com/debuglachy/noted-flask-app/actions/workflows/ci.yaml/badge.svg)](https://github.com/debuglachy/noted-flask-app/actions/workflows/ci.yaml)

![coverage](https://raw.githubusercontent.com/debuglachy/noted-flask-app/python-coverage-comment-action-data/badge.svg)

![release](https://img.shields.io/github/v/tag/debuglachy/noted-flask-app)

# noted-flask-app

Simple web app for writing notes. Saves to persistent storage.

---

## Description

* Page runs on Python with Flask imported
* Containerised for deployments scaling
* Parses invalid form submissions

---

## Quick Start Guide

Run the application:
```bash
docker run -p 80:8080 ghcr.io/debuglachy/noted-flask-app:main
```

Or deploy and run:
```bash
docker-compose up
```

Or use a custom port (defaults to 8080):
```bash
NOTED_APP_PORT=8080 docker-compose up
```

---

## Prerequisites

Docker

---

## Author & License

Developed by Lachlan Christie as a lab demo.

Refer to the [LICENSE](LICENSE).


