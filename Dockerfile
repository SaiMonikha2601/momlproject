# 1. Use Python as the base image
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy your code into the container
COPY . /app

# 4. Install dependencies
RUN pip install -r requirements.txt

# 5. Tell Docker how to run your app
CMD ["python", "app.py"]
