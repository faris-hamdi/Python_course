faris = {
    "user_name": "farishamdi0000",
    "password": "123456",
    "name": "Faris Hamdi",
    "id": "30309181203331",


}
amir = {
    "user_name": "amirhamdi0000",
    "password": "000000",
    "name": "Faris Hamdi",
    "id": "",

}
ibrahim = {
    "user_name": "ibrahimhamdi0000",
    "password": "666666",
    "name": "Ibrahim Hamdi",
    "id": "",

}
governorate_code = {
    "01": "Cairo",
    "02": "Alexandria",
    "03": "port said",
    "12": "Dakahlia",
    "16": "Gharbia",

}

user_name = input("Enter your username: ")
password = input("Enter your password: ")

if user_name == faris["user_name"] and password == faris["password"]:
    faris["id"] = input("Hello "+faris["name"]+"\nEnter your ID: ")
    print("birth date : " + faris["id"][5: 7]+" / " + faris["id"][3: 5] + " / " + "20"+faris["id"][1:3] )
    print("Governorate : ",governorate_code[faris["id"][7:9]])

elif user_name == amir["user_name"] and password == amir["password"]:
    amir["id"] = input("Hello "+amir["name"]+"\nEnter your ID: ")
    print("birth date : " + amir["id"][5: 7]+" / " + amir["id"][3: 5] + " / " + "20"+amir["id"][1:3] )
    print("Governorate : ",governorate_code[amir["id"][7:9]])

elif user_name == ibrahim["user_name"] and password == ibrahim["password"]:
    ibrahim["id"] = input("Hello "+ibrahim["name"]+"\nEnter your ID: ")
    print("birth date : " + ibrahim["id"][5: 7]+" / " + ibrahim["id"][3: 5] + " / " + "20"+ibrahim["id"][1:3] )
    print("Governorate : ",governorate_code[ibrahim["id"][7:9]])

else:
    print("Invalid username or password!! ")
    





