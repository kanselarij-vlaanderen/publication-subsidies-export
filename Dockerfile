FROM python:3.8
RUN pip install pandas lxml
COPY map.py /

CMD [ "python", "./map.py" ]