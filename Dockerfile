FROM python:3.10
#ENV APP_HOME hw_python_web_two/main.py
#WORKDIR $APP_HOME
COPY . .
RUN pip install -r requirements.txt
CMD ["python","hw_python_web_two/main.py"]
EXPOSE 5000

