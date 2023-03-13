from user import User


class admin(User):
    def __init__(self, name, acc_id):
        super.__init__(name, acc_id)
    
    def print_user_info(user: User) -> None:
        '''
        The purpose of this function is to recieve a user object and print the users information

        Params: user 
        Returns: None
        '''
        print(user)

    def get_unapproved_logs(self, user: User) -> None:
        '''
        Gets a users log of unnaproved requests

        Params: User
        Returns: None
        '''
        log = user.points_log

        for key in log:
            temp_rec = log[key]
            status = temp_rec["approved"]
            if status == False:
                userinfo = temp_rec["recommender"]
                print(f"{userinfo[0]} requests {temp_rec['quantity']} for {temp_rec['reason']}")
                print("Do you want to approve or deny this request?")
                input()
            
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

        







    
    
        

