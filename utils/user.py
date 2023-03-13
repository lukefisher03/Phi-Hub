import time
import uuid
#The information used to store a user
class User:
    def __init__(self, acc_id, is_admin=False) -> None:
        self.acc_id = acc_id
        self.total_points = 0
        self.is_admin = is_admin
        self.points_log = dict()

    def add_pts(self, quantity:int, reason:str) -> str:
        '''
        Add an entry into the current user's points log.
        '''

        if not reason:
            return "No reason was given. Please give a reason for adding points to this user."

        self.total_points += quantity
        self.points_log[uuid.uuid4()] = {
            "quantity":quantity,
            "reason":reason,
            "timestamp": int(time.time())
        }

        return f"Added {quantity} points to account #{self.acc_id}"

    def rm_pts(self, id) -> str:
        '''
        Remove an entry from the points log

        Params: Account ID
        Returns: 
        '''
        if not self.points_log[id]:
            return f"Could not locate points entry!"

        entry = self.points_log[id]
        self.points_log.pop(id)

        return f"Successfully removed points: {entry}"

    def get_points(self) -> list:
        '''
        Returns the point log and total points for a user.

        Params: None
        Returns: [points_log, total_points]
        '''
        return [self.points_log, self.total_points]