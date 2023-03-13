import time
from user import User


class admin(User):
    def __init__(self, name, acc_id):
        super.__init__(name, acc_id)
    
    def getuserinfo(user: User) -> None:
        '''
        The purpose of this function is to recieve a user object and print the users information

        Params: user 
        Returns: None
        '''
        print(user)

    def approve_request(self, recommendation: dict) -> None:
        '''
        This function will recieve a recommendation object and be able to approve it or deny it
        - which will in turn call a accessor method

        Params: recommendation
        Returns: one
        '''
        userinfo = recommendation["recommender"]
        print(userinfo[0] + " requests " + recommendation["quantity"] + " for " + recommendation['request'])
        time.sleep(10)
        print("Do you want to approve or deny this request?")


            
    def add_points(user: User, quantity: int) -> None:
        '''
        This function adds points to the user

        Params: User, quantity
        Returns: None
        '''
        user.total_points += quantity

    def remove_points(user: User, quantity: int) -> None:
        '''
        If a admin needs to remove points from a user, he can do so
        '''
        answer = input("Are you sure you want to remove" + quantity + "points from user" + user.name + "?")
        if answer == "Y":
            user.total_points -= quantity

        







    
    
        

