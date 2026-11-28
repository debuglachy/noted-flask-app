# Custom setup (optional)

---

## Change the user login

1. Open `75-custom.ldif` and set `uid` and/or `userPassword`

---

## Change the admin password

1. Open `plugin.env` and set `LDAP_BIND_USER_PASSWORD`
2. [Create a hash](#create-a-hash) of the password
3. Open `bootstrap.env` and set `OPENLDAP_BOOTSTRAP_DATA_ROOT_PASSWORD_HASHED`

---

## Redefine LDAP setup

1. Modify `bootstrap.env` and `plugin.env` values.
2. Adjust the directory file in `ldif-data`.

---

## Create a hash

Argon2 hashing tools are widely available online and in software packages and containers.

To perform a partial deployment and see information on one of the tools, run:
```bash
docker compose run app \
-- /bin/sh -c \
'apt update; apt install argon2; argon2 -h'
```

