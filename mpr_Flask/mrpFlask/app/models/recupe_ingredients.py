from app.models.db import db
class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredients'

    id = db.Column(db.Integer, primary_key=True)  
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)  
    product_id = db.Column(db.Integer, db.ForeignKey('stock.product_id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)  

    recipe = db.relationship('Recipe', backref='ingredients')  
    stock = db.relationship('Stock', backref='recipe_ingredients') 
