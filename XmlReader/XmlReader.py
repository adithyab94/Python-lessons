import pandas as pd
import xml.etree.ElementTree as et

def parse_XML(xml_file, df_cols): 
    
    xtree = et.parse(xml_file)
    xroot = xtree.getroot()
    out_df = pd.DataFrame(columns = df_cols)
    
    for node in xroot: 
        res = []
        res.append(node.attrib.get(df_cols[0]))
        for el in df_cols[1:]: 
            if node is not None:
                res.append(node.find(el).text)
            else: 
                res.append(None)
        out_df = out_df.append(pd.Series(res, index = df_cols), ignore_index = True)    
    return out_df



print(parse_XML("C:\\xml\\sample.xml", ["name", "email", "grade", "age"]))
