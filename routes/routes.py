from fastapi import APIRouter
from api import oAuth2Api, productApi, recipeAPi, mashApi, historyApi, \
    fermentationApi, maltAPi, favoriteRecipesApi

router = APIRouter()
router.include_router(oAuth2Api.router)
router.include_router(productApi.router)
router.include_router(recipeAPi.router)
router.include_router(mashApi.router)
router.include_router(historyApi.router)
router.include_router(fermentationApi.router)
router.include_router(maltAPi.router)
router.include_router(favoriteRecipesApi.router)
