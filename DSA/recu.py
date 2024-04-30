# def main(t):
#     i =1
#     get_final = []
#     while i<=t:
#         get_input1 = 'Venky'
#         get_input2 = 'Iyer'
#         get_final.append(get_input1 + get_input2)
#         i+=1    

#     final_string = "\n".join(get_final)
#     return final_string

# if __name__ == '__main__':
#     print(main(3))

def main(h):
    print(type(h))
    if h>=195:
        return 'abnormal'
    elif h >=165 and h < 195:
        return 'taller'
    elif h >=150 and h < 165:
        return 'average'
    else:
        return 'dwarf'

if __name__ == '__main__':
    print(main(float(205.8)))