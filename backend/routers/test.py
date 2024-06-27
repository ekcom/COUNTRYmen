from fastapi import APIRouter

# A test router,
# to ensure that the server is up
router = APIRouter(
    tags=["test"],
)

@router.get("/test")
async def test():
    return {"message": "test"}