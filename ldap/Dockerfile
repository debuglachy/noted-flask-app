# The official osixia image version 2.6.15-rc (pushed to Docker on Oct 26, 2026) is pulled
FROM docker.io/osixia/openldap@sha256:caf6a875d6cab9543e415ac5623f1cefd20795b220a3aa896438be7eaaab02e0

# Root file is prepared for the required overwrite
USER root
RUN chown ldap:ldap /container/environment/.env.bootstrap
USER ldap

# Lines in bootstrap file are replaced with values from bootstrap secret
ENTRYPOINT ["bash", \
    "-c", \
    "for i in $(cat /run/secrets/bootstrap | awk -F= '''{print $1}'''); \
    do sed \"/$i=/d\" /container/environment/.env.bootstrap > /home/ldap/bootstrap; \
    sed -i \"1i $(grep $i /run/secrets/bootstrap)\" /home/ldap/bootstrap; \
    cat /home/ldap/bootstrap > /container/environment/.env.bootstrap; \
    done; \
    container"]

