import sys
class tree():
#创建字典树

    def __init__(self):
        self.nextword = {}       #相当于指针，指向树节点的下一层节点
        self.failed = None     #失败指针，当节点匹配失败后可直接跳转到失败指针所指向的节点
        self.isEnd = False  #标记，用来判断是否是一个标签的结尾
        self.shieled_word = ""       #用来储存标签

class Ac_automation():
#创建根节点
    def __init__(self):
        self.base = tree()

    def add_word(self, shieled_word):
        temp_base = self.base
        for char in shieled_word:
            if char not in temp_base.nextword:
                temp_base.nextword[char] = tree()
            temp_base = temp_base.nextword[char]
        temp_base.isEnd = True
        temp_base.shieled_word = shieled_word
#构建fail指针
    def made_failed(self):
        temp_word = []
        temp_word.append(self.base)
        while len(temp_word) != 0:
            temp = temp_word.pop(0)
            current = None
            for key,value in temp.nextword.item():
            #该节点为根节点
                if temp == self.base:
                    temp.nextword[key].failed = self.base
                else:
                    current = temp.failed
                    while current is not None:
                        if crux in current.next:
                            temp.nextword[crux].failed = current.failed
                            break
                        current = current.failed
                    if current is None:
                        temp.nextword[key].failed = self.base
                temp_word.append(temp.nextword[crux])
#用于查找匹配

    def search(self, content):
        current = self.base
        output = []
        current_position = 0
#进行遍历
        while current_position < len(content):
            current_word = content[current_position]
        #节点匹配失败并且节点非根节点
            while current_word in current.nextword == False and current != self.base:
                current = current.failed
            if current_word in current.nextword:
                current = current.nextword[current_word]
            else:
                current = self.base
        #屏蔽词匹配已经结束
            if current.isEnd:
                output.append(current.shieled_word)
    #文档中所要遍历的向后一位
            current_position =current_position+1
#对output判断是否为空。不为空就正常返回；否则返回1
        if(len(output)!=0):
            return output
        else:
            return 1
def try_file_path(file_path):
    try:
        f = open(file_path, encoding='utf-8')
    except Exception as msg:
        print(msg)
        exit(0)
    else:
        f.close()
#主函数：用于读取文件以及写入文件
if __name__ == "__main__":
#ac用于添加屏蔽词
    A_c = Ac_automation()
    A_c.add_word("falungong")
    A_c.add_word("邪教")
    A_c.add_word("法轮功")
    A_c.add_word("fuck")
    A_c.add_word("邪_教")
    A_c.add_word("邪  教")
    A_c.add_word("法轮_功")
    A_c.add_word("fa_lun_gong")
    A_c.add_word("fa伦功")
#创建list1用于存放文档中一行的内容，list2用于暂时存放所要输出的结果
    list1 = []
    list2 = []
    list3 = []
    path_words = str(sys.argv[1])
    path_org = str(sys.argv[2])
    path_ans = str(sys.argv[3])
    f2 = open(path_ans, "w",encoding="utf-8")
    with open(path_org, 'r', encoding='utf-8') as f1:
        list1 = f1.readlines()
        lena = len(list1)
        if(lena==0):
                f2.write("Error\n")
        else:
            f2.write(f"Total:{lena}\n")
            f2.write('\n')
            for index in range(len(list1)):
                #用返回值是否为1来判断返回值是否为空，避免了python返回值为空则输出None的问题
                if(A_c.search(list1[index])!=1):
                    list3=A_c.search(list1[index])
                    f2.writelines('Line')
                    f2.write(f"{index}")
                    f2.write(':')
                    f2.write('<')
                    f2.writelines(list3)
                    f2.write('>')
                    f2.write(' ')
                    f2.writelines(list3)
                    f2.write('\n')
                    f2.write('\n')
    f2.close()
