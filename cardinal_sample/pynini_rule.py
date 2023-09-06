from pynini import cdrewrite, closure,  union, cross
from pynini.lib.pynutil import add_weight
from pynini.lib.byte import SPACE, BYTE
from pynini.lib.pynutil import add_weight

# separators
and_rmv = cross(SPACE.ques + "and" + SPACE.ques, "")
space_rmv = cross(SPACE.star, "")
dash_rmv = cross("-", "")

# shortcuts
dash_space_rmv = union(space_rmv, dash_rmv)
dash_space_and_rmv = union(space_rmv, dash_space_rmv, and_rmv)
space_and_rmv = union(space_rmv, and_rmv)
zero_ins = cross("", "0")

# ground values
digit_no_zero = union(
    cross("one", "1"),
    cross("two", "2"),
    cross("three", "3"),
    cross("four", "4"),
    cross("five", "5"),
    cross("six", "6"),
    cross("seven", "7"),
    cross("eight", "8"),
    cross("nine", "9")
)

digit_zero = cross(union("zero", "oh", "naught" ), "0")
single_digit = union(digit_no_zero, digit_zero)
teens = union(
    cross("ten", "10"),
    cross("eleven", "11"),
    cross("twelve", "12"),
    cross("thirteen", "13"),
    cross("fourteen", "14"),
    cross("fifteen", "15"),
    cross("sixteen", "16"),
    cross("seventeen", "17"),
    cross("eighteen", "18"),
    cross("nineteen", "19"),
)

ties = union(
    cross("twenty", "2"),
    cross("thirty", "3"),
    cross("fourty", "4"),
    cross("fifty", "5"),
    cross("sixty", "6"),
    cross("seventy", "7"),
    cross("eighty", "8"),
    cross("ninety", "9"),
)

# suffix rmv
hundred_rmv = cross("hundred" + closure("s", 0, 1), "")
thousand_rmv = cross("thousand" + closure("s", 0, 1), "")

# compounds
two_digits = union(
    teens, 
    ties + closure(dash_space_and_rmv, 0, 1) + digit_no_zero, 
    ties + zero_ins
)

hundred_prefix = union(
    digit_no_zero + space_rmv + hundred_rmv,
    cross("a" + space_rmv + "hundred" + closure("s"), "1")
)

hundred_suffix = union(
    zero_ins + single_digit,  # 0X
    two_digits,  # XX
    add_weight(zero_ins.closure(2,2), 0.1),  # 00
)

three_digits = hundred_prefix + closure(space_and_rmv, 0, 1) + hundred_suffix

thousand_prefix_1_digit = union(
    digit_no_zero + space_rmv + thousand_rmv,
    cross(closure("a", 0, 1) + space_rmv + "thousand" + closure("s", 0, 1), "1")
)

thousand_suffix = union(
    three_digits,  # XXX
    add_weight(union(
        zero_ins.closure(2,2) + single_digit,  # 00X
        zero_ins + two_digits,  # 0XX
    ), 1),
    add_weight(zero_ins.closure(3,3), 2),  # 000
)

four_digits = union(
    thousand_prefix_1_digit + closure(space_and_rmv, 0, 1) + thousand_suffix,
    two_digits + space_rmv + hundred_rmv + space_and_rmv + hundred_suffix
)

five_digits = two_digits + space_rmv + thousand_rmv + closure(space_and_rmv, 0, 1) + thousand_suffix
six_digits = three_digits + space_rmv + thousand_rmv + closure(space_and_rmv, 0, 1) + thousand_suffix

cardinal = union(
    add_weight(single_digit, 40),
    add_weight(union(two_digits, three_digits), 30),
    add_weight(union(four_digits, five_digits, six_digits), 20)
)

rule_001 = cdrewrite(cardinal, "[BOS]" | SPACE, "[EOS]", BYTE.star)

FINAL_FSTs = [rule_001]