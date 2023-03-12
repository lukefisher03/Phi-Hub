from user import User

u = User(3459346)

u.add_pts(10, "Test 1")
u.add_pts(20, "Test 2")
u.add_pts(30, "Test 3")
u.add_pts(40, "Test 4")

print(u.get_points())