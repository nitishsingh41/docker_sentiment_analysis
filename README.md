# Sentiment analysis streamlit app deployment with docker
## AWS Instance and Docker deployment commands
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
sudo apt  install docker.io 
sudo apt install git
sudo service docker start
sudo docker build -t bert_streamlit_docker .
sudo docker run -d -p 8501:8501 bert_streamlit_docker
