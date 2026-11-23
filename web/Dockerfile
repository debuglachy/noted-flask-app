FROM python:3.12-slim

# non-root directory prepared
RUN useradd --create-home noted-flask
WORKDIR /home/noted-flask

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --upgrade --force-reinstall -r requirements.txt

COPY --chown=noted-flask:noted-flask . .
# app is installed as python package
RUN python3 -m pip install /home/noted-flask

# edit ENV and fallback values in app.py and setupfiles/plugin.env when changing EXPOSE value
ENV NOTED_APP_PORT=8080
EXPOSE 8080

CMD . /run/secrets/plugin; python3 -m gunicorn app:app --workers 4 --config /home/noted-flask/gunicorn.conf.py --user noted-flask ; unset LDAP_BIND_USER_PASSWORD SECRET_KEY LDAP_USERNAME LDAP_PASSWORD
