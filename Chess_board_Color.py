def chess_board_cell_color(cell1, cell2):
    odd_letters =['a','c','e','g']
    even_letters=['b','d','f','h']
    odd_nums=['1','3','5','7']
    even_nums=['2','4','6','8']
    l1=[]
    l2=[]
    for ch in cell1:
        l1.append(ch)

    for ch in cell2:
        l2.append(ch)

    if l1[0].lower() in odd_letters and l2[0].lower() in odd_letters and l1[1] in odd_nums and l2[1] in odd_nums:
        return True
    elif l1[0].lower() in even_letters and l2[0].lower() in even_letters and l1[1] in even_nums and l2[1] in even_nums:
        return True
    elif l1[0].lower() in odd_letters and l2[0].lower() in even_letters and l1[1] in even_nums and l2[1] in odd_nums:
        return True
    elif l1[0].lower() in even_letters and l2[0].lower() in odd_letters and l1[1] in odd_nums and l2[1] in even_nums:
        return True
    elif l1[0].lower() in odd_letters and l2[0].lower() in odd_letters and l1[1] in even_nums and l2[1] in even_nums:
        return True
    elif l1[0].lower() in even_letters and l2[0].lower() in even_letters and l1[1] in odd_nums and l2[1] in odd_nums:
        return True
    elif l1[0].lower() in odd_letters and l2[0].lower() in even_letters and l1[1] in odd_nums and l2[1] in even_nums:
        return True
    elif l1[0].lower() in even_letters and l2[0].lower() in odd_letters and l1[1] in even_nums and l2[1] in odd_nums:
        return True
    else:
        return False