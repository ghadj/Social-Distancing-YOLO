"""
This class is responsible for all core operations that involve image manipulation with JPEG encoding and decoding

Created by: Michael Konstantinou, Constandinos Demetriou, George Hadjiantonis
"""
import cv2
import numpy as np
import collections
from . Huffman3 import huffman, encode, decode, makenodes, iterate

def split_blocks(img, b_rows, b_cols):
    """
    Split a image to blocks (b_rows x b_cols).
    """

    vector_blocks = []
    iHeight, iWidth = img.shape

    for startY in range(0, iHeight, b_rows):
        for startX in range(0, iWidth, b_cols):
            block = img[startY:startY+b_rows, startX:startX+b_cols]
            vector_blocks.append(block)

    return vector_blocks


def dct(block):
    """
    Apply DCT for a block
    """

    # float conversion
    block_f = np.float32(block)
    # DCT
    block_dct = cv2.dct(block_f)

    return block_dct


def get_quantization_table():
    """
    Returns the quantization table.
    """

    q_table = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                        [12, 12, 14, 19, 26, 58, 60, 55],
                        [14, 13, 16, 24, 40, 57, 69, 56],
                        [14, 17, 22, 29, 51, 87, 80, 62],
                        [18, 22, 37, 56, 68, 109, 103, 77],
                        [24, 35, 55, 64, 81, 104, 113, 92],
                        [49, 64, 78, 87, 103, 121, 120, 101],
                        [72, 92, 95, 98, 112, 100, 130, 99]])

    return q_table


def quantization(block_dct, factor):
    """
    Quantization of DCT coefficients.
    """

    q_table = get_quantization_table()
    q_table = np.multiply(q_table, factor)

    block_q = np.floor(np.divide(block_dct, q_table) + 0.5)

    return block_q


def zigzag(block):
    """
    Zig-Zag 2d array rearrangement to 1d list.
    """

    b_rows, b_cols = block.shape
    list_zigzag = []
    i = j = 0

    list_zigzag.append(block[i][j])

    while 1:
        # step1 - right or down
        if j < b_cols-1:
            j += 1
        else:
            i += 1
        list_zigzag.append(block[i][j])
        # check if is the last element of array
        if i == b_rows-1 and j == b_cols-1:
            break

        # step2 - diagonal down
        while j != 0 and i < b_rows-1:
            i += 1
            j -= 1
            list_zigzag.append(block[i][j])
        # check if is the last element of array
        if i == b_rows-1 and j == b_cols-1:
            break

        # step3 - down or right
        if i < b_rows-1:
            i += 1
        else:
            j += 1
        list_zigzag.append(block[i][j])
        # check if is the last element of array
        if i == b_rows-1 and j == b_cols-1:
            break

        # step4 - diagonal up
        while i != 0 and j < b_cols-1:
            i -= 1
            j += 1
            list_zigzag.append(block[i][j])
        # check if is the last element of array
        if i == b_rows-1 and j == b_cols-1:
            break

    return list_zigzag


def dpcm(vectors_zigzag):
    """
    Apply DCPM on DC values
    """

    e = []
    e.append(vectors_zigzag[0][0])
    for k in range(1, len(vectors_zigzag)):
        e.append(vectors_zigzag[k][0] - vectors_zigzag[k-1][0])
    return e


def rcl(list_zigzag):
    """
    Apply RCL on AC values
    """

    list_rcl = []
    count = 0

    for i in range(1, len(list_zigzag)):
        if list_zigzag[i] == 0:
            count += 1
        if list_zigzag[i] != 0:
            list_rcl.append(count)
            list_rcl.append(list_zigzag[i])
            count = 0

    list_rcl.append(0)
    list_rcl.append(0)

    return list_rcl


def huffman_encode(myList):
    """
    Apply huffman the huffman algorithm for encoding on a list of nodes
    """

    # Find frequency of appearance for each value of the list
    counter = collections.Counter(myList)

    # Define list of probabilities as list of pairs (Unique item, Corresponding frequency)
    probs = []

    # Initialization of probabilities' list
    for key, value in counter.items():
        probs.append((key, np.float32(value)))

    # Creates a list of nodes ready for the Huffman algorithm 'iterate'.
    symbols = makenodes(probs)

    # Runs the Huffman algorithm on a list of "nodes". It returns a pointer to the root of a new tree of "internal nodes".
    root = iterate(symbols)

    # Encodes a list of source symbols.
    s = encode(myList, symbols)

    return s, root


def huffman_decode(s, root):
    # Decodes a binary string using the Huffman tree accessed via root
    d = decode(s, root)
    return d


def inv_dpcm(decode_dc):
    """
    Apply inverse DPCM
    """
    ie = []
    # leave first value of first vector as it is
    ie.append(decode_dc[0])
    for k in range(1, len(decode_dc)):
        ie.append(decode_dc[k] + ie[k-1])
    return ie


def inv_rlc(decode_list_ac, b_rows, b_cols):
    """
    Apply inverse RLC
    """

    count = 0
    inv_list_ac = []
    total = b_rows * b_cols - 1

    for i in range(0, len(decode_list_ac), 2):
        if decode_list_ac[i] == 0 and decode_list_ac[i+1] == 0:
            for j in range(total - count):
                inv_list_ac.append(0)
        elif decode_list_ac[i] == 0:
            inv_list_ac.append(decode_list_ac[i+1])
            count += 1
        else:
            for j in range(0, int(decode_list_ac[i])):
                inv_list_ac.append(0)
                count += 1
            inv_list_ac.append(decode_list_ac[i+1])
            count += 1

    return inv_list_ac

def inv_zigzag(list_zigzag, b_rows, b_cols):
    """
    Apply inverse Zig-zag data rearrangement
    """

    inv_zigzag_block = np.zeros(b_rows*b_cols).reshape(b_rows, b_cols)
    i = j = count = 0

    # first element
    inv_zigzag_block[i][j] = list_zigzag[count]
    count += 1

    while 1:
        # step1 - right or down
        if j < b_cols-1:
            j += 1
        else:
            i += 1

        inv_zigzag_block[i][j] = list_zigzag[count]
        count += 1
        # check if is the last element of array
        if i == b_rows-1 and j == b_cols-1:
            break

        # step2 - diagonal down
        while j != 0 and i < b_rows-1:
            i += 1
            j -= 1
            inv_zigzag_block[i][j] = list_zigzag[count]
            count += 1
        # check if is the last element of array
        if i == b_rows-1 and j == b_cols-1:
            break

        # step3 - down or right
        if i < b_rows-1:
            i += 1
        else:
            j += 1
        inv_zigzag_block[i][j] = list_zigzag[count]
        count += 1
        # check if is the last element of array
        if i == b_rows-1 and j == b_cols-1:
            break

        # step4 - diagonal up
        while i != 0 and j < b_cols-1:
            i -= 1
            j += 1
            inv_zigzag_block[i][j] = list_zigzag[count]
            count += 1
        # check if is the last element of array
        if i == b_rows-1 and j == b_cols-1:
            break

    return inv_zigzag_block


def inv_quantization(block, factor):
    """
    Apply inverse quantization to a single block
    """

    q_table = get_quantization_table()
    q_table = np.multiply(q_table, factor)
    # inverse Quantization of the DCT coefficients
    return np.multiply(block, q_table)


def inv_dct(block):
    """
    Apply inverse DCT to a single block
    """
    return cv2.idct(block)


def jpeg_encode(img_gray, factor, b_rows=8, b_cols=8):
    """
    Compress and image using the jpeg algorithm
    """
    vectors_zigzag = []
    encode_ac = []
    root_ac = []

    vectors_blocks = split_blocks(img_gray, b_rows, b_cols)

    # For each block calculate the following: DCT, Quantization and Zig-zag rearrangement
    # Afterwards, apply the huffman algorithm. For the huffman encoding we need to apply on it
    # RCL and DPCM. 
    for block in vectors_blocks:

        # Calculate DCT, Quantization and Zig Zag rearranged data
        block_dct = dct(block)
        block_q = quantization(block_dct, factor)
        list_zigzag = zigzag(block_q)
        vectors_zigzag.append(list_zigzag)

        # Now that zig-zag rearrangement applied calculate RCL based on AC cooefficients
        list_rcl = rcl(list_zigzag)

        # Apply huffman with RCL
        encode_list_rcl, root_list_rcl = huffman_encode(list_rcl)
        encode_ac.append(encode_list_rcl)
        root_ac.append(root_list_rcl)

    # Calculate DPCM based on DC cooefficients
    list_dc = dpcm(vectors_zigzag)

    # Apply huffman with DPCM
    encode_dc, root_dc = huffman_encode(list_dc)

    return encode_dc, encode_ac, root_dc, root_ac


def jpeg_decode(encode_dc, encode_ac, root_dc, root_ac, factor, iHeight, iWidth, b_rows=8, b_cols=8):
    """
    Decompresses an image the was compressed using the jpeg algorithm
    """

    # Initialize an empty image
    img_inv = np.empty(shape=(iHeight, iWidth))
    i = 0

    # Follow the opposite steps of jpeg_encode function
    # with the help of inverse functions

    # Apply huffman decoding
    decode_dc = huffman_decode(encode_dc, root_dc)
    decode_dc = [float(k) for k in decode_dc]
    inverse_dc = inv_dpcm(decode_dc)

    # For each block apply decoding
    for startY in range(0, iHeight, b_rows):
        for startX in range(0, iWidth, b_cols):

            # AC Cooefficients
            decode_ac_list = huffman_decode(encode_ac[i], root_ac[i])
            decode_ac_list = [float(k) for k in decode_ac_list]
            if len(decode_ac_list) == 0:
                decode_ac_list = [0, 0]

            # Find original/decoded cooefficients
            inv_coefficients = inv_rlc(decode_ac_list, b_rows, b_cols)
            inv_coefficients.insert(0, inverse_dc[i])

            # Find blocks before applying zig-zag rearrangement
            inv_zigzag_block = inv_zigzag(inv_coefficients, b_rows, b_cols)

            # Find blocks before applying quantization
            inv_quantization_block = inv_quantization(inv_zigzag_block, factor)
            inv_dct_block = inv_dct(inv_quantization_block)

            # From all the above find the inversed decoded image
            img_inv[startY:startY+b_rows, startX:startX+b_cols] = inv_dct_block
            i += 1

    np.place(img_inv, img_inv > 255.0, 255.0)  # saturation
    np.place(img_inv, img_inv < 0.0, 0.0)  # grounding

    # Case back to uint8 that opencv uses to store the images
    img_inv = np.uint8(img_inv)

    return img_inv