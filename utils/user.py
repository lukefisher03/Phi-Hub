import time
import uuid
#The information used to store a user
class User:
    def __init__(self, name, acc_id, is_admin=False) -> None:
        self.name = name
        self.acc_id = acc_id
        self.total_points = 0
        self.is_admin = is_admin

        self.points_log = dict()
        self.recommendations_given = dict()
        self.contact_info = dict()

    def __str__(self) -> str:
        return f"User ID: {self.acc_id}\nName: {self.name}\nTotal Points: {self.total_points}"

    def recomend_points(self, quantity:int, reason:str, user) -> str:
        '''
        Add an entry into the current user's points log.
        '''

        if not reason:
            return "No reason was given. Please give a reason for adding points to this user."

        rec_id = uuid.uuid4()
        rec = {
            "quantity":quantity,
            "reason":reason,
            "timestamp": int(time.time()),
            "approved":False,
            "approver": "",
            "recommender": [self.name, self.acc_id]
        }

        user.points_log[rec_id] = rec
        self.recommendations_given[rec_id] = rec
        return f"Recommendation for {quantity} points to be added to {user.name}'s account has been submitted"

    def get_points(self) -> list:
        '''
        Returns the point log and total points for a user.

        Params: None
        Returns: [points_log, total_points]
        '''

        return [self.points_log, self.total_points]