import re

def perform_regex_matching(test_string, regex_pattern):
    try:
        regex = re.compile(regex_pattern)
        matches = regex.findall(test_string)
        return matches if matches else None
    except re.error as e:
        return f"Error in the regular expression: {e}"
