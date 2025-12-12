from linkedList import LinkedList


ll = LinkedList()

while True:
    print("\n1 append  2 prepend  3 insert  4 pop  5 delete  6 show  7 reverse  8 mid  9 from_end  10 has_cycle  11 exit")
    cmd = input("cmd: ")

    if cmd == "1":
        v = input("value: ")
        ll.append(v)
    elif cmd == "2":
        v = input("value: ")
        ll.prepend(v)
    elif cmd == "3":
        v = input("value: ")
        i = int(input("index: "))
        ll.insert(v, i)
    elif cmd == "4":
        i = input("index (or empty): ")
        ll.pop(None if i == "" else int(i))
    elif cmd == "5":
        v = input("value: ")
        ll.delete(v)
    elif cmd == "6":
        print(ll)
    elif cmd == "7":
        ll.reverse()
    elif cmd == "8":
        print(ll.mid())
    elif cmd == "9":
        n = int(input("n: "))
        print(ll.from_end(n))
    elif cmd == "10":
        print(ll.has_cycle())
    elif cmd == "11":
        break
    else:
        print("invalid")