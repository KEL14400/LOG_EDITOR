def remover(line, list_to_delete):
    for word in list_to_delete:
        if word in line:
            return line.replace(word, '').rstrip()


def file_create(title):
    g = open("output_{}.txt".format(title), 'w')
    g.write("<p data-ke-size=\"size16\">&nbsp;</p>\n")
    g.write("<table style=\"border-collapse: collapse; width: 100%; height: 170px;\" border=\"1\" data-ke-align=\"alignLeft\" data-ke-style=\"style16\">\n")
    g.write("<tbody>\n")
    g.close()


def file_writer(line, last_name, names_colourcode):
    cur_name, cur_words = line.split(" :", 1)
    if cur_name not in names_colourcode:
        names_colourcode = char_input(cur_name, names_colourcode)

    if cur_name != last_name:
        last_name = cur_name
        return "<tr style=\"height: 17px;\">\n<td style=\"width: 14.6511%; height: 17px;\"><span style=\"color: {colour};\">{nam}</span></td>\n<td style=\"width: 85.3489%; height: 17px;\"><span style=\"color: {colour};\">{say}</span></td>\n</tr>".format(
            colour = names_colourcode[cur_name], nam = cur_name, say = cur_words[1:]), last_name, names_colourcode

    elif cur_name == last_name:
        return "<tr style=\"height: 17px;\">\n<td style=\"width: 14.6511%; height: 17px;\">&nbsp;</td><td style=\"width: 85.3489%; height: 17px;\"><span style=\"color: {colour};\">{say}</span></td>\n</tr>".format(
        colour = names_colourcode[cur_name], say = cur_words[1:]), last_name, names_colourcode


def inp_unbox(title, dels):
    f = open('{}.txt'.format(title), 'r')
    raw_lines = f.readlines()
    polish = []
    for i in range(len(raw_lines)):
        if raw_lines[i] != '\n':
            polish.append(remover(raw_lines[i], dels))
    f.close()
    return polish


def char_input(char, names_colourcode):
    code = input("{} : ".format(char))
    if len(code) == 6:
        names_colourcode[char] = "#{}".format(code)
    else:
        names_colourcode[char] = '#474f49'

    return names_colourcode


def main():
    print("\n")
    print("* * * * * * * * * *")
    print("Log Editor activated...")
    deletes = ['[Main] ', '[메인] ', '[メイン] ']
    print("\n")

    que1 = input("Choose a language option(E/K): ").lower()

    if que1 == 'k':
        filename = input("txt 파일 이름을 입력하세요 (.txt 제외): ")
    else:
        filename = input("Type in the name of txt file (without .txt): ")

    print("\n")

    lines = inp_unbox(filename, deletes)
    char_info = {"system": "#9e9e9e"}

    file_create(filename)

    h = open('output_{}.txt'.format(filename), 'a')
    last = 'fwjelfisdkjlf'

    if que1 == 'k':
        print("에디터가 주어진 txt 내의 모든 캐릭터들을 출력하고 컬러코드를 입력하라 할겁니다.")
        print("컬러코드를 입력할 때, 반드시 #를 제거한 숫자/영어 6자만 적어주세요.")
        print("컬러코드를 지정하고 싶지 않다면 엔터를 누르세요.")
        print("*메모: 색을 지정하지 않은 캐릭터의 텍스트는 #474f49 (회색) 으로 표시되며,")
        print("시스템 메세지는 #9e9e9e (옅은 회색) 으로 표시됩니다.")
        print("\n")

    else:
        print("Editor will now display all characters in given txt and ask for its colour code.")
        print("Make sure you only type in 6 digits excluding #.")
        print("If you do not wish to assign colour code, press enter.")
        print("*Note: any characters you didn't assign will have colour code #474f49 (grey),")
        print("and system message will have colour code #9e9e9e (light grey)")
        print("\n")

    for i in lines:
        inpus, last, char_info = file_writer(i, last, char_info)
        h.write('\n'+inpus)

    h.write('\n' + "</tbody>")
    h.write('\n' + "</table>")
    h.close()

    print("\n")
    print("Writing completed.")


def close():
    print("Exiting...")
    print("* * * * * * * * * *")
    print('\n')
    exit()

if __name__ == '__main__':
    main()

    close()