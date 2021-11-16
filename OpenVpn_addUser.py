#Leer el template
def readTemplate(template):
    with open(template, 'r') as f:
        template = f.read()
    return template

# Change the cert and key
def setCert(template, cert, key):
    flag = False
    template = readTemplate(template)
    # print(template)
    for row in template.split("\n"):
        # Search for the cert and replace it
        # print(row)
        if "<cert>" in row:
            flag = True
        if flag:
            print(row)
            if "</cert>" in row:
                flag = False
            else:
                row = row.replace("<cert>", cert)
    return template

def getCert(cert):
    flag = False
    data = ""
    with open(cert, 'r') as f:
        cert = f.read()
        for row in cert.split("\n"):
            if "BEGIN CERTIFICATE" in row:
                flag = True
            if flag:
                # print(row)
                data+=row+"\n"
            if "END CERTIFICATE" in row:
                flag = False
    return data
def getKey(key):
    flag = False
    data = ""
    with open(key, 'r') as f:
        file = f.read()
        for row in file.split("\n"):
            if "BEGIN PRIVATE KEY" in row:
                flag = True
            if flag:
                data+=row+"\n"
            if "END PRIVATE KEY" in row:
                flag = False
    return data

def main():
    # template = readTemplate("template.ovpn")
    cert = getCert("cert.crt")
    key = getKey("key.key")
    setCert("template.ovpn", cert, key)



if __name__ == '__main__':
    print("Inicio")
    main()