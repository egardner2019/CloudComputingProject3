FROM python:3.12-alpine
ADD main.py .
CMD ["python", "./main.py"]
