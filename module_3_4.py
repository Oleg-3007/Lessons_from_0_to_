def single_root_words(root_word, *other_words):
    same_words = []
    other_words_ = list(other_words)
    
    for i in range(len(other_words_)):
        if root_word.lower() in other_words_[i].lower() or other_words_[i].lower() in root_word.lower():
            same_words.append(other_words_[i])
    return (same_words)        
            
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
