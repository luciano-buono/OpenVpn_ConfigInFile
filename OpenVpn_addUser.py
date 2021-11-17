from argparse import ArgumentParser

#1) Pide input file y genera el outfile name
parser = ArgumentParser()
parser.add_argument('-f','--file', type=str, required=True)
user = vars(parser.parse_args())["file"]


#Leer el template
def readTemplate(template):
    with open(template, 'r') as f:
        template = f.read()
    return template

# Change the cert and key
def setCert(template, cert, key):
    template = readTemplate(template)
    filename = f"C:/Users/Usuario/Desktop/{user}.ovpn"
    with open(filename, 'w') as f:
        for row in template.split("\n"):
            f.writelines(row+"\n")
            # Search for the cert and replace it
            if "<cert>" in row:
                f.writelines(cert)
            if "<key>" in row:
                f.writelines(key)
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
    print("Creating the .ovpn file of",user)
    cert = getCert(f"{user}.crt")
    key = getKey(f"{user}.key")
    setCert("template.ovpn", cert, key)



if __name__ == '__main__':
    print("Inicio")
    main()