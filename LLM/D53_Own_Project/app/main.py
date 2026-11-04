"""
FastAPI 서버를 정의하세요.

참고: Day 5 섹션 3 (housing_api.py), Day 6 섹션 6 (image_api.py)

TODO:
  1. FastAPI 앱 생성
  2. startup 이벤트에서 모델 로드
  3. GET /health 엔드포인트
  4. POST /predict 엔드포인트
     - Pydantic 스키마로 입력 검증
     - Depends(verify_api_key)로 인증 적용
     - run_in_executor로 비동기 추론

필수 import:
  import asyncio
  from concurrent.futures import ThreadPoolExecutor
  from fastapi import FastAPI, Depends, HTTPException
  from app.auth import verify_api_key
  from app.schemas import PredictRequest, PredictResponse  (본인이 정의한 이름)
  from app.model_service import load_model, predict
"""

# ── 여기에 작성하세요 ──────────────────────────
