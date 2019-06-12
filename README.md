# csv2png
Translate CSV format data to PNG format graph, using aws sam.
In this repository, provide environment of test in local, and deploy on mac OS using docker container.

## How to deploy
1. build docker image
    ```sh
    % docker build -t deploy_image -f Dockerfile_deploy .
    ```
1. deploy
    ```sh
    % docker run -it --rm --privileged \
        -v /var/lib/docker \
        -e AWS_ACCESS_KEY_ID=`grep "aws_access_key_id" ~/.aws/credentials | awk '{print $3}'` \
        -e AWS_SECRET_ACCESS_KEY=`grep "aws_secret_access_key" ~/.aws/credentials | awk '{print $3}'` \
        -e AWS_DEFAULT_REGION=`grep "region" ~/.aws/config | awk '{print $3}'` \
        -e bucket_name=${your_bucket_name} \
        deploy_image
    ```
1. get endpoint
    ```sh
    % endpoint=`aws cloudformation describe-stacks --stack-name csv2png --query 'Stacks[].Outputs' | jq -r '.[0][2].OutputValue'
    ```
1. test
    ```sh
    % curl -H "Accept: image/png" -H "Content-Type: text/csv" --data-binary "@test.csv" -X POST ${endpoint} -o test.png
    ```

## Test in ubuntu18.04 on Docker
1. build docker image
    ```sh
    % docker build -t test_image -f Dockerfile_test .
    ```
1. run docker for making endpoint
    ```sh
    % docker run -it --rm --privileged \
        -v /var/lib/docker \
        --hostname test_container \
        --name test_container \
        -e AWS_ACCESS_KEY_ID="" \
        -e AWS_SECRET_ACCESS_KEY="" \
        -e AWS_DEFAULT_REGION=`grep "region" ~/.aws/config | awk '{print $3}'` \
        test_image
    ```
1. post csv file
    ```sh
    % docker exec -it test_container curl -H "Accept: image/png" -H "Content-Type: text/csv" --data-binary "@/csv2png/test.csv" -X POST http://127.0.0.1:3000/src -o test.png
    ```
1. copy png file in host and open png file
    ```sh
    % docker cp test_container:/test.png .
    % open test.png
    ```

## Dependencies
* docker
* python3.6
* pip
* boto3
* aws-sam-cli
    ```sh
    % pip install awscli aws-sam-cli
    % aws configure
    AWS Access Key ID: 
    AWS Secret Access Key:
    Default region name: ap-northeast-1
    Default output format:
    ```
