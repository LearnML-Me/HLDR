#!/root/miniconda3/envs/envp39/bin/python3
import difflib

def smart_merge(en1, en2, ja):
    ja = ja.strip().split('、')
    en1_words = en1.split()
    en2_words = en2.split()
    en1_comma_index = [index for index, word in enumerate(en1_words) if word.endswith(",")]
    en2_comma_index = [index for index, word in enumerate(en2_words) if word.endswith(",")]

    en1 = en1.replace(',', '')
    en2 = en2.replace(',', '')

    differ = difflib.Differ()
    diff = list(differ.compare(en1.split(), en2.split()))

    result_words = []
    in_difference = False
    ja_index = 1  # Start with the first replacement, skipping noise
    en_index = 0

    while en_index < len(diff):
        while en_index < len(diff) and diff[en_index].startswith(' '):
            if en_index in en1_comma_index or en_index in en2_comma_index:
                result_words.append(diff[en_index][2:] + ',')
            else:
                result_words.append(diff[en_index][2:])
            en_index += 1
        while en_index < len(diff) and (diff[en_index].startswith('-') or diff[en_index].startswith('+')):
            if not in_difference:
                in_difference = True
                if ja_index < len(ja):
                    result_words.append(ja[ja_index].strip()+',')
                    ja_index += 2  # Skip noise portion
            en_index += 1
        in_difference = False

    processed_string = ' '.join(result_words)

    return processed_string

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    file_name_en1 = 'en1.txt'
    file_name_en2 = 'en2.txt'
    file_name_ja = 'ja.txt'
    file_name_combined = 'combined.txt'

    en1 = read_file(file_name_en1)
    en2 = read_file(file_name_en2)
    ja = read_file(file_name_ja)

    processed_string = smart_merge(en1, en2, ja)

    write_to_file(file_name_combined, processed_string)

    print(f"Content has been written to {file_name_combined}.")

if __name__ == "__main__":
    main()

