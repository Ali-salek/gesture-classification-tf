FROM tensorflow/tensorflow:latest-jupyter

RUN python -m pip install pandas
RUN python -m pip install scikit-learn

RUN mkdir -p /program

WORKDIR /program
COPY app.py /program/app.py

CMD ["python", "/program/app.py"]