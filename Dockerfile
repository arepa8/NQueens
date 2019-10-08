FROM python:3
ADD nqueens.py /
RUN pip install SQLAlchemy
RUN pip install pytest
CMD [ "python", "./nqueens.py" ]