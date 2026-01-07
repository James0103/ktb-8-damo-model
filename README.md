# AI Server Mock-up API

이 프로젝트는 회식 장소 추천 및 사용자 취향 분석을 위한 AI 서버의 FastAPI 기반 모업(Mock-up) API입니다. Pydantic을 활용하여 복잡한 데이터 구조를 정의하고, 버전별(v1, v2) 라우팅을 지원합니다.

## 🚀 주요 기능

### 1. API 기능
- **회식 장소 추천 (v1, v2)**: 사용자 정보, 리뷰 이력, 회식 이력 및 후보 식당 데이터를 기반으로 최적의 장소 추천
- **사용자 특성 분석 (v2)**: 텍스트 또는 유저 데이터를 분석하여 개인화된 라벨링 제공
- **헬스 체크**: 서버 상태 확인용 `/health` 엔드포인트 지원

### 2. 데이터 모델 (Pydantic)
- **Shared**: 여러 도메인에서 공통으로 사용되는 모델
    - `UserData`: 성별, 연령대, **알레르기 정보**, **비선호 음식** 등 상세 속성 포함
    - `DiningData`: 회식 예산, 날짜, 진행 상태(`DiningStatus`) 관리
- **Recommendation**:
    - `RestaurantData`: 카카오 로컬 API 규격 기반 식당 정보 및 상세 리뷰(`RestaurantReviewData`) 중첩 구조
    - `ReviewData`: 사용자의 과거 방문 리뷰 기록
- **Classify**:
    - `GroupData`: 그룹 이름, 소개, 인원 수 등 그룹 속성 관리
    - `ClassifyAnalysis`: AI가 분석한 핵심 키워드 및 종합 분석 내용

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
│   │   ├── user.py      # 공통 유저 모델 (알레르기, 비선호 등)
│   │   └── dining.py    # 공통 회식 모델
│   ├── recom/           # 추천 도메인 전용 모델 패키지
│   │   ├── restaurant.py
│   │   ├── restaurant_review.py
│   │   └── review.py
│   └── classify/        # 개인 특성 분석 도메인 전용 모델 패키지
│       ├── __init__.py
│       └── group.py
└── README.md
```

## 🛠 실행 방법

### 의존성 설치
```bash
pip install -r requirements.txt
```

### 서버 실행
```bash
python main.py
```
* 서버는 `http://localhost:8000`에서 실행됩니다.
* 인터랙티브 API 문서는 `http://localhost:8000/docs`에서 확인할 수 있습니다.

## 📝 최근 작업 요약
- **개인 특성 분석 모델 설계**: `ClassifyRequest`, `ClassifyResponse` 및 AI 분석 결과 구조 정의
- **Shared 모듈 확장**: `UserData`에 이어 `DiningData`를 `shared`로 이동하여 분석/추천 도메인 간 정합성 확보
- **모델 계층화**: `RestaurantData` 내부에 `RestaurantReviewData`를 리스트 형태로 포함시켜 데이터 연관성 강화
- **API 고도화**: 요청/응답 필드에 Snowflake ID(int) 및 시계열 데이터(datetime) 타입 적용
