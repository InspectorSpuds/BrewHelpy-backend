from fastapi import APIRouter

router = APIRouter(
    
)


@router.get("/{user_id}/recently-viewed")
async def get_recently_viewed_recipes(user_id: str):
    """Get recently viewed recipes for a specific user"""
    return {"message": "fetching all recently viewed recipes..."}


@router.get("/{user_id}/{recipe_id}/")
async def get_recipe_details(user_id: str, recipe_id: int):
    """Get detailed information about a specific recipe for a user"""
    return {"message": f"getting recipe ({recipe_id}) details for user {user_id} beep boop..."}


@router.get("/{user_id}/{recipe_id}/{version}")
async def get_recipe_version_details(user_id: str, recipe_id: int, version: int):
    """Get detailed information about a specific recipe for a user"""
    return {"message": f"getting recipe ({recipe_id}) version {version} details for user {user_id}"}

@router.post("/create")
async def create_recipe():
    """Creates a new recipe"""
    return {"message": "creating a new recipe beep boop..."}

@router.delete("/recipes/remove/{recipe_id}")
async def delete_recipe(recipe_id: int):
    """Deletes recipe and all previous versions
       if owned by requested users"""
    return {"message": f"deleting recipe {recipe_id}..."}

@router.delete("/recipes/remove/{recipe_id}}/{version}")
async def delete_recipe_version(recipe_id: int, version: int):
    """Deletes a given recipes recipes version if valid"""
    return {"message": f"deleting version {version} of recipe {recipe_id}..."}

