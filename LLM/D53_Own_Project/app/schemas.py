"""
입력/출력 스키마를 정의하세요.

참고: Day 2 섹션 4 (Pydantic 기초), Day 5 섹션 3 (HousingRequest)

TODO:
  - 본인의 모델 입력에 맞는 Request 스키마를 정의하세요.
  - 모델 출력에 맞는 Response 스키마를 정의하세요.
  - 필수 필드와 선택 필드를 구분하세요.
  - 적절한 검증 규칙(타입, 범위, 길이 등)을 추가하세요.

예시 (텍스트 분류의 경우):
  class PredictRequest(BaseModel):
      text: str = Field(..., min_length=1, max_length=5000)

  class PredictResponse(BaseModel):
      success: bool
      label: str
      confidence: float
"""
from pydantic import BaseModel, Field

# ── 여기에 작성하세요 ──────────────────────────

  class PredictRequest(BaseModel):
      text: str = Field(..., min_length=1, max_length=5000)

  class PredictResponse(BaseModel):
      success: bool
      label: str
      confidence: float