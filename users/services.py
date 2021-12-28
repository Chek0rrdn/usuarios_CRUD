import csv
import os

from users.models import User


class UserService:
    def __init__(self, table_name):
        self.table_name = table_name
    

    def create_user(self, user):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=User.schema())
            writer.writerow(user.to_dict())
    

    def list_users(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=User.schema())
            return list(reader)
    

    def update_user(self, updated_user):
        users = self.list_users()

        updated_users = []
        for user in users:
            if user['uid'] == updated_user.uid:
                updated_users.append(updated_user.to_dict())
            else:
                updated_users.append(user)
        
        self._save_to_disk(updated_users)


    def delete_user(self, user):
        users_lists = self.list_users() 
        users_lists.remove(user[0])

        self._save_to_disk(users_lists)
    

    def _save_to_disk(self, users):
        tmp_table_name = self.table_name + '.tmp'
        
        with open(tmp_table_name, mode='a') as f:
            writter = csv.DictWriter(f, fieldnames=User.schema())
            writter.writerows(users)
        
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
    