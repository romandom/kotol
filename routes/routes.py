from fastapi import APIRouter
from api import oAuth2Api, productApi, recipeAPi, \
    fermentationApi, favoriteRecipesApi, boilingApi

router = APIRouter()
router.include_router(oAuth2Api.router)
router.include_router(productApi.router)
router.include_router(recipeAPi.router)
router.include_router(fermentationApi.router)
router.include_router(favoriteRecipesApi.router)
router.include_router(boilingApi.router)
