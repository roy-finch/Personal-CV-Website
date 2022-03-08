def css():
    string = ""
    names = ["m", "m-t", "m-l", "m-b", "m-r", "p", "p-t", "p-l", "p-b", "p-r", "x-scroll", "y-scroll", "b-style", "b", "w", "h", "left", "right", "top", "bottom", "w-per", "w-vw", "h-per", "h-vh", "col"]
    functions = ["margin", "margin-top", "margin-left", "margin-bottom", "margin-right", "padding", "padding-top", "padding-left", "padding-bottom", "padding-right", "overflow-x", "overflow-y", "border-style", "border-width", "width", "height", "left", "right", "top", "bottom", "width", "width", "height", "height", "width"]
    measurement = ["px", "px", "px", "px", "px", "px", "px", "px", "px", "px", "scroll", "scroll", "border", "px", "px", "px", "px", "px", "px", "px", "%", "vw", "%", "vh", "%"]
    keywords = {"scroll":["scroll", "hidden", "auto", "visible"], "border": ["dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset", "none", "hidden"]}

    for x in range(0, len(names)):
        if measurement[x] in keywords:
            string += "\n /* Styles for "+functions[x]+" up to "+str(len(keywords[measurement[x]]))+" values. */\n"
            for y in range(0, len(keywords[measurement[x]])):
                string += "."+names[x]+"-"+keywords[measurement[x]][y]+" { \n\t"+functions[x]+": "+keywords[measurement[x]][y]+";\n}\n"
        elif functions[x] == "width" or functions[x] == "height":
            string += "\n /* Styles for "+functions[x]+" up to 250 values. */\n"
            for y in range(0, 251):
                if y == 0:
                   string += "."+names[x]+"-auto { \n\t"+functions[x]+": auto;\n}\n"
                elif measurement[x] == "px":
                    string += "."+names[x]+"-"+str(y)+" { \n\t"+functions[x]+": "+str(y)+measurement[x]+";\n}\n"
                elif (measurement[x] == "%" or measurement[x] == "vw" or measurement[x] == "vh") and y < 101:
                    string += "."+names[x]+"-"+str(y)+" { \n\t"+functions[x]+": "+str(y)+measurement[x]+";\n}\n"
        elif functions[x] == "left" or functions[x] == "right" or functions[x] == "top" or functions[x] == "bottom":
            string += "\n /* Styles for "+functions[x]+" up to 20 values. */\n"
            for y in range(0, 21):
                string += "."+names[x]+"-"+str(y-10)+" { \n\t"+functions[x]+": "+str(y-10)+measurement[x]+";\n}\n"
        else:
            string += "\n /* Styles for "+functions[x]+" up to 21 values. */\n"
            for y in range(0, 21):
                if y == 0:
                   string += "."+names[x]+"-auto { \n\t"+functions[x]+": auto;\n}\n"
                elif measurement[x] == "px":
                    string += "."+names[x]+"-"+str(y)+" { \n\t"+functions[x]+": "+str(y)+measurement[x]+";\n}\n"
    print(string)
