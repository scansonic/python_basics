#  Создать текстовый файл (не программно).
#  Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
#  Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
#  Выполнить подсчёт средней величины дохода сотрудников.

with open('zarplata.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')
