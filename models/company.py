from common.database import Database

class Company(Database):
    def __init__(self, lat, lon, locality, region, country, company_id):
        self.lat = lat
        self.lon = lon
        self.locality = locality
        self.region = region
        self.country = country
        self.id = company_id

    def _format2json(self):
        return {
            "lat":self.lat, 
            "lon":self.lon, 
            "locality":self.locality, 
            "region":self.region, 
            "country":self.country, 
            "id":self.id
        }

    def _save2db(self):
        Database.insert_one(collection="company", data=self._format2json())
    