[![.github/workflows/ci.yaml](https://github.com/debuglachy/noted-flask-app/actions/workflows/ci.yaml/badge.svg)](https://github.com/debuglachy/noted-flask-app/actions/workflows/ci.yaml) ![coverage](https://raw.githubusercontent.com/debuglachy/noted-flask-app/python-coverage-comment-action-data/badge.svg)
![release](https://img.shields.io/github/v/tag/debuglachy/noted-flask-app)

# noted-flask-app

Simple web app for writing notes from different devices into persistent storage.

![Animation demonstrating the noted flask app being used in Firefox.](https://github.com/debuglachy/ops/blob/main/writeups/writeup-noted-flask-app-design.gif)

---

## Description

* Securely connects with users
* Starts a sidecar container to validate logins
* Parses and persistently stores data entries
* Containerised for deployments scaling

> [!NOTE]
> See the [design document](https://github.com/debuglachy/ops/blob/main/writeups/writeup-noted-flask-app-design.md) for more information.

---

## Quick Start Guide

1. Clone repo > Open `certs` folder > Generate `server.crt` and `server.key`

2. Open `setupfiles` folder > Remove `.example` from `bootstrap.env.example` and `plugin.env.example`

3. Deploy and run:
   ```bash
   docker compose up
   ```

4. Open `https://127.0.0.1:8080` or `https://<host-ip>:8080` in the browser

5. Login with username `jdoe` and password `password`

> [!TIP]
> See the [guide](setupfiles/README.md) on how to run a non-default setup.

---

## Prerequisites

Docker

---

## Author & License

Developed by Lachlan Christie as a lab demo.

See the [design document](https://github.com/debuglachy/ops/blob/main/writeups/writeup-noted-flask-app-design.md).

Refer to the [LICENSE](LICENSE).


