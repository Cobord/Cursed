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
    with_spaces = True
    maybe_spaces = "    " if with_spaces else ""
    with open(__file__,'a') as f:
        [f.writelines(f"\n{maybe_spaces}print(\"{x}\")") for x in p2]
    # immediately also execute the newly added print statements if they are not in the same indentation level
    # if they are at the same level of indentation (with_spaces is True), then it is within this name == '__main__' condition
    #   so does not get run when the import in myf() happens
    # if they are not at the same level of indentation (with_spaces is False), then it is outside the __main__ condition
    #   so does get run when the import in myf() happens
    take_effect_immediately = True
    if take_effect_immediately:
        myf()