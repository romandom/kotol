from sqlalchemy import Boolean, Column, Table, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base


favorite_recipes = Table(
    "favorite_recipes",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("recipe_id", ForeignKey("recipes.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    date = Column(String)
    is_active = Column(Boolean, default=True)
    recipes = relationship("Recipe", back_populates="user")
    products = relationship("Product", back_populates="user")
    favorite_recipe = relationship("Recipe", secondary=favorite_recipes, back_populates="user_favorite")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="products")
    online = Column(Boolean, default=False)
    name = Column(String)
    boiled = Column(Boolean)
    temperature = Column(String)
    temperatures = relationship("Boling", back_populates="product")
    actual_recipe = Column(String)


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tag = Column(String)
    beer_type = Column(String)
    degrees = Column(String)
    style = Column(String)
    shared = Column(Boolean)
    date = Column(String)
    ibu = Column(String)
    color = Column(String)
    alcohol = Column(String)
    decoction = Column(Boolean)
    infusion = Column(Boolean)
    info = Column(String)
    note = Column(String)
    mladina = Column(String)
    start_water = Column(String)
    splash_water = Column(String)
    mash_type = relationship("MashType", back_populates="recipe")
    hops_type = relationship("HopsType", back_populates="recipe")
    fermentation_type = relationship("FermentationType", back_populates="recipe")
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="recipes")
    malt = relationship("Malt", back_populates="recipe")
    mash = relationship("Mash", back_populates="recipe")
    fermentation = relationship("Fermentation", back_populates="recipe")
    user_favorite = relationship("User", secondary=favorite_recipes, back_populates="favorite_recipe")


class Malt(Base):
    __tablename__ = "malt"
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String)
    degrees = Column(Integer)
    info = Column(String)
    note = Column(String)
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"))
    recipe = relationship("Recipe", back_populates="malt")


class Mash(Base):
    __tablename__ = "mash"
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String)
    type = Column(String)
    amount = Column(String)
    info = Column(String)
    note = Column(String)
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"))
    recipe = relationship("Recipe", back_populates="mash")


class Fermentation(Base):
    __tablename__ = "fermentation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String)
    degrees = Column(String)
    info = Column(String)
    note = Column(String)
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"))
    recipe = relationship("Recipe", back_populates="fermentation")


# class History(Base):
#     __tablename__ = "history"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User", back_populates="history")
#     recipe_id = Column(Integer, ForeignKey("recipes.id"))
#     recipe = relationship("Recipe", back_populates="history")
#     date = Column(String)
#     note = Column(String)


class Boling(Base):
    __tablename__ = "boiling"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    product = relationship("Product", back_populates="temperatures")
    temperature = Column(String)
    time = Column(String)


class MashType(Base):
    __tablename__ = "mash_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    kilograms = Column(String)
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"))
    recipe = relationship("Recipe", back_populates="mash_type")


class HopsType(Base):
    __tablename__ = "hops_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    grams = Column(Integer)
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"))
    recipe = relationship("Recipe", back_populates="hops_type")


class FermentationType(Base):
    __tablename__ = "fermentation_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    amount = Column(Integer)
    grams = Column(Boolean)
    ml = Column(Boolean)
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"))
    recipe = relationship("Recipe", back_populates="fermentation_type")

