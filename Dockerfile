FROM python:3
RUN git clone https://github.com/Ignacio687/Sudoku.git
WORKDIR /Sudoku
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]