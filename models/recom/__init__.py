from pydantic import BaseModel, Field
from typing import List, Optional
from ..shared.user import UserData
from ..shared.dining import DiningData

class RecommendationRequest(BaseModel):
    """식당 추천 요청"""
    group_id: str = Field(..., description="회식 그룹 ID")
    dinner_id: str = Field(..., description="회식 ID")
    user_data: List[UserData] = Field(..., description="회식에 참여하는 사용자 데이터 목록(list)")
    dining_data: DiningData = Field(..., description="회식 데이터 목록(dict)")
    # 리뷰 데이터는 mongoDB에서 직접 조회
    # review_data: List[ReviewData] = Field(..., description="리뷰 데이터 목록(list)")
    # 후보 식당 데이터는 mongoDB에서 직접 조회
    # candidate_restaurants: List[RestaurantData] = Field(..., description="후보 식당 데이터 목록(list)")

class RecommendedItem(BaseModel):
    """추천 식당 아이템"""
    restaurant_id: str = Field(..., description="식당 식별자")
    restaurant_name : str = Field(..., description="식당 이름")
    reasoning_description: str = Field(..., max_length=500, description="추천 사유")
    relevance_score: float = Field(..., description="추천 적합도 점수")
    address_name: str = Field(..., description="전체 지번 주소")
    # 응답 데이터를 백엔드와 논의해서 책임 소재를 확실히 할것

class RecommendationResponse(BaseModel):
    """식당 추천 응답"""
    success: bool = Field(..., description="작업 성공 여부")
    process_time: float = Field(..., description="서버 프로세스 시간")
    group_id: str = Field(..., description="회식 그룹 ID")
    dinner_id: str = Field(..., description="회식 ID")
    recommendations: List[RecommendedItem] = Field(..., description="추천된 식당 목록(list)")
    total_count: int = Field(..., ge=0, le=50, description="추천된 식당 목록의 총 개수")

__all__ = [
    "RecommendationRequest",
    "RecommendationResponse",
]
