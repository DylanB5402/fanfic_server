import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FanFicDatabase():

    def __init__(self):
        cred = credentials.Certificate("keys/fanfic-server-firebase-adminsdk-r288u-1a705e4916.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        doc_ref = self.db.collection(u'users').document(u'aturing')
        doc_ref.set({
            u'first': u'Alan',
            u'middle': u'Mathison',
            u'last': u'Turing',
            u'born': 1912
        })

d = FanFicDatabase()
