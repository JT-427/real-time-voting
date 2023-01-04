# 投票結果即時顯示
> 利用WebSocket實現即時顯示投票結果
## Demo
### 投票畫面
https://user-images.githubusercontent.com/67532044/210598076-45a52209-93e7-4863-b77a-b82ff08734e6.mp4

### 投票結果
https://user-images.githubusercontent.com/67532044/210598132-43b583ee-742e-4fbc-89bc-062fe0e26e91.mp4    

(搭配OBS)

***

## Requirements
- python == 3.8
- [requirements.txt](https://github.com/JT-427/real-time-voting/blob/master/requirements.txt)

## Platform 
### Front-End
- HTML
- CSS
- JavaScript
- Socket.IO
- jQuery
### Back-End
- flask
### Database
- SQLite

## How to run on your own desktop or notebook?
### Install conda
 [https://conda.io/projects/conda/en/latest/user-guide/install/index.html](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
### Install ngrok
 [https://ngrok.com/](https://ngrok.com/)
### Create virtual environment by conda
```
conda create --name ENV_NAME python=3.8
```
### Activate virtual environment
```
conda activate ENV_NAME
```
### Install requirements
```
pip install -r requirements.txt
```
### Start server
```
gunicorn --worker-class eventlet -w 1 app:app -b 127.0.0.1:5000
```
### Start ngrok
```
ngrok http 5000
```

***

### 開發期間
2022/12/30 ~ 2022/12/31
