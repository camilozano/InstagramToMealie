FROM python:3.12-slim
LABEL authors="JoTec2002"

WORKDIR /app

COPY requirements.txt /app/

# Install required packages
RUN pip install -r requirements.txt

# Copy application code
COPY main.py /app/
COPY templates /app/templates
COPY helpers /app/helpers

# Expose the Flask port
EXPOSE 9001

# Run the application
CMD ["python", "-u", "main.py"]
