from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from ..shared.user import UserData
from ..shared.dining import DiningData
from .group import GroupData

class ClassifyRequest(BaseModel):
    """개인 특성 분석 요청"""
    user_data: UserData = Field(..., description="회식에 참여하는 사용자 데이터")
    group_data: List[GroupData] = Field(..., description="참여 그룹 데이터(list)")
    dining_data: List[DiningData] = Field(..., description="회식 데이터(list)")
    # mongoDB에서 직접 조회
    # otherCharacteristics: str = Field(..., description="기타 특성")

class ClassifyKeywords(BaseModel):
    """개인 특성 분석 키워드"""
    words: str = Field(..., description="키워드")
    category: str = Field(..., description="키워드 분류 카테고리(음식, 주류, 분위기 등)")
    sentiment: str = Field(..., description="키워드 감정(긍정, 부정, 중립)")

class ClassifyAnalysis(BaseModel):
    """개인 특성 분석 내용"""
    keywords: List[ClassifyKeywords] = Field(..., description="키워드")
    contents: str = Field(..., max_length=300, description="분석된 내용")

class ClassifyResponse(BaseModel):
    """개인 특성 분석 응답"""
    success: bool = Field(..., description="작업 성공 여부")
    process_time: float = Field(..., description="서버 프로세스 시간")
    user_id: int = Field(..., description="회식에 참여하는 사용자 ID")
    otherCharacteristics: str = Field(..., description="기타 특성")
    analysis: ClassifyAnalysis = Field(..., description="분석된 내용")
    created_at: datetime = Field(..., description="생성 일시")

__all__ = [
    "ClassifyRequest",
    "ClassifyResponse"
]
