## Password help

Changing password requires three steps.

1. Open `plugin.env` and set `LDAP_BIND_USER_PASSWORD`
2. Create a hash of the password (see next section)
3. Open `bootstrap.env` and set `OPENLDAP_BOOTSTRAP_DATA_ROOT_PASSWORD_HASHED`

## Create a hash

Argon2 hashing tools are widely available online and in software packages and containers.

To see information on one of the tools, deploy with defaults and then run:
```bash
docker exec osixia/openldap:2.6.15-rc run openldap-ctl --help
```