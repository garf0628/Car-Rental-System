#Car Rental System


#Function for the admin to login to the system
def admin_login():
    print("------------Login--------------")
    admin_id=input("Enter your admin ID: ")
    file=open("admin_data.txt",mode="r") 
    actual_admin=file.readline()
    flg=0
    while actual_admin!="":
        actual_admin=actual_admin.rstrip("\n").split("||")
        if admin_id==actual_admin[0]:
            flg+=1
            break
        actual_admin=file.readline()

    if flg==0:
        print("Wrong admin ID") 
        print("---------------------------")
        return admin_login()
    file.close()

    admin_password=input("Enter your password: ")
    if admin_password==(actual_admin[2]):
        print("Login successfull") 
    else:
        print("Wrong password")
        print("---------------------------")
        return admin_login()


#Function to show the admin menu
def admin_menu():
    print("----------Admin Menu------------")
    print("1. Add car to be rented out\n2. Modify car details\n3. View the records\n4. Return a rented car\n5. Exit")
    amenu_no=int(input("Please choose a number:"))
    if amenu_no==1:
        add_rented_car()
        return admin_menu()
    elif amenu_no==2:
        modify_car_details()
    elif amenu_no==3:
        view_records()
    elif amenu_no==4:
        return_rented_car()
    elif amenu_no==5:
        print("Thank you!")
    else:
        print("Wrong number")
        print("-----------------------------")
        return admin_menu()


#Function to add cars to be rented out
def add_rented_car():
    print("----------------------------")
    car_plate_number=input("Car plate number: ")
    car_model=input("Car model: ")
    seater=input("Number of seater in car: ")
    colour=input("Colour of the car: ")
    cost=input("Cost per day (RM): ")
    new_car_details=car_plate_number+"||"+car_model+"||"+seater+"||"+colour+"||"+cost+"||"+"Available"
    file=open("car_details.txt", mode="a")
    file.write("\n"+new_car_details)
    file.close()
    print("Sucessfull")
    print("----------------------------")


#Function to show all the car details and and modify option
def modify_car_details():
    file=open("car_details.txt",mode="r") 
    car_details=file.read()
    print(car_details)
    file.close()
    print("1. Modify car details\n2. Return")
    no=int(input("Please choose a number:"))

    if no==1:
        modify_car_details2()

    elif no==2:
        return admin_menu()

    else:
        print("Wrong number")
        print("----------------------------")
        return modify_car_details()


#Function to modify the car details
def modify_car_details2():
    print("------------------------------------------------------")
    platenumber=input("Enter the plate number of the car you want to change: ")
    file=open("car_details.txt",mode="r") 
    specific_car_details=file.readline()
    lineno=0
    while specific_car_details!="":
        if platenumber in specific_car_details: 
            break 
        specific_car_details=file.readline()
        lineno+=1 
    file.close()
    print("------------------------------------------------------")
    print(specific_car_details)
    olddata=input("Enter the data you want to change: ")
    newdata=input("Enter your new data: ")
    if olddata in specific_car_details:
        specific_car_details=specific_car_details.replace(olddata,newdata)
    else:
        print("Wrong data")
        print("---------------------------")
        return modify_car_details2()

    #To replace olddata in car_details.txt with newdata 
    file=open("car_details.txt",mode="r") 
    line=file.readlines()
    line[lineno]=specific_car_details
    file.close()
    file=open("car_details.txt",mode="w")
    file.writelines(line)
    file.close()
    print("Successfull!")
    return modify_car_details()


#Function to show menu for viewing records
def view_records():
    print("----------View Records------------")
    print("1. Cars rented out\n2. Cars available for rent\n3. Customer Booking\n4. Customer Payment\n5. Return")
    no=int(input("Please choose a number: "))
    if no==1:
        cars_rented_out()
        
    elif no==2:
        cars_available_for_rent()

    elif no==3:
        customer_booking()

    elif no==4:
        customer_payment()

    elif no==5:
        return admin_menu()
    else:
        print("Wrong number")
        print("---------------------------")
        return view_records()


#Function to view the records of the cars rented out
def cars_rented_out():
    print("----------Cars Rented Out------------")
    file=open("car_details.txt", mode="r")
    car_details=file.readline()
    while car_details!="":
        if "Rented out" in car_details:
            print(car_details)
        car_details=file.readline()
    file.close()

    return_to_previous_menu=input("Enter something to return to previous menu: ")
    return view_records()


#Function to veiw the records of the cars available for rent
def cars_available_for_rent():
    print("----------Cars Available For Rent------------")
    file=open("car_details.txt", mode="r")
    car_details=file.readline()
    while car_details!="":
        if "Available" in car_details:
            print(car_details)
        car_details=file.readline()
    file.close()

    return_to_previous_menu=input("Enter something to return to previous menu: ")
    return view_records()


#Function to view and search the records of customer booking
def customer_booking():
    print("----------Customer Booking------------")
    file=open("customer_booking.txt", mode="r")
    customer_booking_records=file.read()
    print(customer_booking_records)
    file.close()

    print("1. Search for a specific record\n2. Return")
    no=int(input("Please choose a number: "))
    if no==1:
        print("----------Search For Specific Record------------")
        specific_data=input("Enter a specific user name or car plate number: ")
        file=open("customer_booking.txt", mode="r")
        title=file.readline()
        print(title.rstrip("\n"))
        file.close()

        if specific_data in customer_booking_records:
            file=open("customer_booking.txt", mode="r")
            specific_record=file.readline()
            while specific_record!="":
                specific_record=specific_record.rstrip("\n")
                if specific_data in specific_record:
                    print(specific_record)
                specific_record=file.readline()
            file.close()
            print("---------------------------------------------")
            return_to_previous_menu=input("Enter something to return to previous menu: ")
            return customer_booking()

        else:
            print("Wrong data")
            print("--------------------------------------")
            return customer_booking()

    elif no==2:
        return view_records()

    else:
        print("Wrong number")
        print("--------------------------------------")
        return customer_booking()


#Function to view and search the records of customer payment
def customer_payment():
    print("----------Customer Payment------------")
    file=open("customer_payment.txt", mode="r")
    customer_payment_records=file.read()
    print(customer_payment_records)
    file.close()

    print("1. Search for a specific record\n2. Return")
    no=int(input("Please choose a number: "))
    if no==1:
        print("----------Search For Specific Record------------")
        specific_data=input("Enter a specific user name: ")
        file=open("customer_payment.txt", mode="r")
        title=file.readline()
        print(title.rstrip("\n"))
        file.close()
        if specific_data in customer_payment_records:
            file=open("customer_payment.txt", mode="r")
            specific_record=file.readline()
            while specific_record!="":
                specific_record=specific_record.rstrip("\n")
                if specific_data in specific_record:
                    print(specific_record)
                specific_record=file.readline()
            file.close()
            print("---------------------------------------------")
            return_to_previous_menu=input("Enter something to return to previous menu: ")
            return customer_payment()

        else:
            print("Wrong data")
            print("--------------------------------------")
            return customer_payment()

    elif no==2:
        return view_records()

    else:
        print("Wrong number")
        print("--------------------------------------")
        return customer_payment()


#Function to return a rented car
def return_rented_car():
    print("----------Return Rented Cars------------")
    file=open("customer_booking.txt", mode="r")
    customer_booking_records=file.read()
    print(customer_booking_records)
    file.close()
    
    carplatenumber=input("Enter the plate number of the car you want to return: ")
    file=open("customer_booking.txt", mode="r")
    specific_record=file.readline()
    flg=0
    lineno=0
    while specific_record!="":
        specific_record=specific_record.rstrip("\n").split("||")
        if carplatenumber in specific_record[1]:
            flg+=1
            print("Sucessfull")
            break
        specific_record=file.readline()
        lineno+=1
    if flg==0:
        print("Wrong car plate number")
        print("-----------------------------------------")
        return return_rented_car()
    file.close()

    file=open("customer_booking.txt", mode="r")
    data=file.readlines()
    del data[lineno]
    file.close()
    file=open("customer_booking.txt", mode="w")
    file.writelines(data)
    file.close()

    file=open("car_details.txt",mode="r")
    specific_car=file.readline()
    lineno=0
    while specific_car!="":
        if carplatenumber in specific_car:
            new_data=specific_car.replace("Rented out","Available")
            break
        specific_car=file.readline()
        lineno+=1
    file.close()
    file=open("car_details.txt",mode="r")
    data=file.readlines()
    data[lineno]=new_data
    file.close()
    file=open("car_details.txt",mode="w")
    file.writelines(data)
    file.close()

    file=open("customer_rental_history.txt", mode="a")
    newdata="||".join(specific_record)
    file.write("\n"+newdata)
    file.close()
    return admin_menu()


#Function for customers menu
def customer_menu():
    print("----------Customer Menu------------")
    print("1. Login\n2. Register\n3. View all cars available for rent\n4. Exit")
    cmenu_no=int(input("Please choose a number:"))
    if cmenu_no==1:
        customer_login()
    elif cmenu_no==2:
        register()
        customer_login()
    elif cmenu_no==3:
        viewing_rental_cars()
    elif cmenu_no==4:
        print("Thank you!")
    else:
        print("Wrong number")
        print("---------------------------")
        return customer_menu()


#Function for the customer to login to the system
def customer_login():
    print("----------Login------------")
    user_name=input("Enter your user name: ")
    file=open("user_data.txt",mode="r") 
    actual_user=file.readline()
    flg=0
    while actual_user!="":
        actual_user=actual_user.rstrip("\n").split("||")
        if user_name in actual_user[0]:
            flg+=1
            break
        actual_user=file.readline()

    if flg==0:
        print("Wrong user name") 
        print("---------------------------")
        return customer_login()
    file.close()

    user_password=input("Enter your password: ")
    if user_password==actual_user[1]:
        print("Login successful") 
    else:
        print("Wrong password")
        print("---------------------------")
        return customer_login()
        
    registered_customer_menu(user_name)


#Function for register
def register():
    print("----------Register------------")
    new_user_name=input("Enter your user name: ")
    new_user_password=input("Enter your password: ")
    newdata=new_user_name+"||"+new_user_password
    file=open("user_data.txt",mode="a")
    file.write("\n"+newdata)
    print("Register successful")
    file.close()


#Function for viewing all the cars available for rent
def viewing_rental_cars():
    print("----------Cars Available For Rent------------")
    file=open("car_details.txt",mode="r")
    column=file.readline()
    title=column.rstrip("\n").split("||")
    print(title[0],"||",title[1],"||",title[2],"||",title[3],"||",title[4])
    file.close()   
    file=open("car_details.txt",mode="r")
    car_details=file.readline()
    car_details=file.readline()
    while car_details!="":
        if "Available" in car_details:
            data=car_details.rstrip("\n").split("||")
            print(data[0],"||",data[1],"||",data[2],"||",data[3],"||",data[4])
        car_details=file.readline()
    file.close()

    
#Function for to show Registered Customer Menu
def registered_customer_menu(user_name):
    print("----------Registered Customer Menu------------")
    print("1. View, add and modify personal details\n2. View personal rental history\n3. View car details and Book a car\n4. Exit")
    rcmenu_no=int(input("Please choose a number:"))
    if rcmenu_no==1:
        personal_details(user_name)
    elif rcmenu_no==2:
        personal_rental_history(user_name)
    elif rcmenu_no==3:
        veiw_and_book_car(user_name)
    elif rcmenu_no==4:
        print("Thank you!") 
    else:
        print("Wrong number")
        print("---------------------------")
        return registered_customer_menu(user_name)


#Function to show the option for viewing, adding and modifying personal details
def personal_details(user_name):
    print("---------------------------------------")
    print("1. View and modify personal details\n2. Add personal details(For new users)\n3. Return to menu")
    no=int(input("Please choose a number:"))
    if no==1:
        personal_details2(user_name)     
    
    elif no==2:
        personal_details3(user_name)
        return personal_details(user_name)   

    elif no==3:
        return registered_customer_menu(user_name)

    else:
        print("Wrong number")
        print("---------------------------")
        return personal_details(user_name)


#Function for viewing and modifying personal data
def personal_details2(user_name):
    file=open("user_personal_details.txt",mode="r") 
    user_details=file.readline()
    lineno=0
    while user_details!="":
        if user_name in user_details: 
            break  
        user_details=file.readline()
        lineno+=1
    file.close()

    file=open("user_personal_details.txt",mode="r") 
    title=file.readline()
    print(title)
    print(user_details)
    file.close()
    print("1. Modify personal details\n2. Return")
    no2=int(input("Please choose a number:"))

    if no2==1:
        olddata=input("Enter the data you want to change: ")
        newdata=input("Enter your new data: ")
        if olddata in user_details:
            user_details=user_details.replace(olddata,newdata)
        else:
            print("Wrong data")
            print("---------------------------")
            return personal_details2(user_name)
        
        #To replace olddata in user_personal_details.txt with newdata 
        file=open("user_personal_details.txt",mode="r") 
        line=file.readlines()
        line[lineno]=user_details
        file.close()
        file=open("user_personal_details.txt",mode="w")
        file.writelines(line)
        file.close()
        print("Successfull!")
        return personal_details2(user_name) 

    elif no2==2:
        return personal_details(user_name)  

    else:
        print("Wrong number")
        print("---------------------------")
        return personal_details2(user_name)


#Function for adding personal data(new users)
def personal_details3(user_name):
    age=input("Enter your age: ")
    address=input("Enter your address: ")
    telephoneno=input("Enter your telephone number: ")
    email=input("Enter your E-mail address: ")
    drivinglicensenumber=input("Enter your driving license number: ")
    newdata=user_name+"||"+age+"||"+address+"||"+telephoneno+"||"+email+"||"+drivinglicensenumber
    file=open("user_personal_details.txt",mode="a")
    file.write("\n"+newdata)
    file.close()
    print("Successfull")


#Function for viewing personal history
def personal_rental_history(user_name):
    print("---------------------------------------------")
    print("----------Personal Rental History------------")
    file=open("customer_rental_history.txt",mode="r")
    rental_history=file.read()
    file.close()
    if user_name in rental_history:
        file=open("customer_rental_history.txt",mode="r")
        column=file.readline()
        title=column.rstrip("\n").split("||")
        print(title[1],"||",title[2],"||",title[3],"||",title[4],"||",title[5],"||",title[6])
        file.close()
        file=open("customer_rental_history.txt",mode="r")
        personalrentalhistory=file.readline()
        while personalrentalhistory!="":
            if user_name in personalrentalhistory:
                data=personalrentalhistory.rstrip("\n").split("||")
                print(data[1],"||",data[2],"||",data[3],"||",data[4],"||",data[5],"||",data[6])
            personalrentalhistory=file.readline()
        file.close()

    else:
        print("No Rental History")

    return_to_previous_menu=input("Enter something to return to previous menu: " )
    return registered_customer_menu(user_name)


#Function to view details and book a car 
def veiw_and_book_car(user_name):
    print("---------------------------------------------")
    print("----------Cars Available For Rent------------")
    file=open("car_details.txt",mode="r")
    column=file.readline()
    title=column.rstrip("\n").split("||")
    print(title[0],"||",title[1],"||",title[2],"||",title[3],"||",title[4])
    file.close()   
    file=open("car_details.txt",mode="r")
    car_details=file.readline()
    car_details=file.readline()
    while car_details!="":
        if "Available" in car_details:
            data=car_details.rstrip("\n").split("||")
            print(data[0],"||",data[1],"||",data[2],"||",data[3],"||",data[4])
        car_details=file.readline()
    file.close()
    print("---------------------------------------------")
    print("1. Booking car\n2. Return")
    num=int(input("Please choose a number: "))
    if num==1:
        booking_and_payment(user_name)
    
    elif num==2:
        return registered_customer_menu(user_name)
    
    else:
        print("Wrong number")
        print("---------------------------------------------")
        return veiw_and_book_car(user_name)


#Function to book a car and do payment to confirm booking 
def booking_and_payment(user_name):
    print("---------------Choose a Car----------------")
    carplatenumber=input("Please enter the plate number of the car you want to rent: ")
    file=open("car_details.txt",mode="r")
    car_details=file.read()
    file.close()
    if carplatenumber in car_details:
        print("----------Pick-up and Return Location-----------")
        location=input("Please enter a location for pick up and return the rental car: ")
        print("----------Pick-up Date------------")
        pick_up_year=int(input("Please enter a year: "))
        pick_up_month=int(input("Please enter a month: "))
        pick_up_day=int(input("Please enter a day: "))
        print("----------Return Date-------------")
        return_year=int(input("Please enter a year: "))
        return_month=int(input("Please enter a month: "))
        return_day=int(input("Please enter a day: "))
    
    else:
        print("Wrong plate number")
        return booking_and_payment(user_name)

    file=open("car_details.txt",mode="r")
    specific_car_details=file.readline()
    lineno=0
    while specific_car_details!="":
        if carplatenumber in specific_car_details:
            data=specific_car_details.rstrip("\n").split("||")
            price=int(data[4])
            break
        specific_car_details=file.readline()
        lineno+=1
    file.close()
    
    import datetime
    pick_up_date=datetime.date(pick_up_year,pick_up_month,pick_up_day)
    return_date=datetime.date(return_year,return_month,return_day)
    duration=(return_date-pick_up_date).days
    total_price=price*duration

    print("---------------------------------------------")
    print("Total price (RM)= ",total_price)
    print("1. Do payment with credit/debit card\n2. Add credit/debit card for payment\n3. Return")
    num=int(input("Please choose a number: "))
    if num==1:
        payment(user_name,total_price)

    elif num==2:
        add_creditordebit_card(user_name)
        payment(user_name,total_price)

    elif num==3:
        return veiw_and_book_car(user_name)

    else:
        print("Wrong number")
        print("---------------------------------------------")
        return booking_and_payment(user_name)
    
    file=open("customer_booking.txt",mode="a")
    file.write("\n"+user_name+"||"+carplatenumber+"||"+data[1]+"||"+location+"||"+str(pick_up_date)+"||"+str(return_date)+"||"+str(duration))
    file.close()

    file=open("customer_payment.txt",mode="a")
    file.write("\n"+user_name+"||"+carplatenumber+"||"+data[1]+"||"+str(pick_up_date)+"||"+str(return_date)+"||"+str(duration)+"||"+str(total_price))
    file.close()

    data[5]="Rented out"
    file=open("car_details.txt",mode="r")
    cardetails=file.readlines()
    cardetails[lineno]=data[0]+"||"+data[1]+"||"+data[2]+"||"+data[3]+"||"+data[4]+"||"+data[5]+"\n"
    file.close()
    file=open("car_details.txt",mode="w")
    file.writelines(cardetails)
    file.close()
    return registered_customer_menu(user_name)


#Function for credit/debit card verification
def payment(user_name,total_price):
    print("--------------Credit/debit Card Payment----------------")
    card_number=int(input("Please enter your credit/debit card number:"))
    file=open("customer_creditordebit_card.txt", mode="r")
    card_data=file.readline()
    while card_data!="":
        if user_name in card_data:
            card_data=card_data.rstrip("\n").split("||")
            break
        card_data=file.readline()
    file.close()
    if str(card_number)==card_data[1]:
        card_verification_number=int(input("Please enter your card verification number: "))
        if str(card_verification_number)==card_data[2]:
            print("Total price (RM)= ",total_price)
            no=int(input("Enter 1 to confirm the payment: "))
            if no==1:
                print("Thank you for your purchase!")
                print("-------------------------------------------------------") 
            else:
                print("Wrong number")
                print("-------------------------------------------------------") 
                return payment(user_name,total_price)

        else:
            print("Wrong card verification number")
            print("-------------------------------------------------------")
            return payment(user_name,total_price)
    
    else:
        print("Wrong credit/debit card number")
        print("-------------------------------------------------------")
        return payment(user_name,total_price)


#Function to add credit/debit card for payment
def add_creditordebit_card(user_name):
    print("--------------Adding Credit/debit Card----------------")
    cardnumber=int(input("Please enter your credit/debit card number: "))

    if len(str(cardnumber))==16:
        cardverificationnumber=int(input("Please enter your car verification number(e.g: xxx): "))
        if len(str(cardverificationnumber))==3:
            print("Successfull")
            print("------------------------------------------------------")
        else:
            print("Wrong format for card verification number")
            print("------------------------------------------------------")
            return add_creditordebit_card(user_name)
    
    else:
        print("Wrong format for credit/debit card number")
        print("------------------------------------------------------")
        return add_creditordebit_card(user_name)

    file=open("customer_creditordebit_card.txt", mode="a")
    file.write("\n"+user_name+"||"+str(cardnumber)+"||"+str(cardverificationnumber))
    file.close()
    

#Global Environment
print("----------Online Car Rental------------")
print("You are a/an:\n 1. Admin\n 2. Customer")
admin_or_customer=int(input("Please choose a number:"))
print("---------------------------------------")
if admin_or_customer==1:
    admin_login()
    admin_menu()
elif admin_or_customer==2:
    customer_menu()

else:
    print("wrong number")
