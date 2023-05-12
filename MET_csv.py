import pandas as pd

df = pd.read_csv('MET_Recipe.csv')
df['Device'] = df['Device'].astype('str')
df['Bit Place'] = df['Bit Place'].astype("Int64")

df.set_index("Variable", inplace=True)

def variable_data():
    return df

def variable_dict(name):
    return (df.loc[name]).to_dict()


def find_location_size(var_dict):
    # takes a dictionary of a Met Variable with all its properties
    # and returns the size of the "readsize" for pymc3e
    elements = var_dict['Elements']
    size = var_dict['Type Size']
    typ = var_dict['Type']
    bit = var_dict['Bit Place']
    position = var_dict['Position']

    match typ:
        case 'String':
            return position, size
        case 'Word':
            return position, elements * size
        case 'Float':
            return position, elements * size
        case 'Bit':
            return position, size



if __name__ == '__main__':

    test_var = "Polish_BrushAngleOffset"
    test_dict = variable_dict(test_var)
    device, size = find_location_size(test_dict)

    print(test_dict)
    print(size)





