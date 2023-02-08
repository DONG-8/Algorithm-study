def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    
    for st in s:
        if (st.upper() == "P"):
            p_count += 1
        elif (st.upper() == "Y"):
            y_count += 1
    return (p_count == y_count)