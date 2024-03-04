import requests
# import Faker



API_END_POINT = "https://gorest.co.in/public/v2"
USER_SERVICE = "/users"


class TestApiSample001:

    def test_sample_001(self):
        # create a new user
        user_data = {
            "name": "Sushrut", # Faker.name(),
            "email": "sshroot123@yopmail.com", # Faker.email(),
            "gender": "male", # Faker.random_element(elements=("male", "female")),
            "status": "active" # Faker.random_element(elements=("active", "inactive"))
        }
        token = "d2f3f3c1b4c0cd851bf1cecda376d134cdde4b5a2714987a29f565ff634ee97b"
        headers = {
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json"
        }
        response = requests.post(API_END_POINT + USER_SERVICE, json=user_data, headers=headers)
        print(response.json())
        assert response.status_code == 201, "User creation failed"

