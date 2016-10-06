    
    x_beg= x-1
    x_end= x+2
    y_beg= y-1
    y_end= y+2
    if x_beg< 0:
        x_beg=0
    if x_end> width-1:
        x_end= width
    if y_beg<0:
        y_beg= 0
    if y_end> height-1:
        y_end= height
        

    l= [(i,j) for i in range(x_beg, x_end) for j in range (y_beg, y_end)]
    l.remove((x,y))
    return l    
