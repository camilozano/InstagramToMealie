FROM python:3.12-slim
LABEL authors="JoTec2002"

# Install required packages
RUN pip install flask instaloader pyotp waitress

# Set working directory
WORKDIR /app

# Copy application code
COPY main.py /app/
COPY templates /app/templates
COPY helpers /app/helpers

# Expose the Flask port
EXPOSE 9001

# Run the application
CMD ["python", "-u", "main.py"]