from sqlalchemy import Boolean, Column, Table, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from database import Base


favorite_recipes = Table(
    "favorite_recipes",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("recipe_id", ForeignKey("recipes.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    date = Column(String)
    is_active = Column(Boolean, default=True)
    recipes = relationship("Recipe", back_populates="user")
    products = relationship("Product", back_populates="user")
    history = relationship("History", back_populates="user")
    favorite_recipe = relationship("Recipe", secondary=favorite_recipes, back_populates="user_favorite")


class Product(Base):
    __tablename__ = "products"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID, ForeignKey("users.id"))  # Add name of product
    user = relationship("User", back_populates="products")


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
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
    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="recipes")
    malt = relationship("Malt", back_populates="recipe")
    mash = relationship("Mash", back_populates="recipe")
    fermentation = relationship("Fermentation", back_populates="recipe")
    history = relationship("History", back_populates="recipe")
    user_favorite = relationship("User", secondary=favorite_recipes, back_populates="favorite_recipe")


class Malt(Base):
    __tablename__ = "malt"
    id = Column(UUID(as_uuid=True), primary_key=True)
    time = Column(String)
    degrees = Column(String)
    type = Column(String)
    amount = Column(String)
    info = Column(String)
    note = Column(String)
    recipe_id = Column(UUID, ForeignKey("recipes.id"))
    recipe = relationship("Recipe", back_populates="malt")


class Mash(Base):
    __tablename__ = "mash"
    id = Column(UUID(as_uuid=True), primary_key=True)
    time = Column(String)
    type = Column(String)
    amount = Column(String)
    info = Column(String)
    note = Column(String)
    recipe_id = Column(UUID, ForeignKey("recipes.id"))
    recipe = relationship("Recipe", back_populates="mash")


class Fermentation(Base):
    __tablename__ = "fermentation"
    id = Column(UUID(as_uuid=True), primary_key=True)
    time = Column(String)
    info = Column(String)
    note = Column(String)
    recipe_id = Column(UUID, ForeignKey("recipes.id"))
    recipe = relationship("Recipe", back_populates="fermentation")


class History(Base):
    __tablename__ = "history"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="history")
    recipe_id = Column(UUID, ForeignKey("recipes.id"))
    recipe = relationship("Recipe", back_populates="history")
    date = Column(String)
    note = Column(String)




