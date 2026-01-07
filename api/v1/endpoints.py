from fastapi import APIRouter
from models.recom import RecommendationRequest, RecommendationResponse

router = APIRouter()

@router.post("/recommendations", response_model=RecommendationResponse)
async def get_recommendations_v1(request: RecommendationRequest):
    """
    [v1] 회식 장소 추천
    """
    mock_items = [{"item_id": "v1_item", "item_name": "v1 상품", "relevance_score": 0.9}]
    return {
        "success": True,
        "recommendations": mock_items[:request.num_recommendations]
    }
