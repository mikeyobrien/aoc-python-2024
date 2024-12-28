

with open('input.txt', 'r') as f:
    CONTENTS = f.read()

def main():
    rules, page_updates = CONTENTS.split('\n\n')
    rules = rules.split('\n')
    page_updates = page_updates.split('\n')

    rules_dict = {}
    for rules in rules:
        key, value = rules.split('|')
        lst = rules_dict.get(key, [])
        lst.append(value)
        rules_dict[key] = lst

    print(rules_dict)
    valid_updates = []
    for page_update in page_updates[:len(page_updates)-1]:
        page_numbers = page_update.split(',')
        invalid_update = False
        for i in range(len(page_numbers)):
            rule = rules_dict.get(page_numbers[i], [])
            for p in rule:
                if p in set(page_numbers[:i]):
                    print("invalid rule", page_update)
                    invalid_update = True
                    break
            if invalid_update:
                break
        if not invalid_update:
            valid_updates.append(page_numbers)
    print(valid_updates)
    res = 0
    for valid_update in valid_updates:
        mid = len(valid_update) // 2
        res += int(valid_update[mid])
    print("Result:", res)



main()
