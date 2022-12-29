FROM python:3.10
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 APP_HOME=/microservice HOST=0.0.0.0 PORT=5000
RUN mkdir $APP_HOME
WORKDIR $APP_HOME/
COPY  requirements.txt /tmp/
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt
ADD . $APP_HOME/
EXPOSE $PORT
