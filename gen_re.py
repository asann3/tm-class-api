def gen_re(subjects):
    pt = ""
    for subject in subjects:
        replaced = subject.replace('(','\\(').replace(')','\\)')
        pt += replaced + "|"

    pt = pt.rstrip("|")
    pt = ".*({0})　*→　*({0})".format(pt)

    return pt