from time import time
from pynini import Far, compose, shortestpath

def get_output_string(input_string, FST):
    compose_fst = compose(input_string, FST)
    result = shortestpath(compose_fst).string()
    return result

def load_far(file_name):
    rules = []
    with Far(file_name, "r", arc_type="standard", far_type="default") as sink:
        for _, rule in sink:
            rules.append(rule)
    return rules

thrax_rules = load_far("thrax_rule.far")
pynini_rules = load_far("pynini_rule.far")

print("For add_weight(\"a\", 10). Thrax has weights on states, Pynini on arcs.")
print("Thrax:")
print(thrax_rules[0])
print("Pynini:")
print(pynini_rules[0])
