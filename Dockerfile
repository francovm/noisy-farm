FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim
# Maintainer info
LABEL maintainer="Franco Vega Mercado"

# Make working directories
WORKDIR /app

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip


# Copy application requirements file to the created working directory
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get -y update && apt-get install -y libsndfile1
# RUN apt-get install -y python3-h5py


# Copy every file in the source folder to the created working directory
COPY . .

RUN python /app/setup.py develop
# Expose the port to serve your application
EXPOSE 8080

CMD ["python", "./src/main.py"]