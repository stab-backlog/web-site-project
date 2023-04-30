class FromSystemToSystem:
    def from_ten_to_n(self, original_number, system_to):
        number_o = ''
        o = int(system_to)

        s = []
        p = 0
        num = int(original_number)

        for i in range(int(original_number)):
            if num in range(1, o):
                number_o += f'{num if num not in dc.keys() else dc.get(f"{num % o}")}'
                break

            remainder = num % o if f'{num % o}' not in dc.keys() else dc.get(f'{num % o}')

            if len(s) == 0:

                s = [
                    f' {num} | {o}',
                    f'- {" " * len(str(num))} –––––',
                    f' {num // o * o} | {num // o}',
                    f'{"–" * (len(str(num)) + 2)}',
                    f' {remainder}  {" " * (len(str(num)) - 1)}',
                ]

                number_o += f'{remainder}'

                p = len(str(num)) + 2

            else:
                s_n = [(k, s[k].find(str(num))) for k in range(len(s) - 1, -1, -1) if s[k].find(str(num)) != -1]
                s[s_n[0][0]] = s[s_n[0][0]][:s_n[0][1]] + f'{num} | {o}'
                s[s_n[0][0] + 1] += f'  - {" " * len(str(num))} –––––'
                s[s_n[0][0] + 2] += f' {num // o * o} | {num // o}'

                s += [
                    f'{" " * p}{"–" * (len(str(num)) + 2)}',
                    f'{" " * p} {remainder}  {" " * (len(str(num)) - 1)}{" " * (len(str(num)) - 1)}',
                ]

                number_o += f'{remainder}'

                p += len(str(num)) + 3

            num //= o

        return s, number_o[::-1]

    def from_n_to_ten(self, original_number, system_from):
        o = int(system_from)
        num = 0
        s = []
        lst_of_numbers = []

        for i in range(1, len(original_number) + 1):
            el = original_number[-i] if elem(dc, original_number[-i]) is None else elem(dc, original_number[-i])
            n = int(el) * o ** (i - 1)
            lst_of_numbers.append(f'{n}')
            num += n
            s.append(f'{el} * {o} ** {i - 1} = {n}')
        else:
            s.append('+'.join(lst_of_numbers) + '={}'.format(num))

        return s, str(num)

    def get_number(self, original_number, system_from, system_to):
        answer = FromSystemToSystem()
        if system_from == '10':
            return answer.from_ten_to_n(original_number, system_to)
        else:
            if system_to == '10':
                return answer.from_n_to_ten(original_number, system_from)
            else:
                return answer.from_ten_to_n(answer.from_n_to_ten(original_number, system_from)[-1], system_to)


class ToHtml:
    def transfer(self, lst, number):
        trans_list = ['<!doctype html>', '<html lang="en">',
                      '<head>', '<style> pre {font-weight: bold; font-size: larger}</style>', '</head>',
                      '<body>',
                      '<h1>', number, '</h1>',
                      '</body>',
                      '</html>']
        for element in range(1, len(lst) + 1):
            trans_list.insert(-1 - element, '<pre>{}</pre>'.format(lst[-element]))
        return ''.join(trans_list)


def elem(dictionary, value):
    for k, v in dictionary.items():
        if v == value:
            return k


dc = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F',
}

if __name__ == '__main__':
    answer = FromSystemToSystem()
    num_a = answer.get_number('123', '10', '2')
    print(*num_a[0], sep='\n')
    print(num_a[1])

    to = ToHtml()
    print(to.transfer(num_a[0], num_a[1]))
