# 버전 기록

### 1.1.4
* **23.09.10**
* 관리자 페이지 수정 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/226))
* DB에 없는 학수번호 에러 핸들링 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/228))
---

### 1.1.3
* **23.08.26**
* 이용약관 & 개인정보처리방침 추가 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/209))
---

### 1.1.2
* **23.08.03**
* 특별학기, 몰입 과목 추가 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/205))
---

### 1.1.1
* **23.08.02**
* 지능데이터융합학부 (핀테크·빅데이터·스마트생산) 회원가입 오류 수정 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/201))
---

### 1.1.0
* **23.07.29**
* 2023학년도 2학기 교양 교육과정 수정 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/195))
  * 기초교양 3과목 -> 4과목으로 변경
---

### 1.0.7
* **23.07.19**
* 2023학년도 2학기 강의시간표 및 교육과정 업데이트 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/188))
* 서비스 대상 모든 학과로 업데이트 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/164))
  * 한일문화콘텐츠전공, 경영학부, 글로벌경영학과 추가
* 413 Request Entity Too Large 오류 해결 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/184))
---

### 1.0.6
* **23.06.02**
* 사용자 통계 수정 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/177))
  * 기존: 로그인 횟수
  * 변경: 방문자 수
* 로그인 페이지 화면 개선 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/179))
---

### 1.0.5
* **23.02.23**
* DB 마이그레이션 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/172))
  * 기존: PostgreSQL 도커 이미지
  * 변경: MySQL RDS
* 비밀번호 찾기 오류 해결 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/175))
---

### 1.0.4
* **23.02.09**
* 파일 업로드 오류 해결 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/156))
  * 원인: "SM-人 기초역량교육" 과목이 DB에 존재하지 않음 
  * 해결: DB에 과목 추가 및 예외 처리
* 지능·데이터융합학부 회원가입 오류 해결 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/117))
  * 지능데이터융합학부의 경우 핀테크전공으로 회원가입 되도록 예외처리
  * 마이페이지에서 3가지 전공 중 선택 (핀테크전공, 빅데이터융합전공, 스마트생산전공)
---

### 1.0.3
* **23.02.07**
* 모달 디자인 수정 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/148))
* 장고 로그 설정 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/150))
* 사용자 통계 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/152))
---

### 1.0.2
* **23.02.06**
* 기이수과목 업로드 방식 변경 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/132))
  * 엑셀 -> har
* 학과 업데이트 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/134))
  * 35개 학과 중 32개 학과 검사 가능
---

### 1.0.1
* **23.01.30**
* 마이페이지 학번 오류 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/113))
* 융합전자공학과 회원가입 오류 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/115))
  * 융합전자공학전공 -> 지능IOT융합전공
---

### 1.0.0
* **23.01.29**
* 서비스 출시
* AWS EC2 배포 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/82))
* Nginx SSL 설정 ([더 보기](https://github.com/smu-nity/SMUNITY/issues/83))
  * HTTPS 적용
---
