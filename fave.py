from typing import List

import fave_api
from fave_api.rest import ApiException
from fave_api.models import Index, Document


class FaVe():
    def __init__(
            self,
            url: str = "http://localhost:1234",
    ) -> None:
        self._url = url

        configuration = fave_api.Configuration()
        configuration.host = url+"/v1"

        self._client = fave_api.DefaultApi(fave_api.ApiClient(configuration))
        
    def create_collection(
        self, collection: str, indexes: list[Index]
    ) -> None:
        colection = fave_api.Collection()
        colection.name = collection
        colection.indexes = indexes
        try:
            self._client.fave_create_collection(colection)
        except ApiException as e:
            raise Exception("%s\n" % e)
        
    def add_documents(
        self, collection: str, documents: list[Document], properties_to_vectorize: list[str]
    ) -> None:
        rqst = fave_api.AddDocumentsRequest()
        rqst.name = collection
        rqst.documents = documents
        rqst.properties_to_vectorize = properties_to_vectorize
        try:
            self._client.fave_add_documents(rqst)
        except ApiException as e:
            raise Exception("%s\n" % e)
        
    def get_document(
        self, collection, property, value: str
    ) -> Document:
        try:
            return self._client.fave_get_documents(property, value, collection)
        except ApiException as e:
            raise Exception("%s\n" % e)
        
    def get_nearest_documents(
        self, collection, query: str, limit: int, distance: float
    ) -> List[Document]:
        rqst = fave_api.NearestDocumentsRequest()
        rqst.name = collection
        rqst.text = query
        rqst.limit = limit
        rqst.distance = distance

        try:
            resp = self._client.fave_get_nearest_documents(rqst)
        except ApiException as e:
            raise Exception("%s\n" % e)
        return resp.documents
    
    def get_nearest_documents_by_vector(
        self, collection: str, vector: list[float],limit: int, distance: float
    ) -> List[Document]:
        rqst = fave_api.NearestDocumentsByVectorRequest()
        rqst.name = collection
        rqst.vector = vector
        rqst.limit = limit
        rqst.distance = distance

        try:
            resp = self._client.fave_get_nearest_documents_by_vector(rqst)
        except ApiException as e:
            raise Exception("%s\n" % e)
        return resp.documents