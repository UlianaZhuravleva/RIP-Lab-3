import Child
from datetime import datetime

print("     Вход: ")
user = Child.Client("http://api.vk.com/method", 'users.get')
user.param = 'user_ids='+input("Введите username или id пользователя: ")
print(" ")
print("     Выход: ")
print("Пользователь: ")
print(user.execute())
resp = user.execute()
id = user.find_id(resp)
print(" ")
print("Гистограмма распределения возрастов друзей пользователя, поступившего на вход: ")
friend = Child.Client('http://api.vk.com/method', 'friends.get')
friend.param = "user_id="+str(id)+"&fields=bdate"
friends = friend.execute()
friend_list = friends.get('response')
listf = friend.count_friend(friend_list)
friend.print_list(listf)