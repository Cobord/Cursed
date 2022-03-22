import subprocess

def myf():
    import kata4

if __name__ == '__main__':
    p1 = subprocess.run(['ls'],shell=False,text=True,check=True,stdout=subprocess.PIPE)

    p2=p1.stdout.replace("kata","example").split("\n")
    p2 = p2[0:len(p2)-1]

    # write print statements within this file
    # either within same indentation level or not
    p3 = subprocess.run(['rm','-rf','__pycache__'],shell=False,check=True)
    with_spaces = False
    maybe_spaces = "    " if with_spaces else ""
    with open(__file__,'a') as f:
        [f.writelines(f"\n{maybe_spaces}print(\"{x}\")") for x in p2]
    take_effect_immediately = True
    if take_effect_immediately:
        myf()