from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from datetime import datetime

class AllergyType(str, Enum):
    LEGUMES = "LEGUMES"
    NUTS = "NUTS"
    SHELLFISH = "SHELLFISH"
    FISH = "FISH"
    GRAINS = "GRAINS"
    MILK = "MILK"

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class AgeGroup(str, Enum):
    TWENTIES = "TWENTIES"
    THIRTIES = "THIRTIES"
    FORTIES = "FORTIES"
    FIFTIES_PLUS = "FIFTIES_PLUS"

class DislikeType(str, Enum):
    SEAFOOD = "SEAFOOD"
    OFFAL = "OFFAL"
    RAW = "RAW"
    STRONG_SPICES = "STRONG_SPICES"

class UserData(BaseModel):
    """사용자 데이터 모델(사용자 특이사항은 별도의 mongoDB에서 조회)"""
    id: int = Field(..., description="사용자 테이블의 PK (snowflake)", example=123456789)
    email: str = Field(..., max_length=100, description="소셜 가입 계정 이메일")
    password: Optional[str] = Field(None, max_length=255, description="SHA256 암호화된 비밀번호")
    nickname: str = Field(
        ..., 
        min_length=1, 
        max_length=10, 
        pattern=r'^[^\s!@#$%^&*(),.?":{}|<>]*$',
        description="닉네임 (1-10자, 공백 및 특수문자 금지)"
    )
    gender: Gender = Field(..., description="성별 (MALE, FEMALE)")
    age_group: AgeGroup = Field(..., description="연령대")
    is_push_notification_allowed: bool = Field(default=False, description="푸시 알림 허용 여부")
    created_at: datetime = Field(..., description="생성 일시")
    updated_at: datetime = Field(..., description="수정 일시")
    withdraw_at: Optional[datetime] = Field(None, description="사용자 탈퇴 일시")
    is_withdraw: bool = Field(default=False, description="탈퇴 여부")
    allergies: List[AllergyType] = Field(default_factory=list, description="알레르기 정보 목록")
    dislikes: List[DislikeType] = Field(default_factory=list, description="비선호 음식 정보 목록")
