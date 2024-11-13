def fibonachi (n):
    if n<=1:
        print("Ga bisa kocakkkk")
    elif n==1 or n==2:
        return 1
    else:
        return(fibonachi(n-1))+(fibonachi(n-1))
    
a = int(input("Masukkan angka: "))
nilai_fibonachi = fibonachi(a)
print("Nilai dari", a, "adalah", nilai_fibonachiP)
