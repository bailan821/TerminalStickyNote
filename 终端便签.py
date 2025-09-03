# -*- coding: utf-8 -*-
c = []               # 原来就有的列表，用来存便签

try:
    with open("终端便签储存数据.txt", "r", encoding="utf-8") as b:
        for i in b:
            i = i.strip()
            if i:
                c.append(i)
except FileNotFoundError:
    with open("终端便签储存数据.txt", "w", encoding="utf-8") as b:
        pass

while True:
    print("========终端便签========")
    e=input("请选择模式\n1.查看便签 2.更改便签\n3.应用信息:")          #用户模式选择
    if e=="1":
        print("========查看便签========")
        f=input("请选择查看便签方式\n1.查看所有便签 2.按关键词/日期搜索便签:")          #用户选择查看方式
        if f == "1":
           print("========查看所有便签========")
           c.clear()                                                      # 清空旧内容
           try:
               with open("终端便签储存数据.txt", "r", encoding="utf-8") as b:
                   for i in b:
                       i = i.strip()
                       if i:
                           c.append(i)
           except FileNotFoundError:
              pass                                                  # 文件不存在就跳过，c 保持空
           if c:
               for i in range(len(c)):
                   print(f"{i+1}. {c[i]}")
               input("请按回车键继续:")
           else:
               print("暂时没有便签，你可以新建一个")
               input("请按回车键继续:")

        elif f == "2":
            print("========按关键词/日期搜索便签========")
            c.clear()                                                             # 清空旧内容
            try:
                with open("终端便签储存数据.txt", "r", encoding="utf-8") as b:
                    for i in b:
                        i = i.strip()
                        if i:
                            c.append(i)
            except FileNotFoundError:
                pass  # 文件不存在就跳过，c 保持空
            if c:
                k = input("请输入关键词/日期:")
                q = False
                for i in range(len(c)):
                    if k in c[i]:
                        print(f"{i+1}. {c[i]}")
                        q = True
                if not q:
                    print("暂无此关键词/日期便签")
                input("请按回车键继续:")
            else:
                print("暂时没有便签，你可以新建一个")
                input("请按回车键继续:")

    elif e=="2":
        print("========更改便签========")
        l=input("更改便签模式选择\n1.写入便签 2.删除便签:")
        if l=="1":
            print("========写入便签========")
            print("提示:")
            print("当程序没有新建终端便签储存数据.txt时,您可以手动新建")
            print("从外部直接复制会出现问题,建议直接复制在终端便签储存数据.txt上并保存")
            m=input("请输入便签日期(格式为:2025-08-28):")
            while "-" not in m:
                m=input("格式错误,请输入正确格式(格式为:2025-08-28):")
            n=input("请输入便签内容:")
            o=f"{m} {n}"                     #变量o为日期与内容
            with open("终端便签储存数据.txt","a",encoding="utf-8") as b:         #在a.txt的文件里追加一条便签,编码为utf-8,并更名为b
                b.write(o+"\n")              #把变量o分段
            c.append(o)
            print(f"\n写入成功!\n新便签:{o}")
            print("当前全部便签为:")
            for i in range(len(c)):
                print(f"{i+1}. {c[i]}")
            input("请按回车键继续:")
        
        elif l=="2":
            print("========删除便签========")
            if not c:
                print("暂时没有便签,你可以新建一个")
                input("请按回车键继续:")
            else:
                print("当前全部便签为:")
                for i in range(len(c)):
                    print(f"{i+1}. {c[i]}")
                p=input("请输入要删除的便签序号:")           #变量p为用户输入的要删除的便签序号
                p=int(p)-1
                if 0<=p<len(c):                        #让用户输入的便签序号大于等于0同时小于len(c)
                    del c[p]                        #把用户输入的便签序号从列表c中删除
                    with open("终端便签储存数据.txt","w",encoding="utf-8") as b:         #w为写入覆盖
                        for i in range(len(c)):
                            b.write(c[i]+"\n")
                    print("操作成功!")
                    print("当前全部便签为:")
                    for i in range(len(c)):
                        print(f"{i+1}. {c[i]}")
                    input("请按回车键继续:")
                else:
                    print("请输入正确的便签序号")
                    input("请按回车键继续:")
        
        else:
            print("此编号暂无功能")
            input("请按回车键继续:")
    
    elif e=="3":
        print("========应用信息========")
        print("1. 应用名称:终端便签\n2. 应用版本:v1.0\n3. 开发者:B站账号:@云川星纪\n联系邮箱:3296282338@qq.com")
        input("请按回车键继续:")
    
    else:
        print("此编号暂无功能")
        input("请按回车键继续:")
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
