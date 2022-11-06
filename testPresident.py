import pytest
import requests

url_ddg = "https://api.duckduckgo.com"

united_presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren",
                     "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson",
                     "Grant", "Hayes", "Garfield", "Arthur",
                     "Cleveland", "Harrison", "Cleveland", "McKinley",
                     "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman",
                     "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Regan", "Bush", "Clinton",
                     "Bush", "Obama", "Trump", "Biden"]


@pytest.mark.parametrize('president', united_presidents)
def test_presidents(president):
    resp = requests.get(url_ddg + "/?q=Presidents of the United States&format=json")
    rsp_data = resp.json()
    president_in_result = bool
    for item in rsp_data["RelatedTopics"]:
        if president in item["Text"]:
            president_in_result = True
            break
        else:
            pass
    assert president_in_result
