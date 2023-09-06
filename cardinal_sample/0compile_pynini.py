from pynini import Far
from pynini_rule import FINAL_FSTs

file_name = "pynini_rule.far"

with Far(file_name, "w", arc_type="standard", far_type="default") as sink:
    i = 1
    for fst in FINAL_FSTs:
        sink["rule_"+"{:0>3}".format(i)] = fst.optimize()
        i += 1