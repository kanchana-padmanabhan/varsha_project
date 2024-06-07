docker build -t mudita_test . 
docker run -d -p 8501:8501 mudita_test 
curl http://0.0.0.0:8501    