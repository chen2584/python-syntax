import requests

class myClass:
    variable = ""
    name = "Hello My name is Chen and "
    def getName(self, name):
        print(self.name, name)
    #def getNamez(name, lastname):
    #    print(name, " ", lastname)

#chen = raw_input("input yourname: ")
chen = input("input yourname: ")
print ("Test Hello World ", chen, " Dai")
print ("TestLine2")
if chen == "Chen":
    print("Chen Number 1")
    print("eiei")
elif chen == "Elle":
    print("Test Elle")
else:
    print("Who are you?")
chenClass = myClass()
#chenClass.getName("Chen")
chenClass.name = "Changed variable "
chenClass.getName("ChenZ")

chenClass2 = myClass()
chenClass2.getName("Chenz")

for x in range(5, 10):
    print("Hello Loop ", x)
testVariable = 555.5
testVariable = "Sawaddee"
print(testVariable)
jsonTest = requests.get("https://jsonplaceholder.typicode.com/posts/1").json()
print (jsonTest)
jsonVariable = jsonTest['title'];
#jsonVariable = jsonTest['results'][0]['address_components'][0]['long_name']
print("\n Title is " + jsonVariable)