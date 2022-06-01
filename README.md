# docker-django-mysql

### [필독] 개발환경 설정방법 !!!/



1. 로컬환경의 빈폴더에 compose.yml 파일 Dockerfile 그리고 requirements.txt 파일을 넣어둔다 

2. 그리고 터미널환경을 통해 해당 빈폴더위치로 들어가자  

3. docker-compose run web  

4. docker ps -a 로 up 되어있는상태인지확인 ( 죽어있다면 도커서버는 실행하는파일이없다면 자동으로 종료하게끔설정되어있음 or 오류, docker logs [container_id] 로확인)  

5. docker exec -it django-container /bin/bash 로 도커서버에 접속  

6. 그리고 django-admin startproject config .  로 jango파일 생성! ## 스킵하고 7번에서 실행해도된다  

그리고 vscode 로 개발진행 !! vscode에서의 docker컨테이너 진입방법은   
vscode 스토어에서 docker development 설치후 control+F1 누른후 attach container 클릭후 실행되어있는 conatiner에 접속!! (없다면 컨테이너 실행해주고 다시 접속)  

7.컨테이너 환경 접속후에 Control+ ~ -> 터미널 오픈후 django-admin startproject config .   ,   django-admin startapp pybo 실행  pybo 파일 생성!! 
