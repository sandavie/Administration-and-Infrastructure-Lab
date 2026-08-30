# 🐍 Web Application Service

## 🗺️ Overview

The Flask application is a simple weather app named `Weather Man` which uses the `Open Weather Map` API. The application was created in `Visual Studio Code` and the structure of the application is as follows.

```text
WeatherMan
│── .venv
│── static/
|   |──css/
|      |──style.css
│── templates/
│   ├── index.html
│   ├── results.html
|── .env
|── .gitignore
|── requirements.txt
|── weather-client.py
|── webapp.py
```

---

### ↔️ rsync

`rsync` was used to transfer the files from the `wsl-station` to `web01`

![rsync](../05-Screenshots/04-Linux-Server/04-Web-Application-Servicet/01-rsync.png)

![rsync 2](../05-Screenshots/04-Linux-Server/04-Web-Application-Service/02-rsync-2.png)

The directory was then copied into `/opt/flaskapp/` using the `cp` command

