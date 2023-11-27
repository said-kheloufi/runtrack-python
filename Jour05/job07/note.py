def arrondir_notes(notes):
    notes_arrondies = []
    
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_superieur = ((note // 5) + 1) * 5
            difference = multiple_de_5_superieur - note
            
            if difference < 3:
                note_arrondie = multiple_de_5_superieur
            else:
                note_arrondie = note
            
            notes_arrondies.append(note_arrondie)
    
    return notes_arrondies

notes_originales = [37, 82, 55, 93, 68]
notes_arrondies = arrondir_notes(notes_originales)

print("Notes originales :", notes_originales)
print("Notes arrondies  :", notes_arrondies)
