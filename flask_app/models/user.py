from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self ,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friends = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('Friendships').query_db(query)
        data = []
        for user in results:
            data.append( cls(user) )
        return data

    @classmethod
    def get_friendships(cls):
        query = "SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users JOIN friendships ON users.id = friendships.user_id LEFT JOIN users as user2 ON friendships.friend_id = user2.id;"
        results = connectToMySQL('Friendships').query_db(query)
        print(results)
        friendships = []
        for friendship in results:
            user_and_friend = {
                'user_name': f"{friendship['first_name']} {friendship['last_name']}",
                'friend_name': f"{friendship['friend_first_name']} {friendship['friend_last_name']}"
            }
            friendships.append(user_and_friend)
        print(friendships)
        return friendships

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name,last_name,created_at,updated_at) VALUES ( %(first_name)s , %(last_name)s , NOW() , NOW() );"
        return connectToMySQL('Friendships').query_db( query, data )

    @classmethod
    def create_friendship(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('Friendships').query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        print(query)
        return connectToMySQL('Friendships').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('Friendships').query_db( query, data )

