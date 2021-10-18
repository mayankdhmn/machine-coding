class IDToUserMapping:
    def __init__(self, users):
        IDToUserMapping.id_to_user = {}
        for user in users:
            IDToUserMapping.id_to_user[user.get_id()] = user.get_name()
        
    def get_user(user_id):
        return IDToUserMapping.id_to_user[user_id]
