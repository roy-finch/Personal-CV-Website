def css(nicknames=[]):
    val = {"overflow-x":["scroll", "hidden", "auto", "visible", "initial", "inherit"],
           "overflow-y":["scroll", "hidden", "auto", "visible", "initial", "inherit"],
                "border-style": ["dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset", "none", "hidden"],
                "display": ["inline", "block", "contents", "flex", "grid", "inline-block", "inline-flex", "inline-grid",
                            "inline-table", "list-item", "run-in", "run-in", "table", "table-caption", "table-column-group",
                            "table-header-group", "table-footer-group", "table-row-group", "table-cell", "table-column", "table-row",
                            "none", "initial", "inherit"],
                "position": ["static", "relative", "fixed", "absolute", "sticky"],
                "float": ["left", "right", "up", "down"],
               "text-align": ["left", "right", "center", "justify", "initial", "inhert"],
               "vertical-align": ["baseline", "length", "sub", "super", "top", "text-top", "middle", "bottom",
                                  "text-bottom", "initial", "inherit"],
               "visibility": ["visible", "hidden", "collapse", "initial", "inherit"],
               "text-decoration": ["overline", "line-through", "none", "underline", "underline overline"],
               "list-style-type": ["none", "circle", "square", "upper-roman", "lower-alpha", "disc", "armenian", "circle", "decimal", "georgian", "hebrew"],
               "list-style-position": ["outside", "inside"],
               "font-style": ["normal", "italic", "oblique", "initial", "inherit"],
               "font-stretch": ["ultra-condensed", "extra-condensed", "condensed", "semi-condensed", "normal", "semi-expanded", "expanded", "extra-expanded",
                                "ultra-expanded", "initial", "inherit"],
               "font-family": ["Arial", "Helvetica", "sans-serif", "Times", "serif"],
               "border-width": ["medium", "thin", "thick", "initial", "inherit"],
               "border-top-width": ["medium", "thin", "thick", "initial", "inherit"],
               "border-bottom-width": ["medium", "thin", "thick", "initial", "inherit"],
               "border-right-width": ["medium", "thin", "thick", "initial", "inherit"],
               "border-left-width": ["medium", "thin", "thick", "initial", "inherit"]}
                
    functions = ["width", "height", "margin", "margin-left", "margin-right", "margin-top", "border", "top", "bottom", "min-width", "min-height" , "max-width",
                 "max-height", "list-style-type", "list-style-position", "line-height", "letter-spacing", "font-style", "font-stretch", "font-size", "font-family",
                 "right", "left", "border-style", "border-color", "margin-bottom", "padding-top", "padding-bottom", "padding-left", "padding-right", "padding",
                 "overflow-x", "overflow-y", "background-color", "display", "position", "float", "border-radius", "color", "border-left", "border-width",
                 "border-right", "border-top", "border-bottom", "text-align", "vertical-align", "visibility", "text-indent", "text-decoration", "border-top-radius",
                 "border-bottom-radius", "border-left-radius", "border-right-radius", "border-top-width", "border-bottom-width", "border-left-width",
                 "border-right-width", "border-spacing"]

    functions.sort()
    
    out = ""
    ipt = input("Would you like to through the values to decide nicknames?")
    if ipt.lower() in "yes":
        for x in range(0, len(functions)):
            if (x == 0):
                temp = input("What is the nickname you'd like for "+functions[0]+"?")
            else:
                temp = input(functions[x]+"?")
            if temp == "":
                temp = functions[0]
            nicknames.append(temp)
    elif nicknames == []:
        nicknames = functions
    print(nicknames)

    out += "/* Thank you for creating your CSS generic style using this program, hopefully this is helpful for your programming adventures.\n CSS V0.01\n"+str(val)+"\n"+str(functions)+"\n"+str(nicknames)+"*/\n"
    print("Initialising")
    for x in range(0, len(functions)):
        print("Generating:"+str(round(100/len(functions)*x)))
        out += "/*-----------------------------------This section is for "+functions[x]+" function.-----------------------------------*/\n"
        if (functions[x] in val):
            for y in range(0, len(val[functions[x]])-1):
                out += nicknames[x]+"-"+val[functions[x]][y]+" {\n\t"+functions[x]+": "+val[functions[x]][y]+";\n}\n"
        elif ("width" in functions[x] or "height" in functions[x]):
            out += nicknames[x]+"-none {\n\t"+functions[x]+": auto;\n}\n"
            for z in range(0, 2):
                for y in range(1, 1000):
                    if z == 0:
                        out += nicknames[x]+"-"+str(y)+"-px {\n\t"+functions[x]+": "+str(y)+"px;\n}\n"
                    elif z == 1 and y < 100:
                        out += nicknames[x]+"-"+str(y)+"-per {\n\t"+functions[x]+": "+str(y)+"%;\n}\n"
                    elif z == 2 and "width" in functions[x] and y < 100:
                        out += nicknames[x]+"-"+str(y)+"-vw {\n\t"+functions[x]+": "+str(y)+"vw;\n}\n"
                    elif z == 2 and "height" in functions[x] and y < 100:
                        out += nicknames[x]+"-"+str(y)+"-vh {\n\t"+functions[x]+": "+str(y)+"vh;\n}\n"
        elif "color" in functions[x]:
            r = 0
            g = 0
            b = 0
            for a in range(0, 52*52*52+1):
                out += nicknames[x]+"-r"+str(r)+"g"+str(g)+"b"+str(b)+" {\n\t"+functions[x]+": rgb("+str(r)+", "+str(g)+", "+str(b)+");\n}\n"
                b += 5
                if b == 260:
                    b = 0
                    g += 5
                if g == 260:
                    g = 0
                    r += 5
        else:
            out += nicknames[x]+"-none {\n\t"+functions[x]+": 0px;\n}\n"
            for y in range(1, 60):
                out += nicknames[x]+"-"+str(y)+"-px {\n\t"+functions[x]+": "+str(y)+"px;\n}\n"
        out += "/*--------------------------------------------------------------------------------------------------------------------*/\n\n"
    print("Generated")
    print("Writing to file")
    with open('css.css', 'w') as f:
        f.write(out)

def decant():
    l = []
    functions = ["width", "height", "margin", "margin-left", "margin-right", "margin-top", "border", "top", "bottom", "min-width", "min-height" , "max-width",
                 "max-height", "list-style-type", "list-style-position", "line-height", "letter-spacing", "font-style", "font-stretch", "font-size", "font-family",
                 "right", "left", "border-style", "border-color", "margin-bottom", "padding-top", "padding-bottom", "padding-left", "padding-right", "padding"
                 "overflow-x", "overflow-y", "background-color", "display", "position", "float", "border-radius", "color", "border-left", "border-width",
                 "border-right", "border-top", "border-bottom", "text-align", "vertical-align", "visibility", "text-indent", "text-decoration", "border-top-radius",
                 "border-bottom-radius", "border-left-radius", "border-right-radius", "border-top-width", "border-bottom-width", "border-left-width",
                 "border-right-width", "border-spacing"]
    for x in range(0, len(functions)):
        if functions[x].find("-") != -1:
            temp += functions[x][0:functions[x].find("-")]
            temp += functions[x][functions[x].find("-")+1]
        else:
            temp = functions[x]
        l.append(temp)
        temp = ""
    print(l)
