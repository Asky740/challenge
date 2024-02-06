def convert_ip():
    #otázka
    adress_type = input("Zadejte typ adresy (decimální/binární): ")

    #input
    ip_address = input("Zadejte IP adresu: ")

    #převod
    if adress_type.lower() == "decimální":
        #decimální-binární
        binary_ip = '.'.join(format(int(x), '08b') for x in ip_address.split('.'))
        print("Binární IP adresa: ", binary_ip)
    elif adress_type.lower() == "binární":
        #binární-decimální
        decimal_ip = '.'.join(str(int(x, 2)) for x in ip_address.split('.'))
        print("Decimální IP adresa: ", decimal_ip)
    else:
        print("Máš to špatně.")

    #třída
    first_octet = int(ip_address.split('.')[0])
    if 1 <= first_octet <= 126:
        print("Třída A")
    elif 128 <= first_octet <= 191:
        print("Třída B")
    elif 192 <= first_octet <= 223:
        print("Třída C")
    elif 224 <= first_octet <= 239:
        print("Třída D")
    elif 240 <= first_octet <= 255:
        print("Třída E")
    else:
        print("Máš to špatně.")

convert_ip()
