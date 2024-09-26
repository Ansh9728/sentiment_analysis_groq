FROM python:3.12

WORKDIR /app

# Copy the requirements.txt file into the container
COPY ./requirements.txt /app/requirements.txt

# Copy the .env file into the container
COPY .env /app/.env

# Debugging step: Check if the file exists
RUN ls -l /app/requirements.txt
RUN cat /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

CMD ["fastapi", "run", "main.py", "--port", "8000"]