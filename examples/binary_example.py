from goph419.binary import (
    bin_add_4,
    bin_value,
    dec2bin_array,
    floor_div_2,
    dec2bin,
)


def main():
    a = [0, 1, 1, 1]
    b = [0, 1, 0, 1]
    print(f"  {a}: {bin_value(a)}")
    print(f"+ {b}: {bin_value(b)}")

    c = bin_add_4(a, b)
    print(f"= {c}: {bin_value(c)}")
    print(f"      expected: {(bin_value(a) + bin_value(b)) % 16}")

    print()

    d = "913"
    print(f"{d}:\n{dec2bin_array(d)}")

    print()

    for k in range(10):
        s = str(k)
        d = dec2bin_array(s)[0]
        d_2 = floor_div_2(d)
        v = bin_value(d_2)
        print(f"{k} // 2 = {d_2} = {v} = {dec2bin(v)}")

    print()

    s = 1042
    b = dec2bin(s)
    d = bin(s)
    print(f"{s} -> {dec2bin(s)} -> {d}")


if __name__ == "__main__":
    main()
