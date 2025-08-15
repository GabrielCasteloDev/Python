classroom = [
    [],
    [],
    [],
    []
]

while True:
    #seleção de metodo para lista
    insert_student = input('Insert Studant(i)\nShow Class Map(S)\nDesele Studant(D)\nExit(E):')


    #function input student
    if insert_student == 'i' or insert_student == 'I':
        line_select = input('Select Line: 1 - 2 - 3 - 4:')
        #check char
        try:
            line_select = int(line_select)
        except:
            print("Select a number.")
            continue

        i = 0

        #input studant on line
        if line_select >= 1 and line_select <= 4:
            studant = input("Name studant: ")
            classroom[line_select - 1].append(studant)
            i += 1
            continue
        else:
            print('Error number. Try again')
            continue


    #show list studants with line number
    if insert_student == "s" or insert_student == "S":
        fileira = 1
        for line in classroom:
            print('=================')
            print(f'Fileira {fileira}')
            fileira += 1
            for indice, aluno in enumerate(line):
               print(indice, aluno)
                

    #function delete studant list
    #if insert_student == "d" or insert_student == "D":

        #try:
        #    line_index = input("Choose number line of the student to delete: ")
        #    name_delete_index = input("Choose the name number of the student: ")
         #   line_index = line_index - 1
           # del classroom[line_delete][name_delete]

        #    if 0 <= name_delete_index < len(classroom[line_index]):
        #                        del classroom[line_index][name_delete_index]
        #                        print(f"Student '{classroom[line_index][name_delete_index]}' deleted from Line {line_index}.")
        #                       break
        #    continue
        #except:
        #     continue
    


