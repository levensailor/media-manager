# Use an official Python runtime as a parent image
FROM python:3.8.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Set PYTHONPATH to include /app
ENV PYTHONPATH /app

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Install Cron
RUN apt-get update && apt-get -y install cron

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
