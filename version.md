# 버전 기록

### 1.0.6
* **22.06.02**
* 사용자 통계 수정 ([더 보기](https://github.com/hyunmin0317/SMUNITY/issues/177))
  * 기존: 로그인 횟수
  * 변경: 방문자 수
* 로그인 페이지 화면 개선 ([더 보기](https://github.com/hyunmin0317/SMUNITY/issues/179))
---

### 1.0.5
* **22.02.23**
* DB 마이그레이션 ([더 보기](https://github.com/hyunmin0317/SMUNITY/issues/172))
  * 기존: PostgreSQL 도커 이미지
  * 변경: MySQL RDS
* 비밀번호 찾기 오류 해결 ([더 보기](https://github.com/hyunmin0317/SMUNITY/issues/175))
---

### 1.0.4
* **22.02.09**
* 파일 업로드 오류 해결 ([더 보기](https://github.com/hyunmin0317/smunity/issues/156))
  * 원인: "SM-人 기초역량교육" 과목이 DB에 존재하지 않음 
  * 해결: DB에 과목 추가 및 예외 처리
* 지능·데이터융합학부 회원가입 오류 해결 ([더 보기](https://github.com/hyunmin0317/smunity/issues/117))
  * 지능데이터융합학부의 경우 핀테크전공으로 회원가입 되도록 예외처리
  * 마이페이지에서 3가지 전공 중 선택 (핀테크전공, 빅데이터융합전공, 스마트생산전공)
---

### 1.0.3
* **22.02.07**
* 모달 디자인 수정 ([더 보기](https://github.com/hyunmin0317/smunity/issues/148))
* 장고 로그 설정 ([더 보기](https://github.com/hyunmin0317/smunity/issues/150))
* 사용자 통계 ([더 보기](https://github.com/hyunmin0317/smunity/issues/152))
---

### 1.0.2
* **22.02.06**
* 기이수과목 업로드 방식 변경 ([더 보기](https://github.com/hyunmin0317/smunity/issues/132))
  * 엑셀 -> har
* 학과 업데이트 ([더 보기](https://github.com/hyunmin0317/smunity/issues/134))
  * 35개 학과 중 32개 학과 검사 가능
---

### 1.0.1
* **22.01.30**
* 마이페이지 학번 오류 ([더 보기](https://github.com/hyunmin0317/smunity/issues/113))
* 융합전자공학과 회원가입 오류 ([더 보기](https://github.com/hyunmin0317/smunity/issues/115))
  * 융합전자공학전공 -> 지능IOT융합전공
---

### 1.0.0
* **22.01.29**
* 서비스 출시
* AWS EC2 배포 ([더 보기](https://github.com/hyunmin0317/smunity/issues/82))
* Nginx SSL 설정 ([더 보기](https://github.com/hyunmin0317/smunity/issues/83))
  * HTTPS 적용
---
