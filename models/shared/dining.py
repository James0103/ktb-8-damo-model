from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class DiningStatus(str, Enum):
    ATTENDANCE_VOTING = "ATTENDANCE_VOTING"
    RESTAURANT_VOTING = "RESTAURANT_VOTING"
    CONFIRMED = "CONFIRMED"
    COMPLETE = "COMPLETE"

class DiningData(BaseModel):
    """회식 데이터 모델"""
    id: int = Field(..., description="회식 테이블의 PK (snowflake)", example=1234567890)
    groups_id: int = Field(..., description="그룹 테이블의 PK")
    dining_date: datetime = Field(..., description="회식 진행 날짜")
    vote_due_date: datetime = Field(..., description="투표 마감 날짜")
    budget: int = Field(..., description="회식 진행 예산")
    created_at: datetime = Field(..., description="생성 일시")