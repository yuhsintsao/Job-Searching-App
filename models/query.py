class Query(object):

    def __init__(self):
        self._query = {}
        self._start_date = "2017-07-01"
        self._end_date = "2018-07-31" 

    def on_calendar(self, from_date, to_date):
        if from_date != "" and to_date != "":
            self._query["update_date"] = { "$gte": from_date,
                                           "$lte": to_date }
        elif from_date != "" and to_date == "":
            self._query["update_date"] = { "$gte": from_date,
                                           "$lte": self._end_date } 
        elif from_date == "" and to_date != "":
            self._query["update_date"] = { "$gte": self._start_date,
                                           "$lte": to_date }   
        else:
            self._query["update_date"] = { "$gte": self._start_date,
                                           "$lte": self._end_date }       
    
    def by_title(self, title):
        if title == "":
            pass
        else:
            self._query["title"] = { "$regex": title, "$options": "-i" }

    def by_company_id(self, companyList): 
            # self._query["id"] = { "$in": companyList }  
            pass

    def by_location(self, location):  
        if location == "":
            pass
        else:
            self._query["location"] = { "$regex": location, "$options": "-i" }
    
    def by_region(self, region):
        if region == "":
            pass
        else:
            self._query["region"] = { "$regex": region, "$options": "-i" }
    
    def by_country(self, country):
        if country == "":
            pass
        else:
            self._query["country"] = { "$regex": country, "$options": "-i" }

