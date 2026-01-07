from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class GroupData(BaseModel):
    """그룹 데이터 모델"""
    id: int = Field(..., description="그룹 테이블의 PK (snowflake)", example=1234567890)
    name: str = Field(..., min_length=2, max_length=10, description="그룹 이름 (2-10자, 특수문자/이모지 가능)")
    introduction: Optional[str] = Field(
        None, 
        max_length=30, 
        pattern=r'^[^\n\r]*$', 
        description="그룹 소개 (최대 30자, 줄바꿈 불가)"
    )
    total_members: int = Field(default=1, ge=1, description="그룹 인원 수")
    created_at: datetime = Field(..., description="생성 일시")
