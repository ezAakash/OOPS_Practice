from project import chatbook

user = chatbook()
#user.get_name() = "System" #function call ko assignment operator ke saath kaise use kar raha huh , glat hai ye 
print(user.get_name())

user.set_name("System")
print(user.get_name())

print(user.get_name())

"""
    user._chatbook__name = 'System'
    print(user._chatbook__name)#in python we can't 100% hide the date 
    #but we can make it difficult to access the date by using __ . The idea behind this 
    #is to prevent the data from being modified by accident.
    #but we can access the data by using _classname__variable name
    #this is called name mangling
    #this is a way to make the data private
    #but it is not 100% private
    #it is just a way to make it difficult to access the data
    #but it is not impossible to access the data
"""
