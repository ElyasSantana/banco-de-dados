import faker
import random

faker = faker.Faker(locale="pt_BR")

with open("readme.csv", "w") as f:
    f.write("nomeAluno,endereco,dataNascimento,Curso_codigoCurso\n")
    for _ in range(10):
        codigoCurso: int = random.randint(1, 5)
        insert: str = f"INSERT INTO Curso (nomeAluno,endereco,dataNascimento) VALUES ('{faker.name()}','{faker.street_name()}','{faker.date()}',{str(codigoCurso)});\n"
        #insert: str = f"{faker.name()},{faker.street_name()},{faker.date()},{str(codigoCurso)}\n"
        f.write(insert)
