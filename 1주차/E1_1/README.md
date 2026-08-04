# 
byeong@gimbyeongcheol-ui-MacBookPro retest_docker % docker exec -it my-ubuntu bash
root@05fe75a5ddb5:/# docker attach
bash: docker: command not found

여기서 docker attach를 컨테이너 안에서 실행했기 때문이다. root@05fe75a5ddb5가 컨테이너를 의미한다. 도커 명령은 호스트(맥)에 설치된 명령어 인데, 컨테이너에서 실행해서 그럼. 컨테이너는 격리된 환경이라서 우분투 파일만 있고 도커는 없음. 그래서 command not found 라고 뜸.

#
도커파일에 넣은 내용
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html

nginx 이미지를 베이스(출발점)로 삼겠다
내 index.html을 이미지 안의 저 경로로 복사해라  라는 의미이다. 
/usr/share/nginx/html/은 nginx가 웹페이지를 찾아서 보여주는 기본 폴더인데, nginx 기본 환영 페이지를 내 파일로 덮어쓴 겁니다.
웹 서버가 있는 이미지이기에 가능하고 없다면, 웹서버를 직접 설치해야된다. 

# 1. 프로젝트 개요
    터미널의 작동법을 이해한다. 
    도커의 개념을 이해하고 도커를 만들어 컨테이너 및 볼륨의 특성을 이해할 수 있다. 
    깃허브에 연동하고 풀/푸시를 할 수 있다. 

# 2. 실행환경
    os: mac silicon M4pro
    shell: bash
    ubuntu: 26.04 LTE
    docker: 29.6.2
# 3. 수행항목 (기능요구사항))
1. 터미널 조작
<img width="583" height="875" alt="Image" src="https://github.com/user-attachments/assets/69f7ba36-5afc-4bc5-a752-45ae5951f077" />
<img width="579" height="152" alt="Image" src="https://github.com/user-attachments/assets/31e9d502-6e16-4561-9c64-e3bcde1011bd" />
2. 권한 실습
<img width="579" height="351" alt="Image" src="https://github.com/user-attachments/assets/f18dfd88-ab1f-4f67-9069-2a1b47d58875" />

3. 도커 설치 및 정보확인
<img width="581" height="122" alt="Image" src="https://github.com/user-attachments/assets/9a33ed8a-1b56-48a8-a831-a77e53a56a16" />

4. 도커 이미지, 컨테이너, 운영 (images,ps,ps-a. logs, stats)
<img width="581" height="697" alt="Image" src="https://github.com/user-attachments/assets/87e300cd-7cb5-4abe-9f3a-b55a772904e9" />
도커에서 우분투 이미지를 실행하여 컨테이너를 만들었고 우분투 버젼과 도커 내의 이미지 목록을 확인했다. 
<img width="581" height="365" alt="Image" src="https://github.com/user-attachments/assets/0164164e-87f6-40eb-ac10-52a2cf67db9b" />
도커에서 ps 와 ps -a 의 차이점이다. -a 옵션을 붙이면 숨겨진 파일까지 볼 수 있다. 
<img width="579" height="259" alt="Image" src="https://github.com/user-attachments/assets/98db12e1-323e-4b78-ae8c-299bb0f757cf" />
도커의 로그 기록을 살펴보았다. 
<img width="579" height="179" alt="Image" src="https://github.com/user-attachments/assets/73586861-0aad-4da9-a9a3-a260ab75e5f1" />
현재 설치된 도커 엔진의 전체적인 상태와 시스템 정보를 확인했다.  

5. 기존 Dockerfile 기반 커스텀 이미지 제작
<img width="581" height="460" alt="Image" src="https://github.com/user-attachments/assets/1dc0c174-5818-4151-b3d3-788cdb56a2a8" />
index.html, Dockerfile를 만들어 도커 이미지를 만들었다 . [+] Building 0.1s (7/7) FINISHED 이것은 성공적으로 이미지가 완성되었다는 의미이다. 
<img width="547" height="126" alt="Image" src="https://github.com/user-attachments/assets/40cc1cdb-2130-4f47-8d0f-0353caac853d" />
도커파일의 내용이다. 
<img width="547" height="126" alt="Image" src="https://github.com/user-attachments/assets/618221da-6d03-4a15-ae39-88b24758a5ef" />
indec.html 의 내용이다. 

6. 포트 매핑 및 접속 증거
<img width="581" height="716" alt="Image" src="https://github.com/user-attachments/assets/6a9abb2a-7a72-4d5b-be61-29724f8e4425" />
포트 맵핑을 했다. -p 옵션이 필요하다. 기존에 실습한 내용잉 있어 생성할때 기존의 이름과 일치한다는 에러가 떠서 기존을 지우고 생성하였다. 
<img width="583" height="166" alt="Image" src="https://github.com/user-attachments/assets/c545989c-8aa0-4117-b7f2-7759e0efa181" />

<img width="1512" height="142" alt="Image" src="https://github.com/user-attachments/assets/8653df53-49f6-49be-994f-e4a591f9ee05" />
실습을 통해 실제 뜬 화면이다. 
7. Docker 볼륨 영속성 검증
![Image](https://github.com/user-attachments/assets/b87a45c7-c823-4479-814d-28d0faaad928)
도커에서 볼륨을 생성하고, "This data will survive" 을 볼륨에 넣었다. 컨테이너를 실행하고 컨테이너를 지우고 다시 출력한 결과 전후 모두 같은 내용을 출력한다. 이를 통해 도커에서 컨테이너를 지워도 볼륨의 내용이 지워지지 않는다는 점을 알수 있다. 

8. Git 설정 및 GitHub 연동
<img width="581" height="288" alt="Image" src="https://github.com/user-attachments/assets/fd342416-9bae-4602-ba99-a26d436da8a3" />
<img width="579" height="508" alt="Image" src="https://github.com/user-attachments/assets/4484acd0-072b-47fc-b9b8-6719b8205eac" />
<img width="279" height="622" alt="Image" src="https://github.com/user-attachments/assets/b0ac3a3a-402d-4157-b483-8473651da7c4" />

9. 보안 및 개인정보 보호

# 4. 문제 및 해결
<img width="653" height="246" alt="Image" src="https://github.com/user-attachments/assets/d85c45f6-7948-4950-acda-b174cb855a47" />

도커 내에 같은 컨테이너 이름이 이미 존재해서 생긴 문제라서 기존의 도커를 지우고 시행했다.

<img width="581" height="288" alt="Image" src="https://github.com/user-attachments/assets/fd342416-9bae-4602-ba99-a26d436da8a3" />
입력때 " " 형식으로 해야 입력할 내용을 끝낸다. 

## 깃허브 이미지 삽입은 깃허브에서 issu 를 이용하였다. 이미지를 드로그 하면 이미지가 자동으로 업로드 된다. 따라서 이미지를 따로 업로드 하거나 할필요 없고 create 도 누를 필요가 없다. 

## 도커의  개념
    도커는 컨테이너 기술을 실행하고 관리해 주는 플랫폼(엔진/프로그램)을 의미한다. 보통 1개로 작동한다. 백그라운드에서 맵 a를 실행하고 앱 b를 실행해서 도커가 두개가 아니라 1개다.??? 도커허브에는 여러 이미지 파일들이 존재한다. 이미지 파일들은 이미지를 만드는데 쓰이는 Read only 파일이다. 이미지 파일을 로컬이 가져와서 실행을 하면 도커에서 작동되어 컨테이너가 만들어진다. 사용자가 추가 데이터를 넣어도 컨테이너에서 쌓이는 것이다. 데이터중 지워지면 안되는 정적 데이터와 같은 것은 도커가 만든 별도의 로컬 공간인 볼륨에 들어가서 저장이되게 된다. 따라서 컨테이너를 지워도 볼륨을 기준으로 데이터를 가져와 실행하기 땜에 영속성이란 특성이 나온것이다. 

## 바인드 마운트 vs 포트 맵핑

    바인트 마운트는 컨테이너와 로컬를 직접 연결하여 로컬의 변경사항을 직접 컨테이너에 반영하는 방식이다. 컨테이너는 도커 이미지를 기반으로 만들어진다. 따라서 컨테이너에서 변경사항이 있다면 이미지를 만들어서 컨테이너를 만들어야하진만 바인드 마운트를 하면 이런 과정이 생략된다. 반대로 컨테이너가 생성한 파일도 호스트에 남는다. (ex. 실시간 코드 수정)
    포트 맵핑은 "호스트포트:컨테이너포트" 주소 형식으로 호스트 데이터가 로컬에 이동할수 있다록 한다. 컨테이너는 내 컴퓨터(호스트) 안에서 방화벽으로 격리되어 있기 때문이다. 
    서로 완전히 다른 개념이다. 바인드 마운트는 컨테이너에 실시간으로 데이터를 반영하는 것이고, 포트 맵핑은 호스팅 주소의 데이터를 로컬에 가져오는 것이다. 실시간으로 변경사항을 가져와야한다면 바인드 마운트 방식을 포트 맵핑에 적용시킬수는 있겠다느 생각이 든다. 