# Use the official Python image as a base image

FROM python:3.9-slim

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory

WORKDIR /app

# Install system dependencies

RUN apt-get update && apt-get install -y \
 gcc \
 python3-dev \
 && apt-get clean

# Install Python dependencies

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files

COPY . /app/

# Collect static files

RUN python manage.py collectstatic --noinput

# Expose port 8000

EXPOSE 8000

# Start the Django server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
