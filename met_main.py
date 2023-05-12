import met_functions
import met_functions as mf
import MET_csv as metcsv
import connect
from IPython.display import display

recipe_: list

variables_df = metcsv.variable_data().reset_index()
variables_df.dropna(how='all', axis='columns')
variables_df = variables_df.loc[:, ~variables_df.columns.str.contains('^Unnamed')]

def met_connect():
    return connect.met_pull()

def met2variable (variable_name):

    variable_value = []
    test_key = metcsv.variable_dict(variable_name)
    position, size = metcsv.find_location_size(test_key)
    variable = recipe_[position:position + size]

    if test_key['Type']=='String':
        variable_value.append(mf.MC_word_ascii(variable).rstrip('\x00'))
        print(f'{variable_name}'": ", variable_value)


    if test_key['Type']=='Float':
        variable_value.append(mf.met2float(variable))


    if test_key['Type']=='Word':
        variable_value.append(variable)


    if test_key['Type']=='Bit':

        bit_value = met_functions.met2bin(variable, test_key['Bit Place'])
        variable_value.append(bit_value)

    return variable_value[0]

def pull_recipe():
    global recipe_
    recipe_ = met_connect()
    variables_df["Values"] = variables_df.apply(lambda x: met2variable(x["Variable"]), axis=1)
    return recipe_




if __name__ == '__main__':
    pull_recipe()