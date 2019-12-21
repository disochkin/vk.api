import requests
from urllib.parse import urlencode

OAUTH_URL = "https://oauth.vk.com/authorize"
OAUTH_PARAMS = {
    "client_id": 7247906,
    "redirect_uri": "",
    "display": "page",
    "response_type": "token",
    "scope": "status,friends"
}
print("?".join(
    (OAUTH_URL, urlencode(OAUTH_PARAMS))
))
token = ""


class Vkuser:
    def __init__(self, id="0"):
#если id не задан создаем экземляр класса vkuser для текущего пользователя
        if int(id) != 0:
            response = requests.get(
                "https://api.vk.com/method/users.get",
                {"access_token": token,
                 "v": 5.101, "user_ids": str(id)})
        else:
            response = requests.get(
                "https://api.vk.com/method/users.get",
                {"access_token": token,
                 "v": 5.101})
        self.id = id
        try:
            self.first_name = response.json()["response"][0]["first_name"]
        except:
            self.first_name = "Ошибка доступа"
        try:
            self.last_name = response.json()["response"][0]["last_name"]
        except:
            self.first_name = "Ошибка доступа"


    def get_params(self):
        return {"access_token": token,
                "v": 5.101}

    def __and__(self, other):
        list_mutual_friends = []
        response = requests.get(
            "https://api.vk.com/method/friends.getMutual",
            {"access_token": token,
             "v": 5.101, "source_uid": self.id, "target_uid": other.id})
        for friend_id in response.json()["response"]:
            list_mutual_friends.append(Vkuser(friend_id))
        return list_mutual_friends

    def __str__(self):
        result = "https://vk.com/id" + str(self.id)
        return result


user = Vkuser()
user1 = Vkuser(6492)
user2 = Vkuser(2745)

list_mutual_friend = (user1 & user2)
for friend in list_mutual_friend:
    print(friend)


print(user1)
