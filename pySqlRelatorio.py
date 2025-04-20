# Kauã Alexandre Bernardes e Maria Júlia Leopoldo Barros

import mysql.connector # type: ignore

def connectDB():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "serra",
        database = "empresa"
    )

    return mydb

def desconnectDB(mydb) -> tuple:
    mydb.close()

def faixaSalarial(where:str,mydb) -> str:
    strResult = str()
    somaSal = float()
    cursor = mydb.cursor()

    cursor.execute(f"SELECT * FROM empregado WHERE {where}")
    results = cursor.fetchall()
    strResult = f"|{'-' * 77}|\n" + f"|{'Nome':56}CPF{'Salario'.rjust(18,' ')}|\n" + f"|{'-' * 77}|\n"
    for linha in results:
        strResult = (strResult + f"|{linha[1].ljust(45,' ')}{linha[2][0:3] + '.' + linha[2][3:6] + '.' + linha[2][6:9] + '-' + linha[2][9:11]}{linha[6]}\n")
        somaSal = somaSal + float(linha[6])

    return f"{strResult}Total = {somaSal}\n"

def relatorio(faixaSal1:str,faixaSal2:str,faixaSal3:str):
    file = open("relatorio.txt", "a")
    texto = f"|{'*' * 77}|" + f"\n|{'Salario abaixo de R$3000,00'.center(77, ' ')}|"  + f"\n|{'*' * 77}|" + f"\n{faixaSal1}"
    texto += f"|{'*' * 77}|" + f"\n|{'Salario entre R$3000,00 e R$5000,00'.center(77, ' ')}|"  + f"\n|{'*' * 77}|" + f"\n{faixaSal2}"
    texto += f"|{'*' * 77}|" + f"\n|{'Salario acima de R$5000,00'.center(77, ' ')}|"  + f"\n|{'*' * 77}|" + f"\n{faixaSal3}"
    file.write(texto)
    file.close()

def main():
    mydb = connectDB()
    faixaSal1 = (faixaSalarial("valSalEmprg < 3000" , mydb))
    faixaSal2 = (faixaSalarial("(valSalEmprg >= 3000) AND (valSalEmprg <= 5000)" , mydb))
    faixaSal3 = (faixaSalarial("valSalEmprg > 5000" , mydb))
    relatorio(faixaSal1,faixaSal2,faixaSal3)
    desconnectDB(mydb)

if __name__ == "__main__":
    main()



