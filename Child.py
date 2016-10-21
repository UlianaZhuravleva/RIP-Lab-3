import requests
import Base
from datetime import datetime

class Client(Base.BaseClient):
    param = None

    def __init__(self, url, methods):
        self.BASE_URL = url
        self.method = methods

    def generate_url(self, method):
        return '{0}/{1}'.format(self.BASE_URL, method)

    def _get_data(self, method):
        response = requests.get(self.generate_url(method), self.param)
        response.json()
        return response.json()

    def find_id(self, idf):
        try:
            cl_id1 = idf.get('response')
            cl_id = cl_id1[0].get('uid')
        except:
            print("Пользователь не найден")
            exit()
        return cl_id

    def find_age(self, date):
        try:
            bdate = datetime.strptime(date, '%d.%m.%Y')
        except: return None

        day_now = datetime.now().day
        month_now = datetime.now().month
        year_now = datetime.now().year

        age = year_now - bdate.year
        if (bdate.month == month_now and bdate.day > day_now) or bdate.month > month_now:
            age -= 1
        return age

    def count_friend(self, friends_list):
         if (friends_list == None):
             print ('Страница пользователя была удалена или заблокирована')
             exit()
         if (len(friends_list) == 0):
             print ("У пользователя нет друзей, либо они скрыты")
             exit()
         friends_count = {'Возраст не указан у: ':0}
         for friend in friends_list:
             bdate = friend.get('bdate')
             age = self.find_age(bdate)
             if (age == None):
                 friends_count['Возраст не указан у: '] += 1
                 continue
             if (friends_count.get(age) == None):
                 friends_count[age] = ''
             friends_count[age] += '#'
         return friends_count

    def print_list(self, list):
        print('Возраст не указан у: ', list['Возраст не указан у: '])
        del list['Возраст не указан у: ']
        for key in sorted(list):
            print(key, ': ', list[key])
