def pos_eq_vals(ls, ls2):
    out = []

    for j, i in enumerate(ls):
        if ls[j] == ls2[j]:
            out.append(j)
    return out
