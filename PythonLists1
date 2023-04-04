if __name__ == '__main__':
    N = int(input())
    i=0
    arr = []
    while i < N:
        input_string = input()
        input_parts = []
        input_parts = input_string.split(" ")
        #print(input_parts)
        
        if input_parts[0] == "append":
            arr.append(int(input_parts[1]))
        elif input_parts[0] == "insert":
            arr.insert(int(input_parts[1]), int(input_parts[2]))
        elif input_parts[0] == "remove":
            arr.remove(int(input_parts[1]))
        elif input_parts[0] == "sort":
            arr.sort()
        elif input_parts[0] == "pop":
            arr.pop()
        elif input_parts[0] == "reverse":
            arr.reverse()
        elif input_parts[0] == "print":
            print(arr)
            
        i = i+1







%##

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        command, *n = input().split()
        n = list(map(int,n))
        if command == 'print':
            print(arr)
        else:
            getattr(arr,command)(*n)
