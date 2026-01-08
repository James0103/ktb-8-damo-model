from fastapi import APIRouter
from datetime import datetime
from models.recom import RecommendationResponse, RecommendedItem
from models.classify import ClassifyResponse, ClassifyAnalysis, ClassifyKeywords
from models.validation import ReceiptValidationResponse

router = APIRouter()

@router.get("/recommendations", response_model=RecommendationResponse, tags=["Debug"])
async def get_dummy_recommendations():
    """운영 로직과 무관하게 항상 일정한 더미 추천 데이터를 반환합니다."""
    mock_items = [
        RecommendedItem(
            restaurant_id="rest_001",
            restaurant_name="판교 한우 명가",
            reasoning_description="회식 인원(20명)을 수용할 수 있는 대형 룸이 구비되어 있으며, 예산 범위 내의 코스 요리가 제공됩니다.",
            relevance_score=0.98,
            address_name="경기도 성남시 분당구 판교역로 100"
        ),
        RecommendedItem(
            restaurant_id="rest_002",
            restaurant_name="대장동 해산물 천국",
            reasoning_description="알레르기 보유자(갑각류)를 제외한 나머지 인원의 높은 선호도를 반영하였으며, 신선한 제철 회가 제공됩니다.",
            relevance_score=0.85,
            address_name="경기도 성남시 분당구 판교대장로 50"
        )
    ]
    
    return RecommendationResponse(
        success=True,
        process_time=0.125,
        group_id="group_debug_123",
        dinner_id="dinner_debug_456",
        recommendations=mock_items,
        total_count=len(mock_items)
    )

@router.get("/classify", response_model=ClassifyResponse, tags=["Debug"])
async def get_dummy_classify():
    """사용자 특성 분석의 고정된 더미 결과를 반환합니다."""
    return ClassifyResponse(
        success=True,
        process_time=0.089,
        user_id=123456789,
        otherCharacteristics="조용한 분위기를 선호하며, 육류보다는 해산물을 조금 더 선호하는 경향이 있음",
        analysis=ClassifyAnalysis(
            keywords=[
                ClassifyKeywords(words="삼겹살", category="음식", sentiment="긍정"),
                ClassifyKeywords(words="소음", category="분위기", sentiment="부정"),
                ClassifyKeywords(words="하이볼", category="주류", sentiment="중립")
            ],
            contents="사용자는 전반적으로 대화가 가능한 조용한 식당을 선호하며, 고기류에 대해 긍정적인 반응을 보이지만 시끄러운 환경에는 매우 민감함."
        ),
        created_at=datetime.now()
    )

@router.get("/validation-receipt", response_model=ReceiptValidationResponse, tags=["Debug"])
async def get_dummy_receipt_validation():
    """영수증 검증의 고정된 더미 결과를 반환합니다."""
    return ReceiptValidationResponse(
        success=True,
        process_time=0.045,
        is_valid=True,
        message="[Debug] 고정된 검증 성공 메시지"
    )
