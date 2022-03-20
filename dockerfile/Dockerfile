# centos:stream8
FROM quay.io/centos/centos:stream8

COPY requirements.txt /

RUN \
    dnf -y install \
      python38 \
      sqlite \
    && \
    dnf clean all \
    && \
    python3 -m pip install -r requirements.txt

WORKDIR /workspace/django-testing-tutorial

EXPOSE 8000/tcp

CMD ["python3", "/workspace/django-testing-tutorial/manage.py", "runserver", "0.0.0.0:8000"]
