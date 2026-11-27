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

3. Change defaults (optional):
   - Make desired password and LDAP changes to `bootstrap.env` and `plugin.env` values.
   - When making changes to LDAP settings, also adjust the directory file in `ldif-data`.

     > [!TIP]
     > See [password help](setupfiles/passwordhelp.md) and remember to generate hash when making changes to password.

4. Deploy and run:
   ```bash
   docker compose up
   ```

---

## Prerequisites

Docker

---

## Author & License

Developed by Lachlan Christie as a lab demo.

See the [design document](https://github.com/debuglachy/ops/blob/main/writeups/writeup-noted-flask-app-design.md).

Refer to the [LICENSE](LICENSE).


