import requests
from django.core.files.base import ContentFile

from backend.consts import URL_FOR_SIGN, API_PATH
from backend.serializer import DocumentSerializer
from backend.utils import read_byte_file, save_file


def create_sign():
    pass


class CreateSign:

    def __init__(self, user, document):
        self.user = user
        self.document = document
        self.auth = 'Basic dGVzdGFwaUB0ZXN0LmFwaTpFd08yYXJ6eg=='
        self.user_req_id = None
        self.send_doc_id = None
        self.operation_id = None
        self.signed_document_id = None
        self.endswith_sign = '.sig'
        self.path = document.file.path.replace(document.name, '')


    def find_user(self, inn, snils):
        # auth = 'Basic dGVzdGFwaUB0ZXN0LmFwaTpFd08yYXJ6eg=='
        url = URL_FOR_SIGN + API_PATH + 'dss/find/available?snils={}&inn={}&profileType=2'.format(snils, inn)
        headers = {
            'Authorization': self.auth,
        }
        req = requests.get(url, headers=headers)
        self.user_req_id = req.json()[0]['RequestId']
        # Возвращаем ИД запроса пользователя
        return self.user_req_id


    def send_file_to_cloud(self):

        url = URL_FOR_SIGN + API_PATH + self.user_req_id + '/dss/document'

        headers = {
            "Content-Type": "application/octet-stream",
            'Authorization': self.auth,
            'FileName': self.document.name
        }


        content_file = read_byte_file(self.document.file.path)

        req = requests.post(url, headers=headers, data=content_file)
        self.send_doc_id = req.json()
        # Возвращаем ИД загрузки документа в облако
        return self.send_doc_id

    def init_sign(self):
        url = URL_FOR_SIGN + API_PATH + self.user_req_id + '/dss/operation/sign'

        data = {
            "Documents": [
                {
                    "RefId": self.send_doc_id,
                }
            ],
            "Detached": 'true',
        }
        headers = {
            "Content-Type": "application/json-patch+json",
            'Authorization': self.auth,
        }

        req = requests.post(url, headers=headers, json=data)
        self.operation_id = req.json()['Id']
        # Возвращаем ИД операции подписания
        return self.operation_id

    def init_confirm_operation(self):
        url = URL_FOR_SIGN + API_PATH + self.user_req_id + '/dss/operation/' + self.operation_id

        headers = {
            "Content-Type": "application/json-patch+json",
            'Authorization': self.auth,
        }

        requests.post(url, headers=headers)
        # Ничего не возвращает


    def get_document_id(self):

        url = URL_FOR_SIGN + API_PATH + self.user_req_id + '/dss/operation/' + self.operation_id

        headers = {
            'Authorization': self.auth,
        }

        req = requests.get(url, headers=headers)
        self.signed_document_id = req.json()['Result']['ProcessedDocuments'][0]['RefId']
        # Возвращаем ИД подписанного документа
        return self.signed_document_id


    def get_document(self):
        url = URL_FOR_SIGN + API_PATH + self.user_req_id + '/dss/document/' + self.signed_document_id

        headers = {
            'Authorization': 'Basic dGVzdGFwaUB0ZXN0LmFwaTpFd08yYXJ6eg==',
        }

        req = requests.get(url, headers=headers)

        save_file(req.content, self.path + self.document.name + self.endswith_sign)
        # self.document.sign_file = self.document.file.url + self.endswith_sign
        self.document.sign_file.save(self.document.name + self.endswith_sign, ContentFile(req.content))
        # self.document.save()

        # Сохраняет документ
