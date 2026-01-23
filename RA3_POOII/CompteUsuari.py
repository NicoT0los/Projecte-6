class CompteUsuari:
    def __init__(self, nom, email):
        self.nom = nom
        if "@" in email and "." in email:
            self.__email = email
        else:
            print("Email invàlid. Ha de contenir '@' i '.'")
            self.__email = ""
    
    def get_email(self):
        return self.__email
    
    def set_email(self, nou_email):
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email
            print(f"Email actualitzat a {self.__email}")
        else:
            print("Email invàlid. Ha de contenir '@' i '.'")