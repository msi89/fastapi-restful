from fastapi import APIRouter
from blog.views import PostView
from blog.schemas import PostSchema

router = APIRouter()

view = PostView()


@router.get('/posts')
async def list_post():
    return await view.list(('author',))


@router.post('/posts')
async def create_post(post: PostSchema):
    return await view.store(**post.dict())
