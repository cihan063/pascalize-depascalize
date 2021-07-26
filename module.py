# -*- coding: utf-8 -*-

def pascalize(text):
    """ Turns a string into PascalCase. 
    It uses a single uppercase letter for each additional word
    
    Args: 
        text : the sentence which will pascalize.
    
    Returns: 
        string type of list_str. This string returns us that pascalized text.
    """
    list_str = list(text)
    
    list_str[0] = list_str[0].upper()
    for count, value in enumerate(list_str):
        if value == " " or value == "_":
            list_str[count+1] = list_str[count+1].upper()
    
        
    list_str = [i for i in list_str if i != "_"]
    list_str = [i for i in list_str if i != " "]
    
    return ''.join(str(e) for e in list_str)

def depascalize(text):
    """
    This function converts pascalized text format to depascalized text format. 
    
    Args: 
        text : the sentence which will depascalize.
    
    Returns: 
        string type of tmp_str(list type). This string returns us that depascalized text.
    """
    list_str = list(text)
    tmp_str = []
    for count, value in enumerate(list_str):
        if value.isupper() == True:
            if count == 0 :
                tmp_str.append(value.lower())
            else:
                tmp_str.append("_")   
                tmp_str.append(value.lower())
                   
        else:
            tmp_str.append(value)
    return ''.join(str(e) for e in tmp_str)
            
    
    
    
            
    
    
            
