from functions.corals_helper_function import (
    _assign_quality_text, _confirmation_question, _update_each_column, _number_input_checker, _text_input_checker, _update_coral_indexs,
    _sort_corals_certain_column, _money_formatting_rupiah, _conversion_money_to_number, _conversion_number_to_money
)
from tabulate import tabulate
import os, re

def exit_program():
    '''
    Used to exit
    '''
    print('\nThanks for your support to a better sea life!')
    os._exit(0) # exit ok status

def show_corals_lists(corals_dict, column = 'Code'):
    '''
    Used to show up the the coral to be choosed
    '''
    if len(corals_dict) > 0:
        title_tbl = [i for i in corals_dict]

        if 'Maintenance Cost' in set(corals_dict.keys()):
            corals_dict['Maintenance Cost'] = _conversion_number_to_money(corals_dict)

        if len(corals_dict[column]) == 0:
            print('\nThere is no Coral\'s data at all, please consider to add it first!!')
    
        print(tabulate(corals_dict, headers=title_tbl, tablefmt="rounded_grid"))
    else:
        print('\nThere is no Data available!!')

def sort_corals_display(corals_dict):
    sort_instruction = '''
    How do you want to see the Corals list?
    1. Default Order
    2. Sorted by Certain Column (Ascending) [affect the database]
    3. Sorted by Certain Column (Descending) [affect the database]
    4. Filtered Specific Column(s) [does not affect the default database]
    5. Search by Coral's Name Column [does not affect the default database]

    Write the choice! (1-5)
    '''

    while True:
        sort_input_user = input(sort_instruction)

        if sort_input_user == '1':
            print('\n >>>>>>> Default Order Full List Corals <<<<<<<')
            _sort_corals_certain_column(corals_dict, default_order=True)
            show_corals_lists(corals_dict)
            break
        elif sort_input_user == '2':
            print('\n >>>>>>> Ascending Order Full List Corals <<<<<<<')
            _sort_corals_certain_column(corals_dict, 'Ascending')
            show_corals_lists(corals_dict)
            break
        elif sort_input_user == '3':
            print('\n >>>>>>> Descending Order Full List Corals <<<<<<<')
            _sort_corals_certain_column(corals_dict, ordering_way = 'Descending')
            show_corals_lists(corals_dict)
            break
        elif sort_input_user == '4':
            while len(corals_dict.keys()) > 0:
                filter_text_instruction = '''
                Write some columns you want to filtered!
                (if more than one split it by comma \",\" between each column)\t
                '''
                filter_column_choice_input = input(filter_text_instruction)
                splitted_column_name_unique = set([i.strip() for i in filter_column_choice_input.split(',') for key in corals_dict.keys() if i.strip() in key])

                if len(splitted_column_name_unique) == 0:
                    print('\nThere is no such column, please insert the right one!!')
                    continue

                filtered_corals_dict = {
                    key: corals_dict[key] for key in corals_dict.keys()
                    & splitted_column_name_unique
                }

                print('\n >>>>>>> Full List Corals several Columns Only <<<<<<<')
                show_corals_lists(filtered_corals_dict, list(filtered_corals_dict)[0])
                break
            break
        elif sort_input_user == '5':
            while len(corals_dict['Name']) > 0:
                coral_dict_searched = corals_dict.copy()

                for key in coral_dict_searched.keys():
                    coral_dict_searched[key] = []

                search_text_instruction = 'What Name of Corals, do you want to search?\n'
                search_coral_name = input(search_text_instruction)

                compiled_pattern = re.compile(search_coral_name, re.IGNORECASE)

                for coral_name in corals_dict['Name']:
                    compiled_pattern = re.compile(search_coral_name, re.IGNORECASE)
                    regex_search_status = bool(compiled_pattern.search(coral_name))

                    if regex_search_status:
                        idx_result_true = corals_dict['Name'].index(coral_name)

                        for key in coral_dict_searched.keys():
                            coral_dict_searched[key].append(corals_dict[key][idx_result_true])

                print('\n >>>>>>> Searched Corals based on Name <<<<<<<')
                show_corals_lists(coral_dict_searched)

                if len(coral_dict_searched['Code']) > 0:
                    break
                else:
                    print(f'\nNo Corals: {search_coral_name} exist!')
                    continue
            break   
        else:
            print('There is no such choice!')
            continue

# --------------------- Manager Section ---------------------
def add_coral(corals_dict):
    '''
    Used to adding new corals reef to the warehouse
    '''
    while True:
        print('\n ------- Add New Coral(s) -------')
        coral_name_input = input('Input New Coral\'s Name: ')
        coral_name_set = set([i for i in corals_dict.values()][1])
        # print(coral_name_set)
        prettify_coral_name = coral_name_input.title()

        if prettify_coral_name not in coral_name_set:
            corals_dict['Name'].append(coral_name_input.title())

            _number_input_checker('Input Coral\'s Quantity: ', corals_dict, 'Quantity')
            total_score = _number_input_checker('Input Coral\'s Quality Score: ', corals_dict, 'Total Score', 'float')
            _assign_quality_text(corals_dict, total_score)
            _text_input_checker('Input Coral\'s Type: ', corals_dict, 'Type')
            _text_input_checker('Input Coral\'s Scientific Name: ', corals_dict, 'Scientific Name')
            _number_input_checker('Input Coral\'s Maintenance Cost: ', corals_dict, 'Maintenance Cost', 'float')

            corals_dict['Code'] = _update_coral_indexs(corals_dict)

            print(f'{coral_name_input} Successfully Added!!\n')
            show_corals_lists(corals_dict)

        else:
            print('Already have that corals!')
            print('Please input a new one!')
            print('or Maybe you should consider to go for update menu!')

            text_ask_add_to_update = '\nWant to update the relevant Coral? (Y/n): '
            add_to_update_coral_input = _confirmation_question(text_ask_add_to_update)

            if add_to_update_coral_input.upper() == 'Y':
                exist_code_coral_from_name = corals_dict['Name'].index(prettify_coral_name)
                update_existing_coral_code = corals_dict['Code'][exist_code_coral_from_name]
                update_coral(corals_dict, update_existing_coral_code)
                break
            elif add_to_update_coral_input.lower() == 'n':
                continue
        
        feed_input = _confirmation_question('\nAdd more coral(s)? (Y/n): ')
        
        if feed_input.lower() == 'n':
            break

def delete_coral(corals_dict):
    '''
    Used to remove a coral or a bunch of corals from the warehouse
    '''
    print('\n ------- Full Corals List -------')
    show_corals_lists(corals_dict)

    while (len(corals_dict['Code']) > 0):
        del_input_idx = input(f'\nWhich Coral do you want to delete?\n(write the Code or write \'All\' to purge all the data)\n')
        if del_input_idx.title() == 'All':
            # corals_dict.clear()
            for key in corals_dict:
                corals_dict[key] = []
            print('Successfully delete all Data!')
            break
        if del_input_idx not in set(sorted(corals_dict['Code'])):
            print('\nThere is no such Coral!\n')
            continue
        else:
            # Delete Section
            code_to_be_deleted = corals_dict['Code'].index(del_input_idx)
            coral_name_deleted = corals_dict['Name'][code_to_be_deleted]

            for val in corals_dict.values():
                val.pop(code_to_be_deleted)

            print(f'{coral_name_deleted} Remove Successfully!')

            del_feed_input = _confirmation_question('Delete others Coral again? (Y/n): ')
            if del_feed_input.lower() == 'n':
                break
    print('\n ------- Full Corals List -------')
    show_corals_lists(corals_dict)

def update_coral(corals_dict, coral_code_exist_in_add = False):
    '''
    Used to update the name, quantity, quality score, type,
    scientific name,or maintenance cost of the coral in the list
    '''
    print('\n ------- Full Corals List to Update -------')
    show_corals_lists(corals_dict)
    print('\n ------- Corals List Update -------')
    change_coral = False

    while (len(corals_dict['Code']) > 0):
        code_coral_dict = set([val for val in corals_dict.values()][0])

        if not coral_code_exist_in_add:
            coral_code_to_update = input('Which Coral you want to update? (write the Code) ')
        elif coral_code_exist_in_add in code_coral_dict:
            coral_code_to_update = coral_code_exist_in_add

        if coral_code_to_update in code_coral_dict:
            row_coral_to_update = corals_dict['Code'].index(coral_code_to_update)

            _update_each_column(f'Update Coral\'s new Name: (current-> {corals_dict["Name"][row_coral_to_update]})\n>> ', corals_dict, 'Name', row_coral_to_update)
            _update_each_column(f'Update Coral\'s new Quantity: (current-> {corals_dict["Quantity"][row_coral_to_update]})\n>> ', corals_dict, 'Quantity', row_coral_to_update, 'int')
            score_quality_updated = _update_each_column(f'Update Coral\'s new Total Score: (current-> {corals_dict["Total Score"][row_coral_to_update]})\n>> ', corals_dict, 'Total Score', row_coral_to_update, 'float')
            _update_each_column(f'Update Coral\'s new Type: (current-> {corals_dict["Type"][row_coral_to_update]})\n>> ', corals_dict, 'Type', row_coral_to_update)
            _assign_quality_text(corals_dict, score_quality_updated, 'update', row_coral_to_update)
            _update_each_column(f'Update Coral\'s new Scientific Name: (current-> {corals_dict["Scientific Name"][row_coral_to_update]})\n>> ', corals_dict, 'Scientific Name', row_coral_to_update)
            _update_each_column(f'Update Coral\'s new Maintenance Cost: (current-> {corals_dict["Maintenance Cost"][row_coral_to_update]})\n>> ', corals_dict, 'Maintenance Cost', row_coral_to_update, 'float')
            change_coral = True
        else:
            print('Sorry there is no that Coral on the list, you should added it first!')
            continue

        if change_coral:
            name_coral_updated = corals_dict['Name'][row_coral_to_update]
            print(f'\nCoral: {name_coral_updated} updated successfully!\n')
            show_corals_lists(corals_dict)

            update_confirm_input = _confirmation_question('Update others Coral again? (Y/n): ')
            if update_confirm_input.lower() == 'n':
                break

# --------------------- Inspector Section ---------------------
def maintain_coral(corals_dict, maintained_dict, current_session = 0):
    '''
    Used to add a coral or few corals to the be maintained
    whether it is still in a good condition or not.

    In the end the user can exit directtly or run the program again
    '''
    if len(current_session) == 0:
        current_session.append(1)
    else:
        current_session[0] += 1
    
    while (len(corals_dict['Code'])  > 0):
        if sum(corals_dict['Quantity']) == 0:
            print('All corals still being Maintained!!')
            break
        
        print('\n------- Full List of Corals -------')
        show_corals_lists(corals_dict)

        code_to_maintain = input('\nInput Coral\'s code to be maintained! ')

        upd_feed_input = ''

        if code_to_maintain in corals_dict['Code']:
            code_to_maintain = corals_dict['Code'].index(code_to_maintain)
        else:
            print('There is no such Coral\'s Code\n')
            continue

        if corals_dict['Quantity'][code_to_maintain] > 0:
            while True:
                coral_qty_input = input(f'Input Coral Quantity ({corals_dict["Quantity"][code_to_maintain]} available): ')
                coral_qty_available = corals_dict['Quantity'][code_to_maintain]

                if coral_qty_input.isdigit():
                    coral_qty_input = int(coral_qty_input)
                else:
                    print('Please input a number!')
                    continue

                if coral_qty_input > coral_qty_available:
                    print('No coral available!')
                    continue
                else:
                    # _ = update_corals(corals_dict, maintained_dict, code_to_maintain, coral_qty_input)
                    current_session_index = 'SM' + str(current_session[0])
                    corals_dict['Maintenance Cost'] = _conversion_money_to_number(corals_dict)

                    coral_current_code = corals_dict['Code'][code_to_maintain]
                    coral_name_to_be_maintained = corals_dict['Name'][code_to_maintain]
                    coral_quality_to_be_maintained = corals_dict['Quality'][code_to_maintain]
                    coral_maintenance_cost = corals_dict['Maintenance Cost'][code_to_maintain]
                    coral_total_cost_maintenance = corals_dict['Maintenance Cost'][code_to_maintain] * coral_qty_input

                    maintained_dict['Total Cost'] = _conversion_money_to_number(maintained_dict, 'Total Cost')

                    if coral_name_to_be_maintained not in set(maintained_dict['Name']):
                        maintained_dict['Name'].append(coral_name_to_be_maintained) 
                        maintained_dict['Quantity'].append(coral_qty_input)
                        maintained_dict['Quality'].append(coral_quality_to_be_maintained)
                        maintained_dict['Maintenance Cost'].append(coral_maintenance_cost)
                        maintained_dict['Total Cost'].append(coral_total_cost_maintenance)
                        maintained_dict['Session'].append(current_session_index)
                        maintained_dict['Coral Code'].append(coral_current_code)
                        # _update_coral_indexs(maintained_dict, 'Session')
                    elif coral_name_to_be_maintained in set(maintained_dict['Name']):
                        code_available_maintained_coral = maintained_dict['Name'].index(coral_name_to_be_maintained)

                        if maintained_dict['Session'][code_available_maintained_coral] == current_session_index:
                            maintained_dict['Quantity'][code_available_maintained_coral] += coral_qty_input
                            maintained_dict['Quality'][code_available_maintained_coral] = coral_quality_to_be_maintained
                            maintained_dict['Maintenance Cost'][code_available_maintained_coral] = coral_maintenance_cost
                            maintained_dict['Total Cost'][code_available_maintained_coral] += coral_total_cost_maintenance
                            maintained_dict['Session'][code_available_maintained_coral] =  maintained_dict['Session'][code_available_maintained_coral]
                            maintained_dict['Coral Code'][code_available_maintained_coral] = coral_current_code
                        else:
                            maintained_dict['Name'].append(coral_name_to_be_maintained) 
                            maintained_dict['Quantity'].append(coral_qty_input)
                            maintained_dict['Quality'].append(coral_quality_to_be_maintained)
                            maintained_dict['Maintenance Cost'].append(coral_maintenance_cost)
                            maintained_dict['Total Cost'].append(coral_total_cost_maintenance)
                            maintained_dict['Session'].append(current_session_index)
                            maintained_dict['Coral Code'].append(coral_current_code)

                    corals_dict['Quantity'][code_to_maintain] -= coral_qty_input

                    print('')
                    current_session_maintained_dict = maintained_dict.copy()
                    for key in current_session_maintained_dict:
                        current_session_maintained_dict[key] = []

                    for idx_session in range(len(maintained_dict['Session'])):
                        if maintained_dict['Session'][idx_session] == current_session_index:
                            for key in maintained_dict:
                                current_session_maintained_dict[key].append(maintained_dict[key][idx_session])

                    total_price = sum(current_session_maintained_dict['Total Cost'])
                    current_session_maintained_dict['Total Cost'] = _conversion_number_to_money(current_session_maintained_dict, 'Total Cost')
                    maintained_dict['Total Cost'] = _conversion_number_to_money(maintained_dict, 'Total Cost')

                    show_corals_lists(current_session_maintained_dict, 'Session')
                    print(f'Total Maintenance Cost: {_money_formatting_rupiah(total_price)}')
                    break
            
            upd_feed_input = _confirmation_question('\nWant to maintain more? (Y/n): ')

            if upd_feed_input.lower() == 'n':
                break

        else:
            print(f'All {corals_dict["Name"][code_to_maintain]} still be maintained!')
            print('Please choose other Coral!\n')
            continue
        
    while (len(corals_dict['Code']) > 0):
        money_input = input('\nHow much your money? ')

        if money_input.isdigit():
            money_input = float(money_input)
        else:
            print('Please input correct amount of money as a number!')
            continue

        # total_price = sum(maintained_dict['Total Cost'])

        if money_input >= total_price:
            print('Thanks for maintaining the coral')
            if money_input > total_price:
                print(f'Here\'s your cashback {_money_formatting_rupiah(money_input - total_price)}')
            break
        else:
            print('Not enough money!')
            print(f'You lack {_money_formatting_rupiah(total_price - money_input)}')
            continue

    while (len(corals_dict['Code']) > 0):
        cont_input = input('\nWant to do other things? [Y: back to Inspector\'s Menu | n: exit program]\n')

        if cont_input.upper() == 'Y':
            print('\n------- Corals still being Maintained -------')
            show_corals_lists(maintained_dict, 'Session')
            break
        elif cont_input.lower() == 'n':
            print('\nThank you for saving the sea life!\n')
            os._exit(0) # exit ok status
    else:
        show_corals_lists(corals_dict)

def completing_maintain_coral(maintained_dict, corals_dict):
    while len(maintained_dict['Session']) > 0:
        show_corals_lists(maintained_dict, 'Session')
        session_chooser_input = input('\nWhich session already being maintained? (can only write "All" to finished all Corals)\n')

        if session_chooser_input.title() == 'All':
            for index_maintained in range(len(maintained_dict['Session'])):
                coral_code_maintain_finished = maintained_dict['Coral Code'][index_maintained]
                coral_qty_maintain_finished =  maintained_dict['Quantity'][index_maintained]
                code_to_update_maintain_finished = corals_dict['Code'].index(coral_code_maintain_finished)

                old_qty_coral = corals_dict['Quantity'][code_to_update_maintain_finished]
                old_total_score_coral = corals_dict['Total Score'][code_to_update_maintain_finished] * old_qty_coral
                new_total_score_coral = ( old_total_score_coral + (coral_qty_maintain_finished * 100) ) / (coral_qty_maintain_finished + old_qty_coral)

                corals_dict['Quantity'][code_to_update_maintain_finished] += maintained_dict['Quantity'][index_maintained]
                corals_dict['Total Score'][code_to_update_maintain_finished] = round(new_total_score_coral, 1)
                _assign_quality_text(corals_dict, new_total_score_coral, 'update', code_to_update_maintain_finished)

            for key in maintained_dict:
                maintained_dict[key] = []

            print('\nSuccessfully completing all the maintained Corals!! Thank You')
            break
    else:
        print('\nYou should maintain minimum a Coral first!!')
# https://rajaampatbiodiversity.com/coral-types/