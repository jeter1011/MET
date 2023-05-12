import pymcprotocol
import time

#
# test_name = "Name"
# test_key = metcsv.variable_dict(test_name)
# device, size = metcsv.find_location_size(test_key)
#
# print(f'{test_name}'":  ",test_key)


# if you use L series PLC,
# If you use ascii byte communication. (default is "binary")



# # read from "device" with (size) amount of spaces
# word = pymc3e.batchread_wordunits(headdevice=device, readsize=size)

def met_pull():
    pymc3e = pymcprotocol.Type3E(plctype="L")
    pymc3e.setaccessopt(commtype="ascii")
    pymc3e.connect("10.1.10.10", 10000)
    time.sleep(1)
    recipe1 = pymc3e.batchread_wordunits(headdevice='D9000', readsize=460)
    time.sleep(2)
    recipe2 = pymc3e.batchread_wordunits(headdevice='D9460', readsize=40)
    time.sleep(0.5)
    pymc3e.close()

    recipe = recipe1 + recipe2
    return recipe

if __name__ == '__main__':

    recipe_ = met_pull()

# print("\nData from MET: ", word)
#
# if test_key['Type']=='String':
#     word_string = mf.MC_word_ascii(word)
#     print(f'{test_name}'": ", word_string)
#
# if test_key['Type']=='Float':
#     print(mf.met2float(word))
#     #print(f'{test_name}'": list of float pairs: ", mf.met2float(word))
#     #print(f'{test_name}'": converted floats: ", mf.float_converter(word))
#
# if test_key['Type']=='Word':
#     print(f'{test_name}'": ", word[0])
#
# if test_key['Type']=='Bit':
#
#     bit_value = met_functions.met2bin(word, test_key['Bit Place'])
#     print(f'{test_name}'": ", bit_value)
#     if bit_value: print(True)
#     else: print(False)
