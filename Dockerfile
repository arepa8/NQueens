FROM python:3
ADD nqueens.py /
ADD nqueens_test.py /
ADD models.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./nqueens.py" ]