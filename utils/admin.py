import uuid
import time
from user import User


class admin(User):
    def __init__(self, name, acc_id):
        super().__init__(name, acc_id)
        self.actions_list = dict()

    def approve_logs(self, user: User) -> None:
        '''
        Gets a users log of unnaproved requests

        Params: User
        Returns: None
        '''
        log = user.points_log

        for key in log:
            temp_rec = log[key]
            status = temp_rec['approved']
            userinfo = temp_rec['recommender']
            if status == False and userinfo != self.user_tag:
                print(f"{userinfo} requests {temp_rec['quantity']} for {temp_rec['reason']}")
                answer = input("Do you want to approve or deny this request? Y or N? ")
                if answer == "Y":
                    temp_rec['approved'] = True
                    temp_rec['approver'] = f"{self.name} #{self.acc_id}"
                    user.points_log[key] = temp_rec     
                    self.actions_list[key] = temp_rec
                    user.recommendations_approved[key] = temp_rec
                    
    def add_penalty_log(self, user: User, reason: str, quantity: int) -> None:
        '''
        This function will create a penalty log that will subtract points

        Params: user, reason, quantity
        Returns: None
        '''

        quantity = -abs(quantity)
        self.recomend_points(quantity, reason, user)

    def get_actions_list(self) -> dict:
        '''
        Returns a admins actions log

        Params: None
        Returns: actions_list
        '''

        return self.actions_list



    

        


        
            

        







    
    
        

