FROM python:3.12-alpine

WORKDIR /app

# Disable bytecode and don't buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app/app.py .

# Create non-root user
RUN adduser -D appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 6969

# Run with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:6969", "-w", "2", "app:app"]
