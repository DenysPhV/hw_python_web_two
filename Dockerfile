FROM python:3.10
ENV APP_HOME hw_python_web_two/main
WORKDIR $APP_HOME
COPY . .
ADD setup.py .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]