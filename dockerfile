FROM python:3.7-alpine
# directory for work
WORKDIR /app
# configuration enviroment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
# Copy requirements to docker container
COPY requirements.txt requirements.txt
# Install requirements on docker container
RUN pip3 install -r requirements.txt
# Expose port 3000 of container
EXPOSE 3000
COPY . .
# run flask server
CMD ["flask", "run"]