def remove_comments_and_spaces():
    import sys

    first_line = sys.stdin.readline().strip()
    _, n = first_line.split()
    n = int(n)
    
    result_lines = []
    
    for _ in range(n):
        line = sys.stdin.readline()  
        comment_index = line.find('#')
        if comment_index != -1:
            line = line[:comment_index]  
        line = line.rstrip()  
        result_lines.append(line)
    
    print("\n".join(result_lines))

remove_comments_and_spaces()
