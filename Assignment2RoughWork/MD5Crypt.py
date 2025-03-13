import csv
import re
import crypt
import itertools

def load_wordlist_from_csv(csv_file):
    """Reads the CSV file and returns a list of words."""
    wordlist = []
    with open(csv_file, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                wordlist.append(row[0].strip())
    return wordlist

def generate_variants(word):
    """Generate basic variants: original, lowercase, uppercase, capitalized, cleaned."""
    variants = set()
    variants.add(word)
    variants.add(word.lower())
    variants.add(word.upper())
    variants.add(word.capitalize())
    # Cleaned: remove non-alphanumeric characters
    cleaned = re.sub(r'[^A-Za-z0-9]', '', word)
    variants.add(cleaned)
    return variants

def generate_appended_prepend_variants(word, max_number=100):
    """Generate variants by appending and prepending numbers (0 to max_number)."""
    variants = set()
    for num in range(max_number + 1):
        variants.add(f"{word}{num}")
        variants.add(f"{num}{word}")
    return variants

def generate_inserted_number_variants(word, digits=range(10)):
    """Generate variants by inserting a single digit at every possible position in the word."""
    variants = set()
    for i in range(1, len(word)):
        for d in digits:
            new_variant = word[:i] + str(d) + word[i:]
            variants.add(new_variant)
    return variants

def generate_leet_variants(word):
    """Generate leet (1337) substitutions for the word."""
    mapping = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }
    variants = set()
    def helper(current, index):
        if index == len(word):
            variants.add(current)
            return
        char = word[index]
        # Use original character:
        helper(current + char, index + 1)
        # If a substitution exists, also try it:
        lower_char = char.lower()
        if lower_char in mapping:
            helper(current + mapping[lower_char], index + 1)
    helper("", 0)
    return variants

def generate_all_variants(word, max_number=100):
    """
    Generate a comprehensive set of variants for a word by combining:
      - Basic variants (case and cleaning)
      - Appended and prepended numbers
      - Inserted number variants
      - Leet substitutions
    """
    all_variants = set()
    base_variants = generate_variants(word)
    for base in base_variants:
        all_variants.add(base)
        all_variants.update(generate_appended_prepend_variants(base, max_number))
        all_variants.update(generate_inserted_number_variants(base))
        all_variants.update(generate_leet_variants(base))
    return all_variants

def generate_pair_combinations(wordlist):
    """Generate variants by concatenating every pair of distinct words (in both orders)."""
    pair_variants = set()
    for word1, word2 in itertools.combinations(wordlist, 2):
        pair_variants.add(word1 + word2)
        pair_variants.add(word2 + word1)
    return pair_variants

def crack_md5crypt(target_hash, wordlist, max_number=100):
    """
    Attempt to crack the MD5Crypt hash by trying:
      1. All variants of individual words from the wordlist.
      2. Variants of concatenated pairs of words.
    """
    salt = target_hash.split('$')[2]
    salt_param = f"$1${salt}$"
    tested = 0

    # First, try variants for each individual word.
    for candidate in wordlist:
        candidate = candidate.strip()
        for variant in generate_all_variants(candidate, max_number):
            tested += 1
            candidate_hash = crypt.crypt(variant, salt_param)
            # Uncomment the next line to see what is being tried:
            # print(f"Trying: {variant} -> {candidate_hash}")
            if candidate_hash == target_hash:
                print("Password found:", variant)
                print("Tested variants:", tested)
                return variant

    # Next, try pair combinations of words.
    pair_list = list(generate_pair_combinations(wordlist))
    for pair in pair_list:
        for variant in generate_all_variants(pair, max_number):
            tested += 1
            candidate_hash = crypt.crypt(variant, salt_param)
            if candidate_hash == target_hash:
                print("Password found (pair):", variant)
                print("Tested variants:", tested)
                return variant

    print("Password not found. Total tested variants:", tested)
    return None

if __name__ == "__main__":
    # Load the Bee Movie wordlist from CSV.
    wordlist = load_wordlist_from_csv("bee_movie_words.csv")
    
    # Your target MD5Crypt hash.
    target_hash = "$1$3XiOY4Vw$hxGRCzqTNhdXC4ypiT92s1"
    
    crack_md5crypt(target_hash, wordlist, max_number=100)
