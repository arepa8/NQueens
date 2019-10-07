FROM python:3
ADD nqueens.py /
CMD [ "python", "./nqueens.py" ]