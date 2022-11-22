current_users = ['Fairouz', 'Anthony', 'Kate', 'Inductivo']
new_users = ['Fairouz', 'Kate', 'Danielle', 'Palabrica', 'Nava']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Unfortunately, \"" + new_user + "\" is already taken.")
    else:
        print("The username \"" + new_user + "\" is available.")