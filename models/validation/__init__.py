from pydantic import BaseModel, Field

class ReceiptValidationResponse(BaseModel):
    """영수증 검증 응답"""
    success: bool = Field(..., description="API 요청 성공 여부 (비즈니스 로직 성공과는 별개)")
    process_time: float = Field(..., description="서버 프로세스 시간")
    is_valid: bool = Field(..., description="영수증 검증 결과 (상호명 일치 여부)")
    message: str = Field(..., description="결과 메시지 (성공, 이미지 아님, 텍스트 불일치 등)")

__all__ = ["ReceiptValidationResponse"]
