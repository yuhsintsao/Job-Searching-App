from common.database import Database

class Job(Database):
    def __init__(self, index, domain, updatedate, title, posteddate, company_id):
        self.index = index
        self.domain = domain
        self.update_date = updatedate
        self.title = title
        self.posted_date = posteddate
        self.id = company_id
    
    def _format2json(self):
        return {
            "index":self.index, 
            "domain":self.domain, 
            "update_date":self.update_date,
            "title":self.title, 
            "posted_date":self.posted_date, 
            "id":self.id
        }

    def _save2db(self):
        Database.insert_one(collection="job", data=self._format2json())
