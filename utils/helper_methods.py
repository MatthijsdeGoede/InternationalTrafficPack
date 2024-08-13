def get_os_path(path):
    return path.replace("/", "\\")


def get_characters_surrounding_substring(input_string, substring):
    # return the character proceeding and following the substring
    index = input_string.find(substring)
    ancestor = input_string[index - 1] if index > 0 else ""
    successor = input_string[index + len(substring)] if index > 0 and index + len(substring) < len(
        input_string) else "\n"
    return ancestor, successor


def replace_longest_substring(line, replacements, code):
    longest_replacement = ""
    for replacement in replacements:
        # find the longest matching substring
        if replacement in line and len(replacement) > len(longest_replacement):
            longest_replacement = replacement
    if longest_replacement:
        # ignore comments
        line = line.replace("\t\n", "\n")
        start = "\t" if "\t" in line else ""
        line = f"{start}{line.split('#')[0].strip()}\n"
        prev_char, next_char = get_characters_surrounding_substring(line, longest_replacement)
        # only replace internal names containing a .
        if next_char == "\n" or next_char == "." and prev_char == ".":
            # put country code after occurrence
            line = line.replace(longest_replacement, f"{longest_replacement}.{code}")
        elif prev_char == ".":
            # put country code at the end of the internal name
            line = line.replace("\n", f".{code}\n")
    return line


def prepare_internal_name(input_line, is_accessory=False):
    # deal with inconsistent internal names specified by scs
    split_line = input_line.split(".")[1:]
    accessory = ".".join(split_line[:-1] if is_accessory else split_line).split(" ")[0].strip()
    accessory = accessory.replace("traffic.", "")
    accessory = accessory.replace("trailer.", "")
    return accessory


def check_spawn_ratios(spawn_config, country_dict):
    supported_countries = set(country_dict.keys())
    for country in spawn_config:
        foreign_countries = set()
        ratios = 0
        for ratio in spawn_config[country]["international"]:
            foreign_country = ratio[0]
            ratios += ratio[1]
            if foreign_country in foreign_countries:
                print(f"Country {foreign_country} appears more than once in spawn configuration for {country}")
                return False
            elif foreign_country not in supported_countries:
                print(f"Unsupported country {foreign_country} in spawn configuration for {country}")
                return False
            foreign_countries.add(foreign_country)
        ratio_sum = round(ratios + spawn_config[country]["national"] + spawn_config[country]["random"], 5)
        if ratio_sum != 1.0:
            print(f"Ratios in spawn configuration for {country} sum to {ratio_sum}")
            return False
    return True
