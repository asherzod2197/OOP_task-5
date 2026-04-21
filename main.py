class PasswordManager:
    def __init__(self, password):
        self.password = password

    def check_strength(self):
        if len(self.password) >= 8:
            print("Kuchli parol")
        else:
            print("Zaif parol")

    def change(self, new_password):
        self.password = new_password
        print("Parol o‘zgartirildi")


# Obyekt
pm = PasswordManager("12345")
pm.check_strength()
pm.change("strong123")
pm.check_strength()
