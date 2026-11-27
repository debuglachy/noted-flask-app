## Change user password

Open `75-custom.ldif` and set `userPassword`

## Change admin password

This requires three steps.

1. Open `plugin.env` and set `LDAP_BIND_USER_PASSWORD`
2. Create a hash of the password (see next section)
3. Open `bootstrap.env` and set `OPENLDAP_BOOTSTRAP_DATA_ROOT_PASSWORD_HASHED`

## Create a hash

Argon2 hashing tools are widely available online and in software packages and containers.

To perform a partial deployment and see information on one of the tools, run:
```bash
docker compose run app \
-- /bin/sh -c \
'apt update; apt install argon2; argon2 -h'
```

