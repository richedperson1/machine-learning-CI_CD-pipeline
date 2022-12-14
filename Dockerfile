FROM python:3.7
COPY . ./

WORKDIR /

RUN pip install -r requirements.txt

EXPOSE 5000

# ENTRYPOINT [ "python" ]

CMD ["python","app.py"]