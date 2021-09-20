FROM python:3.6
WORKDIR /app
COPY requiremnet.txt /app
RUN pip3 install -r requiremnet.txt
COPY . /app
ENTRYPOINT ["streamlit", "run", "app.py"] 