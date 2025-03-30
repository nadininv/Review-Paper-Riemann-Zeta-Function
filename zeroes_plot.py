import mpmath
import matplotlib.pyplot as plt

def zeta_zero_check(z):
    result = mpmath.zeta(z)
    return mpmath.almosteq(result, 0)

complex_numbers = [
    complex(0.5, 14.1347251417346937904572519835625),
    complex(0.5, 21.0220396387715549926284795938969),
    complex(0.5, 25.0108575801456887632137909925268),
    complex(0.5, 32),
    complex(-2, 0),
    complex(-4, 0),
    complex(-6, 0),
    complex(-1, 0),
    complex(5, 3),
    complex(-5, 4),
    complex(1, 2),
    complex(0.5, 7)
]

zeros = []
non_zeros = []

for z in complex_numbers:
    if zeta_zero_check(z):
        zeros.append(z)
    else:
        non_zeros.append(z)

if zeros:
    plt.plot([z.real for z in zeros], [z.imag for z in zeros], 'ro', label='Zeros')
if non_zeros:
    plt.plot([z.real for z in non_zeros], [z.imag for z in non_zeros], 'bo', label='Non-Zeros')

plt.title("Zeros of the Riemann Zeta Function")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")

plt.axvline(x=0.5, color='yellow', linestyle='--', label='Critical Line (Re(s) = 0.5)')
plt.axhline(0, color='black')
plt.axhline(0, color='black')

plt.legend()
plt.show()
