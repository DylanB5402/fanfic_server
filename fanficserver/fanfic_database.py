from json.decoder import JSONDecoder
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json

try:
    from fanficserver import url_parser
except:
    import url_parser

class FanFicDatabase():

    def __init__(self):
        cred = None
        try:
            cred = credentials.Certificate(json.loads(os.environ['FIREBASE_KEY']))
        except:
            cred = credentials.Certificate("keys/fanfic-server-firebase-adminsdk-r288u-1a705e4916.json")
        firebase_admin.initialize_app(cred)
        print('taco taoc')
        self.db = firestore.client()
        # doc_ref = self.db.collection('users').document('aturing').delete()
    
    def add_fic(self, url : str):
        id = url_parser.get_id_str(url)
        self.db.collection('fanfics').document(id).set({'title' : '', 'url' : url})

    def get_all_fics(self):
        fics = {}
        docs = self.db.collection('fanfics').stream()
        for doc in docs:
            fics.update({doc.id : doc.to_dict()})
        return fics