from flask import Blueprint, jsonify, request
from app.models.db import db
from app.models.user import User  # Assuming you have a User model for created_by
from app.models.recipe import Recipe, RecipeIngredient  # Create these models for recipes and ingredients

recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.route('/getRecipes', methods=['GET'])
def get_recipes():
    try:
        # Fetch all recipes
        recipes = db.session.query(Recipe).join(User).order_by(Recipe.created_at.desc()).all()
        result = []
        
        for recipe in recipes:
            # Fetch ingredients for each recipe
            ingredients = db.session.query(RecipeIngredient).join(Stock).filter(RecipeIngredient.recipe_id == recipe.recipe_id).all()
            ingredients_list = [
                {
                    "ingredient_name": ingredient.stock.product_name,
                    "quantity": ingredient.quantity
                }
                for ingredient in ingredients
            ]
            result.append({
                "recipe_id": recipe.recipe_id,
                "recipe_name": recipe.name,
                "description": recipe.description,
                "created_at": recipe.created_at,
                "created_by": recipe.user.username,
                "ingredients": ingredients_list
            })

        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@recipe_routes.route('/addRecipe', methods=['POST'])
def add_recipe():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        created_by = data.get('created_by')

        if not name or not description or not created_by:
            return jsonify({"error": "Missing required fields."}), 400

        # Add the recipe to the database
        new_recipe = Recipe(name=name, description=description, created_by=created_by)
        db.session.add(new_recipe)
        db.session.commit()

        return jsonify({"message": "Recipe added successfully.", "recipe_id": new_recipe.recipe_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
