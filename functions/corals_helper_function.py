import locale

# --------------------- Miscellaneous Section (helper function) ---------------------
def _assign_quality_text(corals_dict, score_quality, method='add', row_coral_to_update=-1):
    '''
    helper to dynamically provide classification of quality based on the score
    * 90-100: 'Excellent'
    * 75-89: 'Very Good'
    * 55-74: 'Good'
    * 40-54: 'Poor'
    * 1-39: 'Very Poor'
    * 0: 'Damaged/Lost'

    -> method = add or update
    '''
    classification_quality = '-'

    if 90 <= score_quality <= 100:
        classification_quality = 'Excellent'
    elif 75 <= score_quality < 90:
        classification_quality = 'Very Good'
    elif 55 <= score_quality < 75:
        classification_quality = 'Good'
    elif 40 <= score_quality < 55:
        classification_quality = 'Poor'
    elif 1 <= score_quality < 40:
        classification_quality = 'Very Poor'
    elif score_quality == 0:
        classification_quality = 'Damaged/Lost'
    else:
        classification_quality = '-- Undefined --'

    if method == 'add':
        corals_dict['Quality'].append(classification_quality)
    elif method == 'update':
        corals_dict['Quality'][row_coral_to_update] = classification_quality

def _confirmation_question(text_ask_for_confirmation):
    while True:
        feedback_confirm_input = input(text_ask_for_confirmation)
        if feedback_confirm_input.upper() == 'Y' or feedback_confirm_input.lower() == 'n':
            break
        else:
            print('Please provide right choice!')
            continue

    return feedback_confirm_input
    
def _update_each_column(text_command_to_update, corals_dict, column_to_update, row_coral_to_update, cols_type='text'):
    if cols_type == 'int' or cols_type == 'float':
        while True:
            column_update_new_val = input(text_command_to_update)
            if column_update_new_val.isdigit():
                if cols_type == 'int':
                    column_update_new_val = int(column_update_new_val)
                elif cols_type == 'float':
                    column_update_new_val = float(column_update_new_val)
                corals_dict[column_to_update][row_coral_to_update] = column_update_new_val
                break
            else:
                print('Please insert a number as value!\n')
                continue

    elif cols_type == 'text':
        column_update_new_val = input(text_command_to_update).title()
        corals_dict[column_to_update][row_coral_to_update] = column_update_new_val

    return column_update_new_val

def _number_input_checker(input_text_command:str, corals_dict:dict, key_corals_dict:str, type_choice:str ='int'):
    while True:
        number_input = input(input_text_command)
        if number_input.isdigit():
            if type_choice == 'int':
                number_input = int(number_input)
            elif type_choice == 'float':
                number_input = float(number_input)
            corals_dict[key_corals_dict].append(number_input)
            break
        else:
            print('Please provide a number!')
            continue

    return number_input

def _text_input_checker(input_text_command:str, corals_dict:dict, key_corals_dict:str):
    text_input = input(input_text_command).title()
    corals_dict[key_corals_dict].append(text_input)

def _update_coral_indexs(corals_dict, column_idx = 'Code'):
    '''
    helper to update the Code or Session Maintained of each Coral
    '''
    code_list = corals_dict[column_idx]
    code_list.sort()

    if len(code_list) == 0:
        last_code = 'CR000'
    else:
        last_code = code_list[-1]
    
    num_of_code = int(last_code[-3:])
    num_of_code += 1

    str_num_code = str(num_of_code)
    len_str_num_code = len(str_num_code)

    if len_str_num_code == 1:
        num_of_code = '00' + str_num_code
    elif len_str_num_code == 2:
        num_of_code = '0' + str_num_code
    else:
        num_of_code = str_num_code

    if column_idx == 'Code':
        full_code_added = str(last_code[:-3]) + num_of_code
    elif column_idx == 'Session':
        full_code_added = 'SM' + num_of_code
    corals_dict[column_idx].append(full_code_added)

    return corals_dict[column_idx]

def _sort_corals_certain_column(corals_dict, ordering_way = 'Ascending', default_order = False):
    if default_order:
        sort_column_choice_input = 'Code'
    else:
        sort_column_choice_input = input('\nBased on What column you want to sort? ')

    if sort_column_choice_input in corals_dict:
        corals_dict['Maintenance Cost'] = _conversion_money_to_number(corals_dict)
        old_order_list = corals_dict[sort_column_choice_input].copy()

        if ordering_way.title() == 'Ascending':
            reverse_order = False
        elif ordering_way.title() == 'Descending':
            reverse_order = True
        
        pair_tuple_list = [index_value for index_value in enumerate(corals_dict[sort_column_choice_input])]
        pair_tuple_list.sort(reverse=reverse_order, key=lambda x: x[1])

        corals_dict[sort_column_choice_input] = [value_ordered[1] for value_ordered in pair_tuple_list]
        new_index_order = [index_value[0] for index_value in pair_tuple_list]

        for key_dict in corals_dict.keys():
            if key_dict != sort_column_choice_input:
                corals_dict[key_dict] = [corals_dict[key_dict][sorted_index] for sorted_index in new_index_order]

def _money_formatting_rupiah(amount_of_money, location = 'id_ID'):
    locale.setlocale(locale.LC_ALL, location)
    rupiah_amount = locale.currency(amount_of_money, grouping = True)
    return rupiah_amount

def _conversion_money_to_number(corals_dict, column = 'Maintenance Cost'):
    formatted_cost = []
    for cost in corals_dict[column]:
        if type(cost) == str:
            formatted_cost.append(int(''.join(cost[2:-3].split('.'))))
        else:
            formatted_cost.append(cost)
    return formatted_cost

def _conversion_number_to_money(corals_dict, column = 'Maintenance Cost'):
    formatted_cost = []
    for cost in corals_dict[column]:
        if type(cost) != str:
            formatted_cost.append(_money_formatting_rupiah(cost))
        else:
            formatted_cost.append(cost)
    return formatted_cost