import re
import sys

def sum_numbers(line):
    numbers = re.findall(r'\d+', line)
    return sum(map(int, numbers))

def process_text(text_file):
    with open(text_file, "r") as file:
        text = file.read()
    
    total_sum = 0
    summing_enabled = True
    output = []
    off_string = [-1, -1, -1]
    on_string = [-1, -1]

    lines = text.split('\n')
    for line in lines:
        words = line.split()
        new_line = []
        for word in words:
            for char in word:
                if char.lower() == 'o' and summing_enabled:
                    off_string[0] = 'o'
                elif char.lower() == 'f' and summing_enabled:
                    if off_string[1] == 'f':
                        off_string[2] = 'f'
                    else:
                        off_string[1] = 'f'
                elif char.lower() == 'o' and not summing_enabled:
                    on_string[0] = 'o'
                elif char.lower() == 'n' and not summing_enabled:
                    on_string[1] = 'n'
                
                if off_string == ['o', 'f', 'f']:
                    summing_enabled = False
                    total_sum += sum_numbers(' '.join(new_line))
                    new_line = []  # Reset line
                    off_string = [-1, -1, -1]  # Reset off
                if on_string == ['o', 'n']:
                    summing_enabled = True
                    new_line = []  # Reset line
                    on_string = [-1, -1]  # Reset on
            
            new_line.append(word)
            
            if '=' in word:  # If '=' is in the word, print the sum
                if summing_enabled:
                    total_sum += sum_numbers(' '.join(new_line))
                    output.append(f'{total_sum}')
                    new_line = []  # Reset line
                else:
                    output.append(f'{total_sum}')
    total_sum += sum_numbers(' '.join(new_line))
    output.append(f'{total_sum}')  # Final sum
    return '\n'.join(output)

if __name__ == "__main__":
    text_file = sys.argv[1]
    print(process_text(text_file))
