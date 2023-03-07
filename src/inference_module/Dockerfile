FROM python:3.9.16

WORKDIR /inference_module

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

EXPOSE 5000