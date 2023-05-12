import met_functions
import met_functions as mf
import MET_csv as metcsv
import pandas as pd



recipe_df = pd.read_csv('0625_EM_recipe.csv')
recipe_ = recipe_df['0'].values.tolist()
variables_df = metcsv.variable_data()

def met2variable (variable_name):

    variable_value = []
    test_key = metcsv.variable_dict(variable_name)
    position, size = metcsv.find_location_size(test_key)
    variable = recipe_[position:position + size]

    print("Variable_segment: ", variable)
    #print(f'{variable_name}'" Key:  ",test_key)

    if test_key['Type']=='String':
        variable_value.append(mf.MC_word_ascii(variable))


    if test_key['Type']=='Float':
        variable_value.append(mf.met2float(variable))


    if test_key['Type']=='Word':
        variable_value.append(variable)


    if test_key['Type']=='Bit':

        bit_value = met_functions.met2bin(variable, test_key['Bit Place'])
        variable_value.append(bit_value)
        if bit_value == '1': print(True)
        else: print(False)

    print(f'{variable_name}'": ", variable_value)
    return variable_value


if __name__ == '__main__':

    test_name = "CustomProcessDisabled"
    print(met2variable(test_name))
