import argparse


# This list represents the ratios of an equal tempered tuning system that divides
# an octave into 12 equal tones.

# Starts with fundamental and ends with octave up, so 13 ratios are present

equal_temperament_ratios = [1.0, 1.059463, 1.122462, 1.189207, 1.259921, 1.334840, 1.414214, 1.498307, 1.587401,
                            1.681793, 1.781797, 1.887749, 2]

# Major Scale
# W W H W W W H

# These are a subset of the indices of our equal temperament chromatic scale
# Each index indicates a half step

major_scale = [0, 2, 4, 5, 7, 9, 10, 12]

# Major Pentatonic Scale
# Each value represents an index in a scale, and the list represents a subset of the scale.

major_penta_scale = [0, 1, 2, 4, 5]

# Natural Minor Scale
# W H W W H W W

natural_minor_scale = [0, 2, 3, 5, 7, 8, 10, 12]

# Minor Pentatonic Scale
# Each value represents an index in a scale, and the list represents a subset of the scale.

minor_penta_scale = [0, 2, 3, 4, 6]


# Minor 7th is 9

minor_seventh = 10


# Major Triad is 0,3,6

major_triad = [0, 2, 4]


def generate_scales(fundamental):

    print("Major Scale: \n", generate_major_scale(fundamental))
    print("Minor Scale: \n", generate_minor_scale(fundamental))
    print("Major Pentatonic Scale: \n", generate_major_penta_scale(fundamental))
    print("Minor Pentatonic Scale: \n", generate_minor_penta_scale(fundamental))
    print("7th: \n", generate_seventh(fundamental))


def generate_seventh(fundamental):

    freqs = generate_equal_tempered_frequencies(fundamental)
    major_freqs = generate_major_scale(fundamental)

    triad = [major_freqs[degree] for degree in major_triad]
    m_seventh = freqs[minor_seventh]

    triad.append(m_seventh)

    return triad



def generate_major_scale(fundamental):
    freqs = generate_equal_tempered_frequencies(fundamental)
    return [freqs[note] for note in major_scale]


def generate_major_penta_scale(fundamental):
    major_freqs = generate_major_scale(fundamental)
    return [major_freqs[degree] for degree in major_penta_scale]


def generate_minor_scale(fundamental):
    freqs = generate_equal_tempered_frequencies(fundamental)
    return [freqs[note] for note in natural_minor_scale]


def generate_minor_penta_scale(fundamental):
    minor_freqs = generate_minor_scale(fundamental)
    return [minor_freqs[degree] for degree in minor_penta_scale]


def generate_equal_tempered_frequencies(fundamental):
    return [x * fundamental for x in equal_temperament_ratios]


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fundamental", help="fundamental frequency in hz", required=True)
    args = parser.parse_args()
    generate_scales(float(args.fundamental))
