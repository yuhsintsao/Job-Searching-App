from models.query import Query
from models.job import Job
from models.company import Company
import pandas as pd

class Menu(object):
    
    @staticmethod
    def search_job(from_date, to_date, title):
        query = Query()
        query.on_calendar(from_date, to_date)
        query.by_title(title)

        search_result = pd.DataFrame(Job.find(collection="job", query=query._query))
        return search_result

    @staticmethod
    def search_company(location, region, country):
        query = Query()
        query.by_location(location)
        query.by_region(region)
        query.by_country(country)

        search_result = pd.DataFrame(Company.find(collection="company", query=query._query))
        return search_result

    @classmethod
    def search_both(cls, from_date, to_date, title, location, region, country):

        searchJob = cls.search_job(from_date, to_date, title)
        searchCompany = cls.search_company(location, region, country)
        if not searchJob.empty:
            search_result = searchJob.merge(searchCompany, how="left", on='id')
            return search_result
        else:
            return pd.DataFrame()

    def group_by(cls, data, attribute):

        if not data.empty:
            search_result = data.groupby([attribute]).size().to_frame(name='count')
            return search_result
        else:
            return data
    

    

    
















