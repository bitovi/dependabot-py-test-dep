import datetime
import time
import uuid
import secrets
from enum import Enum

from .common import Agent


class DocumentStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

class Document:
    def __init__(self, documentId: str = None, **kwargs):
        self.documentId = documentId
        self.agent = Agent(**kwargs)
        self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        self.version = 1
        self.status = DocumentStatus.DRAFT
        self.content = None