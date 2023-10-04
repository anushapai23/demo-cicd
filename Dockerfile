FROM python:3
ADD ./testsum.py .
CMD ["python3", "testsum.py"]