from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class RestaurantReviewData(BaseModel):
    """식당별 개별 리뷰 데이터 모델 (크롤링 데이터 등)"""
    nickname: str = Field(..., description="리뷰어 닉네임")
    rating: int = Field(..., description="평점")
    prev_review_count: int = Field(..., description="지난 후기 수")
    average_rating: int = Field(..., description="리뷰어 평균 평점")
    follower: int = Field(..., description="리뷰어 팔로워 수")
    created_at: datetime = Field(..., description="리뷰 생성 일시")
    categorical_tag: str = Field(..., description="카카오맵 제공 태그")
    content: str = Field(..., description="리뷰 내용")
    image_url: List[str] = Field(default_factory=list, description="이미지 URL 목록")
    like: int = Field(..., description="좋아요 수")