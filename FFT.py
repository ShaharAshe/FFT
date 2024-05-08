import numpy as np


def FFT(FFT_vector:list, Z:int, unit_root:int, level:int=1, root:list=[], inverse:bool=False):
    if len(FFT_vector) == 1:
        return [int(FFT_vector[0])%Z]
    
    final_result:list = []
    if level == 1:
        temp_unit:list = [1]
        dup:int = 1
        if inverse:
            dup = -1
        for i in range(len(FFT_vector)-1):
            temp_unit += [(temp_unit[-1]*unit_root*dup)%Z]
        final_result.append(temp_unit[:])
        final_result.append([int(c) for c in FFT_vector])
    else:
        final_result = [root, FFT_vector]
        
    temp_1:list = FFT(final_result[1][::2], Z, unit_root, level*2, final_result[0][::2])
    temp_2:list = FFT(final_result[1][1::2], Z, unit_root, level*2, final_result[0][::2])

    return [((temp_1[i%(len(FFT_vector)//2)] + ((temp_2[i%(len(FFT_vector)//2)] * final_result[0][i])))%Z) for i in range(len(FFT_vector))]


def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


if __name__ == "__main__":
    FFT_vector:list = [1,16,2,15,3,14,4,13,5,12,6,11,7,10,8,9]
    Z:int = 17
    unit_root:int = 6

    "if you dont know the unit root, set it to 0"
    # unit_root:int = 0

    if not unit_root:
        for i in range(2, Z):
            if gcd(i, Z) == 1:
                unit_root = i
                break

    if unit_root == 0:
        print("No unit root found")
    else:
        print(f"Unit root: {unit_root}")
        print(FFT(FFT_vector, Z, unit_root))
