from pydantic import BaseModel, Field
from typing import List

class ClassifyRequest(BaseModel):
    """분류 요청 모델"""
    text: str = Field(..., description="분류할 텍스트 내용", example="이 상품 정말 추천해요!")
    top_k: int = Field(default=3, description="상위 몇 개의 결과를 반환할지", ge=1)

class ClassifyResult(BaseModel):
    """분류 개별 결과 모델"""
    label: str = Field(..., description="분류 레이블")
    score: float = Field(..., description="정확도 점수 (0.0 ~ 1.0)")

class ClassifyResponse(BaseModel):
    """분류 응답 모델"""
    success: bool = Field(..., description="작업 성공 여부")
    results: List[ClassifyResult] = Field(default_factory=list, description="분류 결과 목록")
