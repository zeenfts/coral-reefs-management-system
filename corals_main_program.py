from functions.corals_crud_functions import (
    show_corals_lists, sort_corals_display, add_coral, delete_coral, update_coral, maintain_coral, completing_maintain_coral, exit_program
)
from functions.corals_helper_function import manager_pass, inspector_pass
import maskpass, textwrap

if __name__ == '__main__':
    print('\n======= Coral Reefs Management System =======')
    
    corals_dict = { #The main data Collection 
        'Code': ['CR001', 'CR002', 'CR003', 'CR004', 'CR005', 'CR006', 'CR007', 'CR008'],
        'Name': ['Branch Coral', 'Honeycomb Coral', 'Stinging Hydroid ', 'Leather Corals',
                'Cactus Coral', 'Hood Coral', 'Carnation Coral', 'Sea fans & Whip corals'],
        'Quantity': [100, 200, 170, 113, 78, 44, 185, 89],
        'Total Score': [95, 89, 95, 43, 83, 56, 97, 78],
        'Quality': ['Excellent', 'Very Good', 'Excellent', 'Poor', 'Very Good', 'Good', 'Excellent', 'Very Good'],
        'Type': ['Hard Corals', 'Hard Corals', 'Soft Corals', 'Soft Corals', 'Hard Corals', 'Hard Corals', 'Soft Corals', 'Soft Corals'],
        'Scientific Name': ['Acropora', 'Diploastrea heliopora', 'Aglaopheniidae', 'Sinularia',
                            'Pavona cactus', 'Stylophora pistillata', 'Nephtheidae', 'Subergorgia'],
        'Maintenance Cost': [100_000, 45_000, 78_000, 145_000, 175_000, 99_000, 56_000, 123_000]
    } # https://rajaampatbiodiversity.com/coral-types/

    current_session_global = []

    maintained_dict = {
        'Session': [],
        'Name': [],
        'Quantity': [],
        'Quality': [],
        'Maintenance Cost': [],
        'Total Cost': [],
        'Coral Code': []
    }

    role_choice_text = textwrap.dedent('''\n
    Corals Reef System Login Page

    What is your role?
    1. Manager
    2. Inspector

    Please write (1 or 2):\t
    ''')

    menu_text_admin = textwrap.dedent('''\n\
    [Manager] Welcome to Corals Reef System [Manager]\n\

    List Menu:
    1. Show Corals list
    2. Add Coral(s)
    3. Delete Coral(s)
    4. Update a Coral Detail
    9. Back to Login Page
    0. Exit Program
    
    What do you wanna do? (write the number 0-4, or 9):\t
    ''')

    menu_text_user = textwrap.dedent('''\n\
    [Inspector] Welcome to Corals Reef System [Inspector]\n\

    List Menu:
    1. Show Corals list
    2. Corals Check (Inspection)
    3. Show Still being Maintained Corals
    4. Completing the Maintained Corals
    9. Back to Login Page
    0. Exit Program
    
    What do you wanna do? (write the number 0-4, or 9):\t
    ''')

    while True:
        role_input = input(role_choice_text)

        if role_input not in {'1', '2'}: #wrong choice
            print('\nSorry, Please check if such role exists!')
            continue

        else:
            password_input = maskpass.askpass(prompt='Your Password: ', mask='*')

            if ((password_input not in manager_pass and role_input == '1') or
            (password_input not in inspector_pass and role_input == '2')):
                print('\nSorry, Please check for your password!')
                continue

            elif role_input == '1' and password_input in manager_pass: #admin role
                while True:
                    menu_input = input(menu_text_admin)

                    if menu_input == '1':
                        sort_corals_display(corals_dict)
                    elif menu_input == '2':
                        add_coral(corals_dict)
                    elif menu_input == '3':
                        delete_coral(corals_dict)
                    elif menu_input == '4':
                        update_coral(corals_dict)
                    elif menu_input == '9':
                        break
                    elif menu_input == '0':
                        exit_program()
                    else:
                        print('Sorry there is no choice of that menu!')
                        continue

            elif role_input == '2' and password_input in inspector_pass: #user role
                while True:
                    menu_input = input(menu_text_user)

                    if menu_input == '1':
                        sort_corals_display(corals_dict)
                    elif menu_input == '2':
                        maintain_coral(corals_dict, maintained_dict, current_session_global)
                    elif menu_input == '3':
                        print('>>>>>>> Still Being Maintained Corals <<<<<<<')
                        show_corals_lists(maintained_dict, 'Session')
                    elif menu_input == '4':
                        completing_maintain_coral(maintained_dict, corals_dict)
                    elif menu_input == '9':
                        break
                    elif menu_input == '0':
                        exit_program()
                    else:
                        print('Sorry there is no that menu!')
                        continue