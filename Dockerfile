FROM python:3.10-slim-bullseye
COPY . .
RUN pip install -r requirements.txt
CMD ["python","hw_python_web_two/main.py"]
EXPOSE 5000

