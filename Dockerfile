FROM python:3.11.0

ADD main.py .

RUN pip install scikit-learn

CMD ["python", "./main.py"]