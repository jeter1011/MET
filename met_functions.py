import numpy as np



def dec_to_2byteHex(decimal):
    hex_list = (np.array(decimal, dtype=np.int16)).byteswap(inplace=True)
    return list(map(hex, hex_list))


def hexlistToASCII(hexx):
    # initialize the ASCII code string as empty.
    ascii_ = ""

    # remove empty list slots : '0x0"
    trimmed = [i for i in hexx if i != '0x0']

    for i in range(len(trimmed)):
        # remove "x0"
        bytes_object = bytes.fromhex(trimmed[i].replace("0x", ""))
        # decode hex bytes into ASCII-pairs
        ascii_string = bytes_object.decode("ASCII")
        ascii_ = ascii_ + ascii_string

    return ascii_


def MC_word_ascii(mc_word):
    hexlist = (dec_to_2byteHex(mc_word))
    return hexlistToASCII(hexlist).rstrip('\x00')


def ieee_754_conversion(n, sgn_len=1, exp_len=8, mant_len=23):
    """
    Converts an arbitrary precision Floating Point number.
    Note: Since the calculations made by python inherently use floats, the accuracy is poor at high precision.
    :param n: An unsigned integer of length `sgn_len` + `exp_len` + `mant_len` to be decoded as a float
    :param sgn_len: number of sign bits
    :param exp_len: number of exponent bits
    :param mant_len: number of mantissa bits
    :return: IEEE 754 Floating Point representation of the number `n`
    """
    if n >= 2 ** (sgn_len + exp_len + mant_len):
        raise ValueError("Number n is longer than prescribed parameters allows")

    sign = (n & (2 ** sgn_len - 1) * (2 ** (exp_len + mant_len))) >> (exp_len + mant_len)
    exponent_raw = (n & ((2 ** exp_len - 1) * (2 ** mant_len))) >> mant_len
    mantissa = n & (2 ** mant_len - 1)

    sign_mult = 1
    if sign == 1:
        sign_mult = -1

    if exponent_raw == 2 ** exp_len - 1:  # Could be Inf or NaN
        if mantissa == 2 ** mant_len - 1:
            return float('nan')  # NaN

        return sign_mult * float('inf')  # Inf

    exponent = exponent_raw - (2 ** (exp_len - 1) - 1)

    if exponent_raw == 0:
        mant_mult = 0  # Gradual Underflow
    else:
        mant_mult = 1

    for b in range(mant_len - 1, -1, -1):
        if mantissa & (2 ** b):
            mant_mult += 1 / (2 ** (mant_len - b))

    return sign_mult * (2 ** exponent) * mant_mult


def unassigned_int(float_pair):
    """
    converts a 2 unit list into a 32bit binary string and returns an unassigned integer
    representation of a floating point

    :param float_pair: list[2]
    :return: unassigned integer
    """

    bin0 = bin(float_pair[0] % (1<<16))[2:]
    bin1 = bin(float_pair[1] % (1<<16))[2:]

    while len(bin0) < 16:
        bin0 = '0' + bin0

    while len(bin1) < 15:
        bin1 = '0' + bin1

    return int(bin1 + bin0, 2)


def float_converter(float_list):
    """
    """
    return ieee_754_conversion(unassigned_int(float_list), exp_len=8, mant_len=23)


def met2float(fulllist):

    float_values = []
    list_pairs = np.split(np.asarray(fulllist), int(len(fulllist)/2))
    for i in range(len(list_pairs)):
        float_values.append(round((float_converter(list_pairs[i])),3))

    return float_values

def met2bin(met, position):

    numpy_int = np.array(met, dtype=int)
    bin_met = bin(numpy_int[0] % (1 << 16))[2:]

    while len(bin_met) < 6:
        bin_met = '0' + bin_met

    return bin_met[-(position + 1)]


if __name__ == '__main__':

    a = [-26214, 16689, 20447, 16697, -26214, 16713, 5243, 16736, 26215, 16724]
    print(met2float(a))



