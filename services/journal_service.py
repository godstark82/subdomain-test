
from db_instance import get_db
from models.article_model import ArticleModel
from models.issue_model import IssueModel
from models.journal_model import JournalModel
from models.volume_model import VolumeModel
import services.volume_service
from firebase_admin import firestore
import json

db = get_db()


#! Article
def get_articles_issue(issue_id) -> list[ArticleModel]:
    articles = db.collection('articles').where(filter=firestore.FieldFilter('issueId', '==', issue_id)).get()
    article_models = []
    for article in articles:
        json_data = json.dumps(article.to_dict())
        model = ArticleModel.from_json(json_data)
        article_models.append(model)
    return article_models




#! Issue
def get_issues_volume(volume_id) -> list[IssueModel]:
    issues = db.collection('issues').where(filter=firestore.FieldFilter('volumeId', '==', volume_id)).get()
    issue_models = []
    for issue in issues:
        json_data = json.dumps(issue.to_dict())
        model = IssueModel.from_json(json_data)
        model.articles = get_articles_issue(model.id)
        issue_models.append(model)
    return issue_models

#! Volume 
def get_volumes_journal(journal_id) -> list[VolumeModel]:
    volumes = db.collection('volumes').where(filter=firestore.FieldFilter('journalId', '==', journal_id)).get()
    volume_models = []
    for volume in volumes:
        json_data = json.dumps(volume.to_dict())
        model = VolumeModel.from_json(json_data)
        model.issues = get_issues_volume(model.id)
        volume_models.append(model)
    return volume_models



def get_all_journals() -> list[JournalModel]:
    journals = db.collection('journals').get()

    journal_models = []
    for journal in journals:
        data = journal.to_dict()
        model = JournalModel()
        model.from_dict(data)
        journal_models.append(model)
    return journal_models

def get_journal(journal_id) -> JournalModel:
    journal = db.collection('journals').document(journal_id).get()
    if journal.exists:
        data = journal.to_dict()
        model = JournalModel()
        model.from_dict(data)
        model.volumes = get_volumes_journal(model.id)
        return model
    else:
        return None