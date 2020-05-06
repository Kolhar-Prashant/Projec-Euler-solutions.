import csv

def generate_index_table():
    cap_lett = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    ascii_cap = 1

    for let in cap_lett:
        index_val_Dict[let] = ascii_cap
        ascii_cap += 1

def calc_index_sum(S):
    lexi_val = 0

    for alpha in S:
        lexi_val += index_val_Dict[alpha]
    return lexi_val

def gen_tri_num_list():
    i = 1
    a = 2
    t_num.append(i)
    for e in range(1, 30):
        x = i + a
        t_num.append(x)
        a += 1
        i = x

if __name__ == "__main__":

    index_val_Dict={}
    t_num = []
    Word_list = []

    generate_index_table()
    gen_tri_num_list()

    total_cnt=0
    with open('D:\p042_words.txt','r') as file_reader:
        file = csv.reader(file_reader)
        Word_list=list(file)

    alpha_val=0
    for e in Word_list:
        for a in e:
            alpha_val = calc_index_sum(a)
            if alpha_val in t_num:
                total_cnt+=1
    print(total_cnt)
