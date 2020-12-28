from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Franchise(Base):
    __tablename__ = "franchise"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    image = Column(String(250))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        """return object data in easily serializeable format"""
        return {"name": self.name, "id": self.id, "image": self.image}


class Player(Base):
    __tablename__ = "player"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    price = Column(String(80))
    position = Column(String(80))
    height = Column(String(80))
    weight = Column(String(80))
    image = Column(String(250))
    ppg = Column(Integer)
    youtube_url = Column(String(250))
    franchise_id = Column(Integer, ForeignKey("franchise.id"))
    franchise = relationship(Franchise)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
            "price": self.price,
            "position": self.position,
            "height": self.height,
            "weight": self.weight,
            "image": self.image,
            "ppg": self.ppg,
            "youtube_url": self.youtube_url,
        }


engine = create_engine("sqlite:///gamersnba.db")

Base.metadata.create_all(engine)
