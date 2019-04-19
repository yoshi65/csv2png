FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common gcc && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable test edge" && \
    apt-get install -y docker-ce && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    apt install -y python3-distutils && \
    python3 get-pip.py && \
    pip install --upgrade pip && \
    apt install -y python3-dev && \
    pip install awscli aws-sam-cli 

CMD export LC_ALL=C.UTF-8 && \
    export LANG=C.UTF-8 && \
    service docker start && \
    git clone https://github.com/yoshi65/csv2png && \
    cd ./csv2png && \
    sam build && \
    sam local start-api
