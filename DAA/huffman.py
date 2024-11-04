import heapq
from collections import defaultdict, Counter

# Class for Huffman Tree Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # Character
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child
        self.right = None  # Right child

    # Define comparator for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)  # Build a min-heap from nodes based on frequency

    while len(heap) > 1:
        # Remove the two nodes of highest priority (lowest frequency)
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new node with frequency equal to the sum of the two nodes
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)  # Insert the new node back into the heap

    # The remaining node is the root of the Huffman Tree
    return heap[0]

# Function to generate Huffman Codes
def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return

    # If this is a leaf node, store the character and its code
    if root.char is not None:
        codes[root.char] = current_code
        return

    # Traverse the left and right child
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

# Function to encode a given text using Huffman Codes
def huffman_encode(text):
    # Calculate frequency of each character
    frequencies = Counter(text)

    # Build Huffman Tree
    root = build_huffman_tree(frequencies)

    # Generate Huffman Codes
    codes = {}
    generate_huffman_codes(root, "", codes)

    # Encode the text
    encoded_text = ''.join(codes[char] for char in text)

    return encoded_text, codes

# Function to decode a Huffman encoded string
def huffman_decode(encoded_text, codes):
    reverse_codes = {code: char for char, code in codes.items()}
    decoded_text = ""
    current_code = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text

# Main program
text = input("Enter text to encode: ")
encoded_text, codes = huffman_encode(text)

print("Huffman Codes for each character:")
for char, code in codes.items():
    print(f"{char}: {code}")

print("\nEncoded Text:", encoded_text)

# Decode the encoded text to verify
decoded_text = huffman_decode(encoded_text, codes)
print("\nDecoded Text:", decoded_text)
