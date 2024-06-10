# Sentiment analysis streamlit app deployment with docker
## AWS Instance and Docker deployment commands
### Install necessary packages
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

### Install Docker
sudo apt install docker.io

# Install Git
sudo apt install git

# Start Docker service
sudo service docker start

# Build Docker image
sudo docker build -t bert_streamlit_docker .

# Run Docker container
sudo docker run -d -p 8501:8501 bert_streamlit_docker
