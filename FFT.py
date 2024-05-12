import numpy as np

def FFT(FFT_vector:list, Z:int, unit_root:int=0, inverse:bool=False):
    """
    Performs the Fast Fourier Transform (FFT) or its inverse on a given vector modulo Z.

    Args:
        FFT_vector (list): The input vector for FFT.
        Z (int): Modulus for arithmetic operations.
        unit_root (int, optional): The primitive root of unity modulo Z. Defaults to 0.
        inverse (bool, optional): If True, computes the inverse FFT. Defaults to False.

    Returns:
        list: The FFT result or its inverse.
    """
    def gcd(num_1:int, num_2:int)->int:
        """
        Computes the greatest common divisor (GCD) of two numbers using Euclid's algorithm.

        Args:
            num_1 (int): First integer.
            num_2 (int): Second integer.

        Returns:
            int: The greatest common divisor of num_1 and num_2.
        """
        if num_1 == 0:
            return 0
        return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)
    
    def FFT(FFT_vector:list, Z:int, unit_root:int, level:int=1, root:list=[], dup:int=1):
        """
        Recursive function to perform FFT.

        Args:
            FFT_vector (list): The input vector for FFT.
            Z (int): Modulus for arithmetic operations.
            unit_root (int): The primitive root of unity modulo Z.
            level (int, optional): Current recursion level. Defaults to 1.
            root (list, optional): Current primitive root of unity values. Defaults to [].
            dup (int, optional): Duplication factor for inverse FFT. Defaults to 1.

        Returns:
            list: The FFT result or its inverse.
        """
        if len(FFT_vector) == 1:
            return [int(FFT_vector[0])%Z]
        
        final_result:list = []
        if level == 1:
            temp_unit:list = [1]
            for j in range(len(FFT_vector)-1):
                temp_unit += [(temp_unit[-1]*unit_root*dup)%Z]
            final_result.append(temp_unit[:])
            final_result.append([int(c) for c in FFT_vector])
        else:
            final_result = [root, FFT_vector]
            
        temp_1:list = FFT(final_result[1][::2], Z, unit_root, level*2, final_result[0][::2])
        temp_2:list = FFT(final_result[1][1::2], Z, unit_root, level*2, final_result[0][::2])

        return [((temp_1[i%(len(FFT_vector)//2)] + ((temp_2[i%(len(FFT_vector)//2)] * final_result[0][i])))%Z) for i in range(len(FFT_vector))]
    
    dup:int = 1
    if inverse:
        dup = -1

    if not unit_root:
        for i in range(2, Z):
            if gcd(i, Z) == 1:
                temp_unit:list = [1]
                for j in range(len(FFT_vector)):
                    temp_unit += [(temp_unit[-1]*i*dup)%Z]
                if temp_unit[-1] == 1 and len(set(temp_unit)) == len(FFT_vector):
                    unit_root = i
                    break
        if not unit_root:
            return("No unit root found")
        else:
            print(f"Unit root: {unit_root}")
    
    return FFT(FFT_vector=FFT_vector, Z=Z, unit_root=unit_root, dup=dup)
    

if __name__ == "__main__":
    pass
