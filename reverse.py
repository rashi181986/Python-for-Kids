class StringReverser:
    def reverse_words(self, text):
        # 1. split() breaks the string into a list of words
        # 2. [::-1] reverses that list
        # 3. ' '.join() puts them back together with spaces
        words = text.split()
        reversed_text = " ".join(words[::-1])
        return reversed_text

# Example Usage:
reverser = StringReverser()
input_string = "hello world python"
result = reverser.reverse_words(input_string)

print(f"Original: {input_string}")
print(f"Reversed: {result}")
