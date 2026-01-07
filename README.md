# AI Server Mock-up API

이 프로젝트는 회식 장소 추천 및 사용자 취향 분석을 위한 AI 서버의 FastAPI 기반 모업(Mock-up) API입니다. Pydantic을 활용하여 복잡한 데이터 구조를 정의하고, 버전별(v1, v2) 라우팅을 지원합니다.

## 🚀 주요 기능

### 1. API 기능
- **회식 장소 추천 (v1, v2)**: 사용자 정보, 리뷰 이력, 회식 이력 및 후보 식당 데이터를 기반으로 최적의 장소 추천
- **사용자 특성 분석 (v2)**: 텍스트 또는 유저 데이터를 분석하여 개인화된 라벨링 제공
- **헬스 체크**: 서버 상태 확인용 `/health` 엔드포인트 지원

### 2. 데이터 모델 (Pydantic)
- **Shared**: 여러 도메인에서 공통으로 사용되는 모델 (`UserData` 등)
- **Recommendation**:
    - `UserData`: 성별, 연령대, **알레르기 정보**, **비선호 음식** 등 상세 속성 포함
    - `DiningData`: 회식 예산, 날짜, 진행 상태(`DiningStatus`) 관리
    - `RestaurantData`: 카카오 로컬 API 규격 기반 식당 정보 및 상세 리뷰(`RestaurantReviewData`) 중첩 구조
    - `ReviewData`: 사용자의 과거 방문 리뷰 기록

## 📂 프로젝트 구조

```text
.
├── main.py              # FastAPI 앱 실행 (Uvicorn)
├── api/
│   ├── v1/
│   │   └── endpoints.py # v1 라우터 (/api/v1/recommendations)
│   └── v2/
│   │   └── endpoints.py # v2 라우터 (/api/v2/classify, /api/v2/recommendations)
├── models/
│   ├── shared/
│   │   └── user.py      # 공통 유저 모델 및 Enum (알레르기, 비선호 등)
│   ├── recom/           # 추천 도메인 전용 모델 패키지
│   │   ├── dining.py
│   │   ├── restaurant.py
│   │   ├── restaurant_review.py
│   │   └── review.py
│   └── classify.py      # 분류 모델
└── .gitignore           # Python 환경 설정 제외 파일
```

## 🛠 실행 방법

### 의존성 설치
```bash
pip install fastapi uvicorn pydantic
```

### 서버 실행
```bash
python main.py
```
* 서버는 `http://localhost:8000`에서 실행됩니다.
* 인터랙티브 API 문서는 `http://localhost:8000/docs`에서 확인할 수 있습니다.

## 📝 최근 작업 요약
- **모델 계층화**: `RestaurantData` 내부에 `RestaurantReviewData`를 리스트 형태로 포함시켜 데이터 연관성 강화
- **Shared 모듈화**: 여러 도메인에서 사용되는 `UserData`를 `shared` 폴더로 이동하여 재사용성 확보
- **상세 제약 조건 반영**: 엔드포인트별 요청(Request)/응답(Response) 모델에 DB 제약 조건(Enum, MaxLength, 정규표현식 등) 반영
- **v1/v2 라우팅 설계**: 도메인 확장성 및 하위 호환성을 고려한 버전별 API 분리
