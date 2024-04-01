FROM python:3.9-slim
WORKDIR /app
COPY *.py requirements.txt ./ 
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]

