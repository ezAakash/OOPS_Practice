class chatbook:
    """
    here class level variable's are declared 
    """
    id = 0
    def __init__(self):
        #want to give every user a unique id.
        chatbook.id += 1
        self.user_id = chatbook.id
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    '''
    we can build static method for the class , which have class level access rather object level access.
    what is static keyword in python in a nutshell?
    static keyword is used to define a static method in a class.
    static method is a method that belongs to the class rather than the object of a class.
    it is a method that is bound to the class and not the object of the class.
    '''
    @staticmethod
    def get_id():
        return id
    
    def set_id(id):
        chatbook.id = id 



    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name



    def menu(self):
        user_input = input(""""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()


    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            pwd = input("ENter your password here -> ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please input correct credentials..")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()


