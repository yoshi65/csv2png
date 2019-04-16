# csv2png

## SETTING
1. dockerのインストール
1. python3.6のインストール
1. pipのインストール
1. aws-sam-cliのインストール
    ```sh
    % pip install awscli aws-sam-cli
    ```
1. awsの初期設定
    ```sh
    % aws configure
    AWS Access Key ID: 
    AWS Secret Access Key:
    Default region name: ap-northeast-1
    Default output format:
    ```

## Test in ubuntu18.04 on Docker
1. build docker image
    ```sh
    % docker build -t test_image .
    ```
1. run docker
    ```sh
    % AWS_ACCESS_KEY_ID=""
    % AWS_SECRET_ACCESS_KEY=""
    % AWS_DEFAULT_REGION="ap-northeast-1"
    % docker run -it --rm --privileged \
        -v /var/lib/docker \
        -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
        -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
        -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
        test_image /bin/bash
    ```
1. make endpoint
    ```sh
    # export LC_ALL=C.UTF-8
    # export LANG=C.UTF-8
    # service docker start
    # git clone https://github.com/yoshi65/csv2png
    # cd ./csv2png
    # sam build
    # sam local start-api
    ```
1. post csv file
    ```sh
    % docker exec -it ${CONTAINER ID} /bin/bash
    # cd ./csv2png
    # curl -H "Accept: image/png" -H "Content-Type: text/csv" --data-binary "@test.csv" -X POST http://127.0.0.1:3000/src -o test.png
    ```
1. copy png file in host and open png file
    ```sh
    % docker cp ${CONTAINER ID}:/csv2png/test.png .
    % open test.png
    ```
