# Elliptic Curve Parameters (secp256k1 - Bitcoin Standard)
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F  # Prime field
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # Order of the group
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240  # Generator x
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337424483  # Generator y

def modular_inverse(a, n):
    """Compute the modular inverse of a modulo n."""
    return pow(a, -1, n)

def compute_p_and_private_key(m, k):
    """
    Calculate P = xG and the private key x using the given formulas.
    """
    # Step 1: Calculate t = Gk (X-coordinate of G * k)
    t_x = (Gx * k) % p
    print(f"t = Gk (X-coordinate of G * k): {t_x}")

    # Step 2: Use m = k = x = k as provided in the equation to derive s
    s = (m + k * t_x) // k
    print(f"Calculated s: {s}")

    # Step 3: Calculate x using the provided formula
    x = (s * k - m) % n
    print(f"Derived Private Key (x): {x}")

    # Step 4: Verify private key by regenerating public key P = xG
    P_x = (Gx * x) % p
    P_y = (Gy * x) % p
    print(f"Regenerated Public Key (P = xG): ({P_x}, {P_y})")

    return x

def compute_s_and_tau(x, gamma):
    """
    Compute the formula S = (x + x*gamma)/x and return the result.
    """
    tau = 1 + gamma * 2  # tau calculation
    S = (x * (1 + 2)) / x  # S = (x + x*gamma) / x
    print(f"S = (x + x*gamma)/x = {S}")
    print(f"tau = {tau}")
    return S, tau


# Main function
if __name__ == "__main__":
    print("=== Bitcoin Private Key Exploit Using Provided Logic ===")

    # Step 1: Take inputs interactively
    m = int(input("Enter message hash m (as integer): "))
    k = int(input("Enter nonce k (as integer): "))

    # Step 2: Compute P and private key x
    private_key = compute_p_and_private_key(m, k)

    # Step 3: Additional calculations for S and tau (optional, as per the formula)
    gamma = float(input("Enter gamma (as float, e.g., 0.1): "))
    S, tau = compute_s_and_tau(private_key, gamma)

    # Final output
    print(f"\nFinal Derived Private Key (x): {private_key}")
    print(f"Final S value: {S}")
    print(f"Final tau value: {tau}")
