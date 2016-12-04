def pretty_print(text, max_line_length):
    """For a string and a number, return a pretty-printed version
       of the string: replace some spaces with linebreaks such 
       that the total amount of wasted space at the ends of lines
       is minimized.
    """
    words = text.split()
    lines = []
    s = ''

    for w in words:
        if len(s) + len(w) >= max_line_length:
            lines.append(s)
            s = ''

        s += (" " + w if len(s) > 0 else w)
    lines.append(s)

    return "\n".join(lines)
