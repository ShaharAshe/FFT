import numpy as np

def FFT(FFT_vector, Z, unit_root, level=1, root=[]):
    # pass
    if len(FFT_vector) == 1:
        return [int(FFT_vector[0])%Z]
    
    final_result = [[(np.power(unit_root, i*level))%Z for i in range(len(FFT_vector))], [int(v) for v in FFT_vector]]
    temp_1 = FFT(final_result[1][::2], Z, unit_root, level+1, final_result[0][::2])
    temp_2 = FFT(final_result[1][1::2], Z, unit_root, level+1, final_result[0][1::2])
    
    # return [((temp_1[i] + (temp_2[i] * final_result[0][i]))%Z) for i in range(len(FFT_vector))]
    print(f'{level = } - {final_result = }\n{temp_1 = }\n{temp_2 = }')



if __name__ == "__main__":
    # FFT_vector = ""
    FFT_vector = "12345600"
    while len(FFT_vector) % 2 != 0 or (not len(FFT_vector)):
        FFT_vector = input("Please enter a valid vector:\n")

    # Z = 17
    Z = 17
    if Z == 0:
        Z = int(input("Please enter a valid Z:\n"))

    # unit_root = 0
    unit_root = 2
    if unit_root == 0:
        unit_root = int(input("Please enter a valid unit root:\n"))

    FFT(FFT_vector, Z, unit_root)
    print(  np.fft.fft(FFT_vector))
