# Use the Python image
FROM python:3.9.19-slim-bullseye

# Set working directory in the container
WORKDIR /chatbot

# Copy the Python scripts and other files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV ACCESS_TOKEN=6947069686:AAEvzu1IP02XqqCePzgrrv0PtgY9U8FOjB4
ENV BASICURL=https://chatgpt.hkbu.edu.hk/general/rest
ENV MODELNAME=gpt-4-turbo
ENV APIVERSION=2024-02-15-preview
ENV ACCESS_TOKEN1=ef15e917-cf31-41d1-a897-9ae9c710f1b5

# Set the entrypoint
CMD python chatbot.py

