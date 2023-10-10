governorate_code = {
    "01": "Cairo",
    "02": "Alexandria",
    "03": "port said",
    "12": "Dakahlia",
    "16": "Gharbia",

}

faris = {
    "user_name": "farishamdi0000",
    "password": "123456",
    "name": "Faris Hamdi Rizk",
    "id": "",


}

amir = {
    "user_name": "amirhamdi0000",
    "password": "000000",
    "name": "Amir Hamdi Rizk",
    "id": "",

}

ibrahim = {
    "user_name": "ibrahimhamdi0000",
    "password": "666666",
    "name": "Ibrahim Hamdi Rizk",
    "id":"",

}

new_one = {
    "user_name": "",
    "password": "",
    "name": "",
    "id":"",

}



case_n = input("1 - Log in\n2 - Sign up\nEnter your registration case number : ")

if case_n == '1':
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_name == faris["user_name"] and password == faris["password"]:
        faris["id"] = input("Hello " + faris["name"] + "\nEnter your ID: ")
        print("birth date : " + faris["id"][5: 7] + " / " + faris["id"][3: 5] + " / " + "20" + faris["id"][1:3])
        print("Governorate : ", governorate_code[faris["id"][7:9]])

    elif user_name == amir["user_name"] and password == amir["password"]:
        amir["id"] = input("Hello " + amir["name"] + "\nEnter your ID: ")
        print("birth date : " + amir["id"][5: 7] + " / " + amir["id"][3: 5] + " / " + "20" + amir["id"][1:3])
        print("Governorate : ", governorate_code[amir["id"][7:9]])

    elif user_name == ibrahim["user_name"] and password == ibrahim["password"]:
        ibrahim["id"] = input("Hello " + ibrahim["name"] + "\nEnter your ID: ")
        print("birth date : " + ibrahim["id"][5: 7] + " / " + ibrahim["id"][3: 5] + " / " + "20" + ibrahim["id"][1:3])
        print("Governorate : ", governorate_code[ibrahim["id"][7:9]])

    else:
        print("Invalid username or password!! ")

elif  case_n == '2':
    new_one["name"] = input("Enter your name: ")
    new_one["user_name"] = input("Enter your username: ")
    new_one["password"] = input("Enter your password: ")
    new_one["id"] = input("Enter your ID: ")

    print("\nHello "+new_one["name"]+"\n")
    print("birth date : " + new_one["id"][5: 7] + " / " + new_one["id"][3: 5] + " / " + "20" + new_one["id"][1:3])
    print("Governorate : ", governorate_code[new_one["id"][7:9]])

else:
    print("Invalid input")






