FROM python:3.8

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6

WORKDIR /app

COPY my-model.h5 inference.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "inference.py"]
