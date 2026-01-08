from fastapi import APIRouter, File, UploadFile, Form, HTTPException
import time
from models.classify import ClassifyRequest, ClassifyResponse
from models.recom import RecommendationRequest, RecommendationResponse
from models.validation import ReceiptValidationResponse

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

@router.post("/validation-receipt", response_model=ReceiptValidationResponse)
async def validate_receipt_v2(
    file: UploadFile = File(..., description="영수증 이미지 파일"),
    store_name: str = Form(..., description="검증할 상호명")
):
    """
    [v2] 영수증 검증 OCR (목업)
    - 이미지 형식 체크 (.jpg, .jpeg, .png)
    - 파일 용량 제한 (20MB)
    """
    start_time = time.time()
    MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB
    ALLOWED_EXTENSIONS = {"image/jpeg", "image/png", "image/jpg"}

    # 1. 파일 형식 확인
    if file.content_type not in ALLOWED_EXTENSIONS:
        return ReceiptValidationResponse(
            success=False,
            process_time=round(time.time() - start_time, 4),
            is_valid=False,
            message="올바른 이미지 형식이 아닙니다 (JPEG, PNG만 허용)"
        )

    # 2. 파일 용량 확인
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        return ReceiptValidationResponse(
            success=False,
            process_time=round(time.time() - start_time, 4),
            is_valid=False,
            message="파일 용량이 너무 큽니다 (최대 20MB)"
        )

    # 3. 텍스트 검증 로직 (목업: 상호명이 '실패'가 아니면 성공으로 처리)
    is_valid = store_name != "실패"
    message = "영수증 검증 성공" if is_valid else "상호명이 일치하지 않거나 영수증 판독이 불가능합니다."

    return ReceiptValidationResponse(
        success=True,
        process_time=round(time.time() - start_time, 4),
        is_valid=is_valid,
        message=message
    )
