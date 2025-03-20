from crud import create_user, read_users, update_user, delete_user  

# Test Create  
print("Creating users...")  
create_user('Alice', 'alice@example.com')  
create_user('Bob', 'bob@example.com')  

# Test Read  
print("Reading users...")  
users = read_users()  
for user in users:  
    print(user)  

# Test Update  
print("Updating user with id 1...")  
update_user(1, 'Alice Johnson', 'alice.johnson@example.com')  

# Test Read again to verify update  
print("Reading users after update...")  
users = read_users()  
for user in users:  
    print(user)  

# Test Delete  
print("Deleting user with id 2...")  
delete_user(2)  

# Final Read to verify deletion  
print("Reading users after deletion...")  
users = read_users()  
for user in users:  
    print(user)  