docker-compose down
docker volume rm tapsell_task_appdata tapsell_task_mongodbdata tapsell_task_nginxdata
docker image rm flask-python:3.6 nginx_img:1.0
