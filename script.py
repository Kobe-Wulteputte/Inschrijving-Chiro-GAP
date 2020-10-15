import pandas as pd
import re

afdelingscode = {
    'sjamfoeter': 84683,
    'speelclub': 84684,
    'rakker': 84685,
    'topper': 84686,
    'kerel': 84687,
    'aspirant': 84688
}
    

df = pd.read_excel("vul_in.xlsx")
elementIds = open('elementIds.txt', 'r').readlines() 
outFile = open('OUT.txt', 'w')

# Clean up tel numbers
df['Telefoonnummer'].replace(to_replace ='[ -/.]', value = '', regex = True, inplace=True) 
df['Telefoonnummer'].replace(to_replace ='^(0032|32|\+320)', value = '+32', regex = True, inplace=True)
df['Telefoonnummer'].replace(to_replace ='.*0(4[0-9]{8}|9[0-9]{7}).*', value = r'+32\1', regex = True, inplace=True)

# Remove whitespaces
df.replace(r'^\s+', '', regex=True, inplace=True) #front
df.replace(r'\s+$', '', regex=True, inplace=True) #end

# Force lowercase
df['Email'] = df['Email'].str.lower()
df['Afdeling'] = df['Afdeling'].str.lower()

# Split bus and huisnummer
df['Bus'] = df['Huisnummer'].str.extract(r'\d(\w+)', expand=False)
df['Bus'] = df['Bus'].str.upper()
df['Huisnummer'] = df['Huisnummer'].apply(str)
df['Huisnummer'] = df['Huisnummer'].str.replace(r'(\D+)','')

# Remove all non digits from postcode
df['Postcode'] = df['Postcode'].apply(str)
df['Postcode'] = df['Postcode'].str.replace(r'(\D+)','')
print(df)


for index, row in df.iterrows():
    # voornaam
    print(elementIds[0].strip() + ' \"' + row[0] + '\"')
    outFile.write(elementIds[0].strip() + ' \"' + row[0] + '\"\n')
    # achternaam
    print(elementIds[1].strip() + ' \"' + row[1] + '\"')
    outFile.write(elementIds[1].strip() + ' \"' + row[1] + '\"\n')
    # geboortedatum
    print(elementIds[2].strip() + ' \"' + row[2].strftime("%d/%m/%Y") + '\"')
    outFile.write(elementIds[2].strip() + ' \"' + row[2].strftime("%d/%m/%Y") + '\"\n')
    # Geslacht
    print(elementIds[3].strip())
    outFile.write(elementIds[3].strip() + '\n')
    # PostNr
    print(elementIds[4].strip() + ' \"' + str(row[8]) + '\"')
    outFile.write(elementIds[4].strip() + ' \"' + str(row[8]) + '\"\n')
    print(elementIds[5].strip())
    outFile.write(elementIds[5].strip() + '\n')
    # Timeout
    print(elementIds[6].strip())
    outFile.write(elementIds[6].strip() + '\n')
    # Straatnaam
    print(elementIds[7].strip() + ' \"' + row[6] + '\"')
    outFile.write(elementIds[7].strip() + ' \"' + row[6] + '\"\n')
    # HuisNr
    print(elementIds[8].strip() + ' \"' + str(row[7]) + '\"')
    outFile.write(elementIds[8].strip() + ' \"' + str(row[7]) + '\"\n')
    # Bus
    if not pd.isna(row['Bus']):
        print(elementIds[9].strip() + ' \"' + str(row[10]) + '\"')
        outFile.write(elementIds[9].strip() + ' \"' + str(row[10]) + '\"\n')
    # Woonplaats
    print(elementIds[10].strip() + ' \"' + row[9] + '\"')
    outFile.write(elementIds[10].strip() + ' \"' + row[9] + '\"\n')
    # Email
    print(elementIds[11].strip() + ' \"' + row[5] + '\"')
    outFile.write(elementIds[11].strip() + ' \"' + row[5] + '\"\n')
    # Tel
    print(elementIds[12].strip() + ' \"' + row[4] + '\"')
    outFile.write(elementIds[12].strip() + ' \"' + row[4] + '\"\n')
    # lid
    print(elementIds[13].strip())
    outFile.write(elementIds[13].strip() + '\n')
    print(elementIds[14].strip())
    outFile.write(elementIds[14].strip() + '\n')
    # Afdeling
    print(elementIds[15].strip() + ' ' + str(afdelingscode[row[3]]))
    outFile.write(elementIds[15].strip() + ' ' + str(afdelingscode[row[3]]) + '\n')
    # Press button
    print(elementIds[16].strip())
    outFile.write(elementIds[16].strip() + '\n')
    print()
    outFile.write('\n')

# TODO:
# Documentatie scrijven voor noobs
# Voorbeeld data in de vul_in.xlsx
# pytoexe