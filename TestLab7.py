from ED import edit_distance

def main():
    str1 = "stacked"
    str2 = "tacky"
    str3 = ""
    str4 = "azsxdcfv"
    str5= "zaxscdvf"
    print(edit_distance(str1, str2, len(str1), len(str2)))
    print(edit_distance(str3, str2, len(str3), len(str2)))
    print(edit_distance(str4, str5, len(str4), len(str5)))

if __name__ == "__main__":
    main()