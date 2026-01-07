from fastapi import APIRouter
from models.classify import ClassifyRequest, ClassifyResponse
from models.recom import RecommendationRequest, RecommendationResponse

router = APIRouter()

@router.post("/classify", response_model=ClassifyResponse)
async def classify_v2(request: ClassifyRequest):
    """
    [v2] 개인 특성 분석
    """
    mock_results = [{"label": "v2_enhanced_label", "score": 0.99}]
    return {
        "success": True,
        "results": mock_results[:request.top_k]
    }

@router.post("/recommendations", response_model=RecommendationResponse)
async def get_recommendations_v2(request: RecommendationRequest):
    """
    [v2] 회식 장소 추천 (개선 버전 적용 목업)
    """
    mock_items = [{"item_id": "v2_item", "item_name": "v2 추천 상품", "relevance_score": 0.98}]
    return {
        "success": True,
        "recommendations": mock_items[:request.num_recommendations]
    }
