# 1. Base image
FROM python:3.12-slim

# 2. Working directory in the container
WORKDIR /app

# 3. Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the source code
COPY . .

# 5. Expose port
EXPOSE 5000

# 6. Start the app with Gunicorn
#   app.main:app  ->  module:object (from app/main.py)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.main:app"]
