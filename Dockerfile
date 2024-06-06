FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip3 install torch==2.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
