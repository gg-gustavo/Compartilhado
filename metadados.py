import xml.etree.ElementTree as ET
import os

def get_element_text(element, namespaces):
    return element.text if element is not None else 'null'

# Iterate through all XML files in the 'revistas_xml' folder
for filename in os.listdir('revistas_xml'):
    if filename.endswith('.xml'):
        # Parse the XML file
        tree = ET.parse(os.path.join('revistas_xml', filename))
        root = tree.getroot()

        # Definir os namespaces
        namespaces = {
            'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
        }
        
        # Iterar sobre os elementos do XML usando namespaces
        for i, child in enumerate(root.findall('.//oai_dc:dc', namespaces)):
            title = child.find('dc:title', namespaces)
        
            # Manipulação para múltiplos elementos 'dc:creator'
            creators = [child.find(f'dc:creator[{j}]', namespaces) for j in range(1, 4)]
            creators = [get_element_text(creator, namespaces) for creator in creators]
        
            # Manipulação para múltiplos elementos'dc:subject'
            subjects = [child.find(f'dc:subject[{j}]', namespaces) for j in range(1, 4)]
            subjects = [get_element_text(subject, namespaces) for subject in subjects]
        
            # Manipulação para múltiplos elementos 'dc:identifier'
            identifiers = [child.find(f'dc:identifier[{j}]', namespaces) for j in range(1, 4)]
            identifiers = [get_element_text(identifier, namespaces) for identifier in identifiers]
        
            # Manipulação para múltiplos elementos 'dc:type'
            types = [child.find(f'dc:type[{j}]', namespaces) for j in range(1, 4)]
            types = [get_element_text(type, namespaces) for type in types]
        
            # Manipulação para múltiplos elementos 'dc:source'
            sources = [child.find(f'dc:source[{j}]', namespaces) for j in range(1, 4)]
            sources = [get_element_text(source, namespaces) for source in sources]
        
            description = child.find('dc:description', namespaces)
            publisher = child.find('dc:publisher', namespaces)
            date = child.find('dc:date', namespaces)
        
            # Verificar se 'dc:language' está presente
            language = child.find('dc:language', namespaces)
            language_text = get_element_text(language, namespaces)
        
            rights = child.find('dc:rights', namespaces)
        
            # Exibir os resultados
            print(f"Title: {get_element_text(title, namespaces)}")
            
            # Exibir múltiplos elementos 'dc:creator'
            for j, creator in enumerate(creators):
                print(f"Creator{j + 1}: {creator}")
        
            # Exibir múltiplos elementos 'dc:subject'
            for j, subject in enumerate(subjects):
                print(f"Subject{j + 1}: {subject}")
        
            # Exibir múltiplos elementos 'dc:identifier'
            for j, identifier in enumerate(identifiers):
                print(f"Identifier{j + 1}: {identifier}")
        
            # Exibir múltiplos elementos 'dc:type'
            for j, type in enumerate(types):
                print(f"Type{j + 1}: {type}")
        
            # Exibir múltiplos elementos 'dc:source'
            for j, source in enumerate(sources):
                print(f"Source{j + 1}: {source}")
        
            print(f"Description: {get_element_text(description, namespaces)}")
            print(f"Publisher: {get_element_text(publisher, namespaces)}")
            print(f"Date: {get_element_text(date, namespaces)}")
            print(f"Language: {language_text}")
            print(f"Rights: {get_element_text(rights, namespaces)}")
            print("\n")