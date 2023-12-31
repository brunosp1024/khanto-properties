FROM python:3.10-slim-buster

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

RUN chmod +x start.sh
ENTRYPOINT ["sh", "start.sh"]
