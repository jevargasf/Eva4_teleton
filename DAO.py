from pymongo import MongoClient
from bson.objectid import ObjectId
from os import system

class DAO:
    
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["teleton"]
        self.collection = self.db["institutos"]
    
#--------------------------------------------------------------------------------------------------
    
    def registrar(self, datos):
        resultado = self.collection.insert_one(datos)
        return resultado.inserted_id
    
#--------------------------------------------------------------------------------------------------

    def comprobar_id(self, id):
        resultado = self.collection.count_documents({"_id": id})
        return resultado
    
#--------------------------------------------------------------------------------------------------    
    def obtener_todos(self):
        resultado = self.collection.find()
        return resultado
    
#--------------------------------------------------------------------------------------------------
    
    def cantidad_institutos(self):
        resultado = self.collection.count_documents({})
        return resultado
    
#--------------------------------------------------------------------------------------------------
    
    def obtener_buscados(self, id):
        resultado = self.collection.find({"_id":id})
        return resultado
    
#--------------------------------------------------------------------------------------------------
    
    def cantidad_institutos_condicion(self, condicion):
        cant = self.collection.count_documents({ "_id":condicion })
        return cant
    
#--------------------------------------------------------------------------------------------------
    
    def actualizar(self, id, datos_nuevos):
        resultado = self.collection.update_one(
            { "_id" : id },
            { "$set" : datos_nuevos }
        )
        return resultado.modified_count
    
#--------------------------------------------------------------------------------------------------
    
    def eliminar(self, id):
        resultado = self.collection.delete_one( { "_id":id } )
        return resultado.deleted_count
    