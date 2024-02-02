from datetime import datetime
from app.extensions import db


# 用户表
class User(db.Model):
    __tablename__ = 'users'
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    ProfilePicture = db.Column(db.String(255))
    Bio = db.Column(db.Text)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# 文章表
class Article(db.Model):
    __tablename__ = 'articles'
    ArticleID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=False)
    user = db.relationship('User', backref='articles')
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    Published = db.Column(db.Boolean, default=False)


# 评论表
class Comment(db.Model):
    __tablename__ = 'comments'
    CommentID = db.Column(db.Integer, primary_key=True)
    ArticleID = db.Column(db.Integer, db.ForeignKey('articles.ArticleID'), nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)


# 标签表
class Tag(db.Model):
    __tablename__ = 'tags'
    TagID = db.Column(db.Integer, primary_key=True)
    TagName = db.Column(db.String(255), nullable=False)


# 文章-标签关联表
class ArticleTag(db.Model):
    __tablename__ = 'article_tags'
    ArticleID = db.Column(db.Integer, db.ForeignKey('articles.ArticleID'), primary_key=True)
    TagID = db.Column(db.Integer, db.ForeignKey('tags.TagID'), primary_key=True)
