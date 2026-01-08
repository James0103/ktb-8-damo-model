from pydantic import BaseModel, Field
from typing import List
from .restaurant_review import RestaurantReviewData

class RestaurantData(BaseModel):
    """식당 데이터 모델 (카카오 로컬 API 기반)"""
    address_name: str = Field(..., description="전체 지번 주소")
    category_group_name: str = Field(..., description="카테고리 그룹 명 (예: 음식점)")
    category_name: str = Field(..., description="카테고리 이름")
    distance: str = Field(..., description="중심좌표로부터의 거리 (단위: m)")
    id: str = Field(..., description="식당 ID")
    phone: str = Field(..., description="전화번호")
    place_name: str = Field(..., description="식당 이름")
    place_url: str = Field(..., description="식당 상세 페이지 URL")
    road_address_name: str = Field(..., description="전체 도로명 주소")
    x: str = Field(..., description="X 좌표 (경도, Longitude)")
    y: str = Field(..., description="Y 좌표 (위도, Latitude)")
    reviews: List[RestaurantReviewData] = Field(default_factory=list, description="식당 리뷰 목록")
