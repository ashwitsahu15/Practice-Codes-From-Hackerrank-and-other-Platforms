t=int(input())
period=[]
arr=[1, 2, 3, 6, 7, 14, 15, 30, 31, 62, 63, 126, 127, 254, 255, 510, 511, 1022, 1023, 2046, 2047, 4094, 4095, 8190, 8191, 16382, 16383, 32766, 32767, 65534, 65535, 131070, 131071, 262142, 262143, 524286, 524287, 1048574, 1048575, 2097150, 2097151, 4194302, 4194303, 8388606, 8388607, 16777214, 16777215, 33554430, 33554431, 67108862, 67108863, 134217726, 134217727, 268435454, 268435455, 536870910, 536870911, 1073741822, 1073741823, 2147483646, 2147483647]
for _ in range(t) :
    n=int(input())
    print(arr[n])