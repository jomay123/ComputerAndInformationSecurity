#!/usr/bin/env python3

import hashlib
import re
def custom_hash(input_string: str) -> str:
    data = input_string.encode('utf-8')

    for _ in range(100):
        data = hashlib.md5(data).digest()
    for _ in range(100):
        data = hashlib.sha256(data).digest()

    for _ in range(100):
        data = hashlib.sha512(data).digest()

    return data.hex()

def password_crack(target_hash: str, rockyou_path: str = "rockyou-20.txt"):
    pattern = re.compile(r'^[0-9A-Za-z]{6}$')  
    with open(rockyou_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            candidate = line.strip()
            if pattern.match(candidate):
                if custom_hash(candidate) == target_hash:
                    return candidate  
    return None


def main():
    # Suppose this is the hash we want to crack:
    target_hash = "620ddcc8f2881b8006ad58ff0175dd9c2a9e89a311285d6d6e3488a98e160d9e87194dbe7e9641028a621696d1bd8520bb6336f06d2a4c23ae24f0208d757da8"
    #target_hash2 = "de112cda87268821941fd95f3659d2abb1615acaaa33ff837b63efc55127e6a537b5a328c3602a2b5758a9115547bcb36661e4a5c3cd95195b4239a979b8e42b"
    #target_hash3 = "a2ff92fa895a9cbac4b5784e93a805b7a2819ac3bf0317c10cc18a2258a17cfdcff894f26b32a0f277b8341173152eec9f94aa8e302bd22aff6eac3c64ef32fc"
    found_password = password_crack(target_hash)
   # found_password2 = dictionary_attack(target_hash2)
   # found_password3 = dictionary_attack(target_hash3)
    if found_password:
        print(f"[+] Found matching password: {found_password}")
    else:
        print("[-] No match found in dictionary.")

   # if found_password2:
   #     print(f"[+] Found matching password: {found_password2}")
  #  else:
  #      print("[-] No match found in dictionary.")

  #  if found_password3:
   #     print(f"[+] Found matching password: {found_password3}")
  #  else:
   #     print("[-] No match found in dictionary.")

if __name__ == "__main__":
    main()

