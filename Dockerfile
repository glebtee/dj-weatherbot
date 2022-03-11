#stage to build and install packages
FROM python:3.9 as build-python

#installing pyth dependencies
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install virtualenv
RUN virtualenv /opt/venv --python=python3
RUN . /opt/venv/bin/activate && pip install -r requirements.txt
COPY . /app

#final image stage
FROM nginx/unit:1.26.1-python3.9
COPY --from=build-python /opt/venv /opt/venv
COPY --from=build-python /app /app

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"
COPY config.json /docker-entrypoint.d
COPY ~/certchain.pem /docker-entrypoint.d