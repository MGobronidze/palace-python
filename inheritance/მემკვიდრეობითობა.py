class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def show_info(self):
        return f"User: {self.username}, Email: {self.email}"

class Admin(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    def show_permissions(self):
        return f"Admin Permissions: {', '.join(self.permissions)}"

class Guest(User):
    def show_info(self):
        return f"Guest User: {self.username}"

admin = Admin("admin123", "admin@example.com", ["edit", "delete", "create"])
guest = Guest("guest456", "guest@example.com")
print(admin.show_info())  # Output: User: admin123, Email: admin@example.com
print(admin.show_permissions())  # Output: Admin Permissions: edit, delete, create
print(guest.show_info())  # Output: Guest User: guest456