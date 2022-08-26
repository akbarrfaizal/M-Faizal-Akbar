#Daftar Menu
#Membuat Data set yang merupakan dictionary dalam list terdiri dari 5 kolom data karyawan dengan 1 unique key
employee = [
    {'NRP' : 'JK19006', 'Nama' : 'Galih', 
    'Entity' : 'ABC', 'Golongan': '4A',
    'Status' : 'T0'},

    {'NRP' : 'JK22010', 'Nama' : 'Wafi',
    'Entity' : 'TTR', 'Golongan': '4A',
    'Status' : 'T0'},

    {'NRP' : 'JK06077', 'Nama' : 'Eko',
    'Entity' : 'GFE', 'Golongan': '4E',
    'Status' : 'M3'},

    {'NRP' : 'JK12456', 'Nama' : 'Agung Nugroho',
    'Entity' : 'EVR', 'Golongan': '4D',
    'Status' : 'M1'},

    {'NRP' : 'JK18027', 'Nama' : 'Ayu',
    'Entity' : 'DHY', 'Golongan': '4B',
    'Status' : 'M1'}
    ] 

def data_karyawan():     
    print(f"NRP    \t| Nama \t\t| Entity  | Gol  | Status")
    for x in employee:
        Nama2=(x['Nama']+((14-len(x['Nama']))*' '))
        NRP2=(x['NRP']+((8-len(x['NRP']))*' '))
        Entity2=(x['Entity']+((8-len(x['Entity']))*' '))
        Gol2=(x['Golongan']+((5-len(x['Golongan']))*' '))
        Stat2=(x['Status']+((2-len(x['Status']))*' '))
        print(NRP2+'| '+ Nama2+'| '+ Entity2+'| '+ Gol2+'| '+ Stat2)
#APPLICATION STARTS HERE

def main_menu():
    print('''
========= EMPLOYEE DATABASE of "PT. TITIEY" =========
1. Employee Data Report
2. Add Employee Data
3. Edit Employee Data
4. Delete Employee Data
5. Exit
''')
    menu_option = input('Please Choose the Menu [1-5]: ')
    if menu_option == '1':
        report_data()
    elif menu_option == '2':
        add_data()
    elif menu_option == '3':
        edit_data()
    elif menu_option == '4':
        delete_data()
    elif menu_option == '5':
        print ('\nThank You for Using Employee Database of "PT. TITIEY"')
        exit()
    else:
        main_menu()

#1. Employee Data Report "PT. TITIEY"
def report_data():
    while True:
        print ('''
========= EMPLOYEE DATABASE "PT. TITIEY" =========
1. All Employee Data Report
2. Employee Data Report with Filter
3. Back to Main Menu''')
        
        submenu1 = input('\nPlease Choose the Menu [1-3]: ')
        if submenu1 == '1':            
            
            data_karyawan()

        elif submenu1 == '2':
            #Jika database kosong maka akan muncul 'The Data is empty'
            if len(employee) == 0:
                print('\nThe Data is Empty')
            elif (len(employee)) != 0:
                NRP_Karyawan = input('\nInput NRP [8 Digits]: ')
                print (f'NRP: {NRP_Karyawan}')
                print(f"NRP \t\t| Nama \t\t\t| Entity \t| Golongan \t| Status")
                list_NRP = []
                for i in range (len(employee)):
                    list_NRP.append(employee[i]['NRP'])
                if NRP_Karyawan in list_NRP:
                    print(f"{NRP_Karyawan}\t\t| {employee[list_NRP.index(NRP_Karyawan)]['Nama']}\t\t\t| {employee[list_NRP.index(NRP_Karyawan)]['Entity']}\t\t| {employee[list_NRP.index(NRP_Karyawan)]['Golongan']}\t\t| {employee[list_NRP.index(NRP_Karyawan)]['Status']}\n")
                else:
                    print (f'There is no employee with NRP {NRP_Karyawan}')
               
        elif submenu1 == '3':
            main_menu()
        else:
            print('Please Input Correctly!')
            continue

#2. Add Employee Data
def add_data():
    while True:
        print ('''
======== Add Employee Data Menu ========
1. Add Employee Data
2. Back to Main Menu''')
        pilihan_submenu_2 = input('\nPlease Choose the Menu [1-2]: ')

        if pilihan_submenu_2 == '1':
#             print('''Aturan Input NRP standar perusahaan adalah 7 digit.
# 2 digit pertama menandakan kode lokasi penerimaan karyawan,
# Digit 3-4 menandakan tahun bergabungnya karyawan,
# 3 digit terakhir adalah urutan masuknya karyawan di perusahaan.''')
            NRP_karyawan_baru = input('Input NRP (8 Digits): ')
            if len (NRP_karyawan_baru) != 8:
                print ('Please input NRP correctly with no more/less than 8 digits')
                add_data()
            elif len (NRP_karyawan_baru) == 8:
                for i in employee:
                    if i['NRP'] == NRP_karyawan_baru:
                        print ('\nNRP is already listed in the database')
                        add_data()
                else:
                    print('Maximum characters for Name: 14')
                    Nama_Baru = input('Input Name: ').capitalize()
                    if len (Nama_Baru) > 14:
                        print('Maximum characters for Name: 14. Please Input again!')
                        add_data()
                    elif len (Nama_Baru) <= 14:
                        print('Maximum Characters for Entity: 3')
                        Entity_Baru = input('Input Entity: ').capitalize()
                    if len (Entity_Baru) > 3:
                        print('Maximum characters for Entity: 3. Please Input again!')  
                        add_data()                        
                    elif len (Entity_Baru) <= 3:
                        print('Maximum Characters for Golongan: 2')
                        Golongan_Baru = input ('Input Golongan: ')
                    if len (Golongan_Baru) > 2:
                        print('Maximum characters for Golongan: 2. Please Input again!')
                        add_data()
                    elif len (Golongan_Baru) <= 2:
                        print('Maximum Characters for Status: 3')
                        Status_Baru = input ('Input Status: ').capitalize()
                    if len (Status_Baru) > 2:
                        print('Maximum characters for Status: 2. Please Input again!')
                        
                    while True:
                        confirm = input('Proceed to save? (Y/N): ').capitalize()
                        if confirm == 'Y':
                            baris_baru = {'NRP':NRP_karyawan_baru, 'Nama' : Nama_Baru,  'Entity' : Entity_Baru, 'Golongan' : Golongan_Baru, 'Status' : Status_Baru}
                            employee.append(baris_baru)
                            print ('\nData Saved')
                            data_karyawan()
                            break
                        elif confirm == 'N':
                            add_data()
                        else:
                            print ('\nY/N')
        elif pilihan_submenu_2 == '2':
            main_menu()
        else:
            continue

#3. Edit Employee Data
def edit_data():
    while True:
        print ('''
======== Edit Employee Data Menu ========
1. Edit Employee Data
2. Back to Main Menu''')
        pilihan_submenu_3 = input('\nPlease Choose the Menu [1-2]: ')
        if pilihan_submenu_3 == '1':
            data_karyawan()
            Input_NRP = input('\nInput NRP: ')
            for i in employee:
                if Input_NRP == i['NRP']:
                    print (f"NRP: {i['NRP']}, Name: {i['Nama']}, Entity: {i['Entity']}, Golongan: {i['Golongan']}, Status: {i['Status']}")
                    while True:
                        konfirmasi_ubah = input('Proceed to save the edit? (Y/N)').capitalize()
                        if konfirmasi_ubah == 'Y':
                            editkolom = input('Choose a column to edit (NRP, Nama, Entity, Golongan, Status): ').lower()
                            if editkolom == 'NRP':
                                editkolom = editkolom.upper()
                            else:
                                editkolom = editkolom.capitalize()
                            editvalue = input(f'Input {editkolom} baru: ').capitalize()
                            while True:
                                konfirmasi_ubah2 = input('Proceed to save the edit? (Y/N)').capitalize()
                                if konfirmasi_ubah2 == 'Y':
                                    i[editkolom] = editvalue
                                    print ('\nData Edited')
                                    data_karyawan()
                                    edit_data()
                                elif konfirmasi_ubah2 == 'N':
                                    edit_data()
                                else:
                                    print ('\nPlease answer with Y/N !!')
                                
                        elif konfirmasi_ubah == 'N':
                            edit_data()
                        else:
                            print ('\nPlease answer with Y/N !!')
            else:
                print ('\nNRP is not available')
                edit_data()
        elif pilihan_submenu_3 == '2':
            main_menu()
        else:
            continue

#4. Delete Employee Data.
#Untuk melakukan deleting data, akan digunakan method delete
def delete_data():
    while True:
        print ('''
======== Delete Employee Data Menu ========      
1. Delete Employee Data
2. Back to Main Menu''')
        pilihan_submenu_4 = input('\nPlease Choose the Menu [1-2]: ')
        if pilihan_submenu_4 == '1':

            if len(employee) == 0:
                print ('\nDatabase is empty')
            elif len(employee) != 0:
                data_karyawan()
                delete = input('\nInput NRP to delete: ')
                list_NRP = []
                for i in range (len(employee)):
                    list_NRP.append(employee[i]['NRP'])
                if delete in list_NRP:
                    konfirmasi = input('\nProceed to delete data? (Y/N): ').capitalize()
                    if konfirmasi == 'Y':
                        del employee[list_NRP.index(delete)]
                        data_karyawan()

                        print('\nData has been removed')
                    elif konfirmasi == 'N':
                        print ('\nremove canceled')
                    else:
                        print('Y/N')
                else:
                    print (f'\nNRP {delete} is not available')
        elif pilihan_submenu_4 == '2':
            main_menu()
        else:
            continue

main_menu()           