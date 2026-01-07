from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ReviewData(BaseModel):
    """리뷰 데이터 모델"""
    id: int = Field(..., description="리뷰 테이블의 PK (snowflake)", example=1234567890)
    restaurants_id: int = Field(..., description="식당 테이블 PK")
    users_id: int = Field(..., description="사용자 테이블 PK")
    rating: int = Field(..., ge=0, le=5, description="별점 (tinyint)")
    comment: Optional[str] = Field(None, description="리뷰 상세 내용 (text)")
    created_at: datetime = Field(..., description="생성 일시")
