import sys
import matplotlib.pyplot as plt

if (len(sys.argv) > 1):
    word_list = {}
    new_word_list = {}
    frequency_list = {}
    with open(sys.argv[1], "r") as fin:
        for line in fin:
            line_filtered = " ".join( line.lower().replace("\n", " ").replace("\t", " ").replace("{", " ").replace("}", " ").replace("<", " ").replace(">", " ").replace("(", " ").replace(")", " ").replace("[", " ").replace("]", " ").replace("=", " ").replace("?", " ").replace("!", " ").replace("$", " ").replace("%", " ").replace("&", " ").replace("/", " ").replace("\\", " ").replace("#", " ").replace("_", " ").replace(".", " ").replace(",", " ").replace("+", " ").replace("-", " ").replace("*", " ").replace(":", " ").replace(";", " ").replace("@", " ").replace("\"", " ").replace("'", " ").replace("|", " ").replace("`", " ").replace("0x", " ").replace("0", " ").replace("1", " ").replace("2", " ").replace("3", " ").replace("4", " ").replace("5", " ").replace("6", " ").replace("7", " ").replace("8", " ").replace("9", " ").split() )
            if (len(line_filtered) > 0):
                line_list = line_filtered.split(" ")
                for word in line_list:
                    if (word in word_list): word_list[word] += 1
                    else: word_list[word] = 1
    for key, value in sorted(word_list.items(), reverse=True):
        if (value in frequency_list): frequency_list[value] += ", "+key
        else: frequency_list[value] = key
    # output = open(sys.argv[1].split(".")[0], 'w')
    for key, value in sorted(frequency_list.items(), reverse=True):
        new_word_list[key] = value
        # output.write(str(key)+"\t"+value+"\n") # print(str(key)+" times:\t[ "+value+" ]\n") # inv_map = {v: k for k, v in word_list.items()}
    # print(list(new_word_list.keys()))
    plt.plot(list(new_word_list.keys()))
    plt.savefig(sys.argv[1].split(".")[0]+".png")
