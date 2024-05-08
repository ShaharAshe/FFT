from FFT import FFT


if __name__ == "__main__":
    FFT_vector:list = [1,16,2,15,3,14,4,13,5,12,6,11,7,10,8,9]
    Z:int = 17
    unit_root:int = 6

    "if you dont know the unit root, set it to 0"
    # unit_root:int = 0
    
    print(FFT(FFT_vector, Z, unit_root))