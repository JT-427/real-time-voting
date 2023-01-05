# 利用WebSocket實現即時顯示投票結果
## Demo
1. 輸入名字後，即可進行投票。    
2. 使用者投票後，螢幕上就會即時地以長條圖和數字來呈現目前的得票數。   
 
![DEMO](https://user-images.githubusercontent.com/67532044/210788243-d326e1e9-6428-4f61-9ffc-39247e6a7f2a.gif)

> *筆電為OBS直出畫面。透過OBS的Browser擷取器，將網頁內容即時投影到輸出畫面上，來達到同時直播和呈現得票數。*
 
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
### Reset database
```

flask reset
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
