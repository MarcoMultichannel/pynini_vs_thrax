from time import time
from pynini import Far, compose, shortestpath

#function to apply string 
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

print("Proof pynini is slower:")

#producing a long string and make it even longer of 2000 times
str_sample = """seventy-nine thousand and three hundred and fifty-eight eighty-six thousand and two hundred and thirty-three twenty-nine thousand nine hundred and fifty-five fourteen thousands and seven hundred and six fourty-six thousand and one hundred one fifty thousand two hundred and seventy-nine thousand and two hundred and seventy-nine six hundred and thirty-eight thousands one hundred and nine 477 thousand seven hundred and sixty nine eight hundred thousands"""

# use different string lenghts
str_multipliers = [1, 10, 100, 1000, 5000]
for str_multiplier in str_multipliers:
    in_str = " ".join([str_sample for _ in range(str_multiplier)])
    print("With string length="+str(len(in_str)))

    # measure 5 times and average measurements
    num_tests = 5
    time_pynini = 0
    time_thrax = 0
    for _ in range(num_tests):

        #pynini
        start = time()
        res = get_output_string(in_str, pynini_rules[0])
        duration = time() - start
        time_pynini += duration

        #thrax
        start = time()
        res = get_output_string(in_str, thrax_rules[0])
        duration = time() - start
        time_thrax += duration

    time_pynini /= num_tests
    time_thrax /= num_tests

    print("Pynini: "+str(time_pynini)+"s")
    print("Thrax: "+str(time_thrax)+"s\n")