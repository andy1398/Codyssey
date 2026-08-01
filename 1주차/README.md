## 1 실행 환경
- OS: mac M4
- Shell: bash
- Docker: 29.6.2
- Git: 2.50.1

## 2 수행 체크리스트
- [o] 터미널 기본 조작 및 폴더 구성
- [o] 권한 변경 실습
- [o] Docker 설치/점검
- [o] hello-world 실행
- [o] Dockerfile 빌드/실행
- [o] 포트 매핑 접속
- [o] 바인드 마운트 반영
- [o] 볼륨 영속성
- [o] Git 설정 + VSCode GitHub 연동

 ## 3 터미널 조작 로그 기록
 pwd,ls,cd,mkdir,touch,cat,>,mv,rm,chmod 를 이용하여 터미널 명령어를 사용했다.
 byeong@gimbyeongcheol-ui-MacBookPro ~ % pwd
/Users/byeong 
-깃허브 폴더 이미지 '터미널 조작 로그 기록'에서 일부 발췌

 ## 3 권한 실습 및 증거 기록
byeong@gimbyeongcheol-ui-MacBookPro Codyssey % ls -la test.txt
total 0
drwxr-xr-x  2 byeong  staff   64  7월 29 16:00 .
drwxr-xr-x  8 byeong  staff  256  7월 29 16:00 ..
byeong@gimbyeongcheol-ui-MacBookPro Codyssey % chmod 766 test.txt
byeong@gimbyeongcheol-ui-MacBookPro Codyssey % ls -la test.txt   
total 0
drwxrw-rw-  2 byeong  staff   64  7월 29 16:00 .
drwxr-xr-x  8 byeong  staff  256  7월 29 16:00 ..

 ## 4 Docker 설치 및 기본 점검
byeong@gimbyeongcheol-ui-MacBookPro Codyssey % docker --version
Docker version 29.6.2, build dfc4efb 
byeong@gimbyeongcheo1-ui-MacBookPro Codyssey % docker info Client:
Version:
29.6.2

 ## 5 Docker 기본 운영 명령 수행
- 이미지
byeong@gimbyeongcheol-ui-MacBookPro Codyssey % docker images
IMAGE ID
DISK USAGE
DISK USAGE CONTENT SIZE EXTRA
byeong@gimbyeongcheol-ui-MacBookPro Codyssey % docker ps -a
CONTAINER ID IMAGE
COMMAND CREATED
STATUS PORTS
[byeong@gimbyeongche01-ui-MacBookProCodyssey % docker logs
docker: 'docker logs' requires 1 argument
i Info →
Usage: docker logs LOPTIONS] CONTAINER
Run 'docker logs --help' for more information

- 도커 실행 중지 확인
byeong@gimbyeongcheol-ui-MacBookPro Codyssey % docker ps
CONTAINER ID
IMAGE
COMMAND
CREATED
STATUS
PORTS
NAMES
98a398ec0d9f
nginx
"/docker-entrypoint..." 14 seconds ago
Up 14 seconds

- 도커 logs
byeong@gimbyeongcheol-ui-MacBookPro Codyssey % docker logs my-web-8080
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perfo
Im configuration

- 도커 stats
ICONTAINER ID
I/0
ac4ea2a182e5
/ 126B
63b77173bf1b
kB / 3.88kB
bb215ee24f13 kB / 3.29kB
NAME
BLOCK I/O
new-vol-container
OB / OB
bind-web
OB / 12.3kB
13
my-web-8080
135kB / 12.3kB
13
CPU %
PIDS
0.00%
1
0.00%
0.00%
MEM USAGE / LIMIT
1.648MiB / 7.75GiB
10.24MiB / 7.75GiB
10.37MiB / 7.75GiB
MEM %
0.02%
0.13%
0.13%
NET J
872B
5.21
5.83

 ## 6 컨테이너 실행 실습
 hello-world나 ubuntu에서 exit을 쳤을 때는 컨테이너가 종료됨
 docker ps-a를 했을때 상태가 exit 으로 표기되어있다. 
 nginx를 -d 옵션으로 실행했을 때는 터미널을 계속 써도 서버가 백그라운드에서 유지됨
docker ps-a를 했을때 상태가 up 으로 표기되어있다. 

 ## 7 기존 Dockerfile 기반 커스텀 이미지 제작
 nginx:latest (공식 NGINX 웹 서버 베이스 이미지)를 선택
 커스텀 포인트: COPY index.html /usr/share/nginx/html/index.html 명령어를 Dockerfile에 추가하여 NGINX의 기본 웹 페이지를 교체
목적: 기존 NGINX의 기본 환영 화면 대신, 내가 직접 작성한 정적 HTML 콘텐츠("Hello Codyssey!")를 출력하도록 설정
 ## 8 포트 매핑 및 접속 증거
 [byeong@gimbyeongcheol-ui-MacBookPro my-custom-web % docker run -d -p 8080:80
--n/
ame my-web-8080 my-web:1.0
bb215ee24f13a8ae6409e5364f51c210698a0657075f804c409cb6d7ebd975c7 byeong@gimbyeongcheol-ui-MacBookPro my-custom-web % docker ps
curl http://localhost:8080
CONTAINER ID
IMAGE
COMMAND
CREATED
STATUS
PORTS
bb215ee24f13
my-web:1.0
"/docker-entrypoint....
nds
0.0.0.0:8080-80/tcp, [::]:8080->80/tcp
NAMES
12 seconds ago
my-web-8080
Up 11 seco
<h1>Hello, Codyssey! This is my custom server.</h1>

 ## Docker 볼륨 영속성 검증
- 볼륨 생성
docker volume create my-data-vol
- 볼륨 연결
docker run -d -v my-data-vol:/dat a --name vol-container ubuntu sleep infinity
- 컨테이너에 데이터 삽입
docker exec vol-container bash -c "echo 'This data will survive' > /data/hello.txt"
- 기록된 데이터 확인
docker exec vol-container cat /data/hello.txt
- 볼륨 영속성 (컨테이너 삭제 후 새롭게 연결후 출력)
docker rm -f vol-container
docker run -d -v my-data-vol:/data --name new-vol-container ubuntu sleep infinity
docker exec new-vol-container cat /data/hello.txt
- 결과
This data will survive 가 출력됨

 ## Git 설정 및 GitHub 연동
 이미지 첨부
 ## 보안 및 개인정보 보호
 기술 문서/로그/스크린샷에 토큰, 비밀번호, 개인키, 인증 코드 등이 포함되지 않도록 마스킹한다.
