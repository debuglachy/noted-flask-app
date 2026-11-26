FROM docker.io/osixia/openldap:2.6.15-rc

# Get root file ready to be overwritten
USER root
RUN chown ldap:ldap /container/environment/.env.bootstrap
USER ldap

# Replaces lines in bootstrap file with values being passed in the secret
ENTRYPOINT ["bash", \
    "-c", \
    "for i in $(cat /run/secrets/bootstrap | awk -F= '''{print $1}'''); \
    do sed \"/$i=/d\" /container/environment/.env.bootstrap > /home/ldap/bootstrap; \
    sed -i \"1i $(grep $i /run/secrets/bootstrap)\" /home/ldap/bootstrap; \
    cat /home/ldap/bootstrap > /container/environment/.env.bootstrap; \
    done; \
    container"]

