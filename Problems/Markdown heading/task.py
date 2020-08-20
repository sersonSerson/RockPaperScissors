def heading(text, level=1):
    level = max(min(level, 6), 1)
    return '#' * level + ' ' + text


# print(heading("A") == '# A')      # Returns "# A"
# print(heading("A", 3) == '### A')   # Returns "### A"
# print(heading("A", 1) == '# A')   # Returns "# A"
# print(heading("A", 0) == "# A")   # Returns "# A"
# print(heading("A", 10) == "###### A")  # Returns "###### A"
