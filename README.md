# sample

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

## 動作確認
Vagrantを用いて、ubuntu18.04(bionic64)における動作確認を行なった。
```sh
% vagrant up
% vagrant ssh
```

### 各種インストールについて
1. dockerのインストール及び起動
    ```sh
    % sudo apt-get update
    % sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common gcc
    % curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    % sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable test edge"
    % sudo apt-get update
    % sudo apt-get install -y docker-ce
    
    % sudo systemctl start docker
    % sudo systemctl enable docker
    ```
1. pipのインストール
    ```sh
    % curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    % sudo apt install -y python3-distutils
    % sudo python3 get-pip.py
    % sudo pip install --upgrade pip
    ```
1. aws-sam-cliのインストール
    ```sh
    % sudo apt install -y python3-dev
    % sudo pip install awscli aws-sam-cli
    ```
1. awsの初期設定
    ```sh
    % aws configure
    ```

### 実行について
1. エンドポイント作成
```sh
% cd ./sample
% sam local start-api
```
1. csvファイルをPOSTして、レスポンスを受け取る
```sh
% curl -H "Accept: image/png" -H "Content-Type: text/csv" --data-binary "@test.csv" -X POST http://127.0.0.1:3000/src -o test.png
```

### 補足
1. デスクトップ画面を出力
    ```sh
    % sudo apt-get install ubuntu-desktop
    % sudo reboot
    ```
