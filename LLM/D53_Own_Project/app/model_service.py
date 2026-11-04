"""
모델 로드와 추론 함수를 정의하세요.

참고: Day 1 섹션 5 (모델 로드), Day 5 섹션 2 (HousingPredictor)

TODO:
  1. load_model(): 모델을 로드하여 반환합니다.
     - transformers의 pipeline() 또는 from_pretrained()을 사용합니다.
     - 섹션 2.3에서 확인한 코드를 여기에 옮기면 됩니다.

  2. predict(model, input_data): 입력을 받아 추론 결과를 반환합니다.
     - 입력 전처리가 필요하면 여기서 합니다.
     - 결과를 dict로 반환합니다.

예시 (텍스트 분류의 경우):
  def load_model():
      return pipeline("text-classification", model="모델이름")

  def predict(model, text: str) -> dict:
      result = model(text)
      return {"label": result[0]["label"], "confidence": result[0]["score"]}
"""

# ── 여기에 작성하세요 ──────────────────────────

  def load_model():
      return pipeline("text-classification", model="snunlp/KR-FinBert-SC")

  def predict(model, text: str) -> dict:
      result = model(text)
      return {"label": result[0]["label"], "confidence": result[0]["score"]}