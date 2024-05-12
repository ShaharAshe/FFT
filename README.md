
---

# FFT Implementation for Modular Arithmetic #
This project provides a Fast Fourier Transform (FFT) implementation with modular arithmetic. It allows you to perform FFT operations on a list of numbers with a given modulus `Z`, a specified or automatically determined unit root, and an option for inverse FFT.

![GitHub](https://img.shields.io/github/license/ShaharAshe/FFT)

## How to Use ##
1. Clone or download the project code.
2. Import the `FFT` module into your Python script with `from FFT import FFT`.
3. Create a list of numbers to perform FFT on, specify a modulus `Z`, and optionally a unit root.
4. Call the `FFT` function with the list of numbers, the modulus, the unit root, and an inverse flag (False for FFT, True for inverse FFT).

Example usage:
```python
from FFT import FFT

FFT_vector = [1, 16, 2, 15, 3, 14, 4, 13, 5, 12, 6, 11, 7, 10, 8, 9]
Z = 17
unit_root = 6
inverse = False

result = FFT(FFT_vector, Z, unit_root, inverse=inverse)
print("FFT Result:", result)
```

**`unit_root = 0` if you don't know the unit root**

**`inverse = False` for FFT, `inverse = True` for inverse FFT**


## Notes ##
- The FFT algorithm in this project uses modular arithmetic. Make sure that `Z` is a prime number for proper behavior.
- If you don't provide a unit root, the code will attempt to find one. If it can't find a unit root, it will return an error message.
- The FFT implementation is recursive, so ensure that Python's recursion limit is sufficient for your data size.

## License ##
This project is licensed under the MIT License - see the `LICENSE` file for details.

---
