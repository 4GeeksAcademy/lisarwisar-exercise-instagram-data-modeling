import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), primary_key=True)
    email = Column(String(100), primary_key=True)
    password = Column(String(100), nullable=False)
    bio_info = Column(String(100), nullable=True)
    user_image_url = Column(String(300), nullable=True)

class Stories(Base):
    __tablename__ = "Stories"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(Users)
    story_image_url = Column(String(300), nullable=False)

class Followers(Base):
    __tablename__ = "Followers"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(Users)

class Posts(Base):
    __tablename__ = "Post"
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(Users)

class Comments(Base):
    __tablename__ = "Comments"
    id = Column(Integer, primary_key=True)
    comment_content = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship(Users)
    post = relationship(Posts)

class Media(Base):
    __tablename__ = "Media"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Posts)
    media_type = Column(Integer, nullable=False)
    media_url = Column(String(300), nullable=False)

class Liked_Posts(Base):
    __tablename__ = "Liked Posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship(Users)
    post = relationship(Posts)

class Saved_Posts(Base):
    __tablename__ = "Saved Posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship(Users)
    post = relationship(Posts)
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
