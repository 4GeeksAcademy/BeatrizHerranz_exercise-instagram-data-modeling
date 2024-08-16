import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    firstname = Column(String(200), nullable=False)
    lastname = Column(String(200), nullable=False)
    email= Column(String(200))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(200), nullable=False)
    url= Column(String(250))
    post_id= Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(String(60), primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text= Column(String(25000))
    author_id= Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(String(60), primary_key=True)
    user_to_id= Column(Integer, ForeignKey('user.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')