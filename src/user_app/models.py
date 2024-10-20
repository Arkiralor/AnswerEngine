from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId as PyObjectId
from uuid import uuid4

from ..database.methods import SynchronousMethods
from ..database.collections import DatabaseCollections

class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default_factory=lambda: uuid4().hex)
    username: str = Field(min_length=8, max_length=16)
    email: str = Field(min_length=5, max_length=64)
    password: str = Field(...)

    def __str__(self):
        return self.email
    
    def __repr__(self):
        return self.__str__()
    
    def create(self):
        try:
            return SynchronousMethods.insert_one(data=self.__dict__, collection=DatabaseCollections.user)
        except Exception as ex:
            print(f"{ex}")
            return None
    
    def save(self):
        if not self.id:
            return self.create()
        else:
            return SynchronousMethods.update_one(_id=self.id, data=self, collection=DatabaseCollections.user)
    

class UserTokenModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default_factory=lambda: uuid4().hex)
    user: UserModel = Field(...)
    token: str = Field(...)
    blacklisted: bool = Field(default=False)

    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.__str__()