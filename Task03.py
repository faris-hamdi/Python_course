import qrcode

governorate_code = {
    "01": "Cairo",
    "02": "Alexandria",
    "03": "Port Said",
    "04": "Suez",
    "11": "Damietta",
    "12": "Dakahlia",
    "13": "Elsharqia",
    "14": "Qalyubia",
    "15": "Kafr El-Sheikh",
    "16": "Elgharbia",
    "17": "Menoufia",
    "18": "Elbehira",
    "19": "Ismailia",
    "21": "Giza",
    "22": "Beni Suef",
    "23": "Fayoum",
    "24": "Minya",
    "25": "Assiut",
    "26": "Sohag",
    "27": "Qena",
    "28": "Aswan",
    "29": "Luxor",
    "31": "Red Sea",
    "32": "El wady elgedeed",
    "33": "Matrouh",
    "34": "North Sinai",
    "35": "South Sinai",
    "88": "You were born outside Egypt"

}

faris = {
    "user_name": "farishamdi0000",
    "password": "123456",
    "name": "Faris Hamdi Rizk",
    "id": "",
    "birth_cen": "",
    "birth_date": "",
    "governorate": "",
    "gender": "",
    "birth_order": "",

}

amir = {
    "user_name": "amirhamdi0000",
    "password": "000000",
    "name": "Amir Hamdi Rizk",
    "id": "",
    "birth_cen": "",
    "birth_date": "",
    "governorate": "",
    "gender": "",
    "birth_order": "",

}

ibrahim = {
    "user_name": "ibrahimhamdi0000",
    "password": "666666",
    "name": "Ibrahim Hamdi Rizk",
    "id": "",
    "birth_cen": "",
    "birth_date": "",
    "governorate": "",
    "gender": "",
    "birth_order": "",

}

new_one = {
    "user_name": "",
    "password": "",
    "name": "",
    "id": "",
    "birth_cen": "",
    "birth_date": "",
    "governorate": "",
    "gender": "",
    "birth_order": "",

}


# Your governorate_code, user profiles, and new_one dictionary remain the same

def generate_and_print_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Print the QR code to the console
    qr_img.show()


case_n = input("1 - Log in\n2 - Sign up\nEnter your registration case number : ")

if case_n == '1':
    user_name = input("Enter your username : ")
    password = input("Enter your password : ")

    if user_name == faris["user_name"] and password == faris["password"]:
        faris["id"] = input("\nHello " + faris["name"] + "\n\nEnter your ID: ")

        if faris["id"][0] == 2:
            faris["birth_cen"] = "1900 - 1999"
            print("birth century : " + faris["birth_cen"])
        else:
            faris["birth_cen"] = "2000 - 2099"
            print("birth century : " + faris["birth_cen"])

        faris["birth_date"] = faris["id"][5: 7] + " / " + faris["id"][3: 5] + " / " + "20" + faris["id"][1:3]
        print("birth date : " + faris["birth_date"])

        faris["governorate"] = governorate_code[faris["id"][7:9]]
        print("Governorate : ", faris["governorate"])

        if int(faris["id"][12]) % 2 != 0:
            faris["gender"] = "male"
            print("Gender : " + faris["gender"])
        else:
            faris["gender"] = "female"
            print("Gender : " + faris["gender"])

        faris["birth_order"] = faris["id"][9:13]
        print("Your birth order on your birthday : " + faris["birth order"] + "\nThank You.")

        # Call the function to generate and print the QR code
        generate_and_print_qr_code(faris)

    elif user_name == amir["user_name"] and password == amir["password"]:
        amir["id"] = input("\nHello " + amir["name"] + "\n\nEnter your ID: ")

        if amir["id"][0] == 2:
            amir["birth_cen"] = "1900 - 1999"
            print("birth century : " + amir["birth_cen"])
        else:
            amir["birth_cen"] = "2000 - 2099"
            print("birth century : " + amir["birth_cen"])

        amir["birth_date"] = amir["id"][5: 7] + " / " + amir["id"][3: 5] + " / " + "20" + amir["id"][1:3]
        print("birth date : " + amir["birth_date"])

        amir["governorate"] = governorate_code[amir["id"][7:9]]
        print("Governorate : ", amir["governorate"])

        if int(amir["id"][12]) % 2 != 0:
            amir["gender"] = "male"
            print("Gender : " + amir["gender"])
        else:
            amir["gender"] = "female"
            print("Gender : " + amir["gender"])

        amir["birth_order"] = amir["id"][9:13]
        print("Your birth order on your birthday : " + amir["birth order"] + "\nThank You.")

        generate_and_print_qr_code(amir)


    elif user_name == ibrahim["user_name"] and password == ibrahim["password"]:
        ibrahim["id"] = input("\nHello " + ibrahim["name"] + "\n\nEnter your ID: ")

        if ibrahim["id"][0] == 2:
            ibrahim["birth_cen"] = "1900 - 1999"
            print("birth century : " + ibrahim["birth_cen"])
        else:
            ibrahim["birth_cen"] = "2000 - 2099"
            print("birth century : " + ibrahim["birth_cen"])

        ibrahim["birth_date"] = ibrahim["id"][5: 7] + " / " + ibrahim["id"][3: 5] + " / " + "20" + ibrahim["id"][1:3]
        print("birth date : " + ibrahim["birth_date"])

        ibrahim["governorate"] = governorate_code[ibrahim["id"][7:9]]
        print("Governorate : ", ibrahim["governorate"])

        if int(ibrahim["id"][12]) % 2 != 0:
            ibrahim["gender"] = "male"
            print("Gender : " + ibrahim["gender"])
        else:
            ibrahim["gender"] = "female"
            print("Gender : " + ibrahim["gender"])

        ibrahim["birth_order"] = ibrahim["id"][9:13]
        print("Your birth order on your birthday : " + ibrahim["birth order"] + "\nThank You.")

        generate_and_print_qr_code(ibrahim)


    else:
        print("Invalid username or password!! ")

elif case_n == '2':
    new_one["name"] = input("Enter your name : ")
    new_one["user_name"] = input("Enter your username : ")
    new_one["password"] = input("Enter your password : ")
    new_one["id"] = input("Enter your ID : ")

    print("\nHello " + new_one["name"] + "\n")

    if new_one["id"][0] == 2:
        new_one["birth_cen"] = "1900 - 1999"
        print("birth century : " + new_one["birth_cen"])
    else:
        new_one["birth_cen"] = "2000 - 2099"
        print("birth century : " + new_one["birth_cen"])

    new_one["birth_date"] = new_one["id"][5: 7] + " / " + new_one["id"][3: 5] + " / " + "20" + new_one["id"][1:3]
    print("birth date : " + new_one["birth_date"])

    new_one["governorate"] = governorate_code[new_one["id"][7:9]]
    print("Governorate : ", new_one["governorate"])

    if int(new_one["id"][12]) % 2 != 0:
        new_one["gender"] = "male"
        print("Gender : " + new_one["gender"])
    else:
        new_one["gender"] = "female"
        print("Gender : " + new_one["gender"])

    new_one["birth_order"] = new_one["id"][9:13]
    print("Your birth order on your birthday : " + new_one["birth order"] + "\nThank You.")

    generate_and_print_qr_code(new_one)

else:
    print("Invalid inputs")
