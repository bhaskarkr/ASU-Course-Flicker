import helper.account_helper as account_helper
import helper.csv_helper as csv_helper
import helper.chrome_helper_selenium as selenium_helper


# def process_each_user(data):
#     for row in data:
#         account_helper.login_and_logout_one_user(row[0], row[1])

def setup_selenium():

    url_open = "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&level=grad&promod=F&searchType=open&subject=CSE&term=2241"
    url = "https://catalog.apps.asu.edu/catalog-microservices/api/v1/search/classes?&refine=Y&advanced=true&campusOrOnlineSelection=A&honors=F&keywords=semantic&promod=F&searchType=all&subject=CSE&term=2237"
    url2 = "https://catalog.apps.asu.edu/catalog/classes/classlist?advanced=true&campusOrOnlineSelection=C&honors=F&keywords=semantic&promod=F&searchType=all&subject=CSE&term=2237"
    url3 = "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=A&honors=F&keywords=semantic&promod=F&searchType=open&subject=CSE&term=2237"
    url_all = "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&level=grad&promod=F&searchType=all&subject=CSE&term=2237"
    selenium_helper.open_chrome(url_open)


if __name__ == '__main__':

    # file_name = "credentials.csv"
    # data = csv_helper.open_file(file_name)
    # process_each_user(data)
    setup_selenium()