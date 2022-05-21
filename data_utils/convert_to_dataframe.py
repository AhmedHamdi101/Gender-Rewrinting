import pandas as pd
import numpy as np
import argparse
import os

def main(args):
    type = args.type
    path = args.path
    split = args.split
    save_path = args.save_path

    print(type, path , split)
    split_path = path+split+"/"
    arabic_data_path = split_path + split + ".ar." + type
    english_data_path = split_path+split+".ar."+type+".en"
    id_path = split_path+split+".ar."+type+".ids" 
    label_path = split_path+split+".ar."+type+".label"

    with open(arabic_data_path, encoding="utf-8") as f:
        data = np.array(f.readlines())
        data = np.expand_dims(data , axis=1)
        
    with open(english_data_path, encoding="utf-8") as f:
        en_data = np.array(f.readlines())
        en_data = np.expand_dims(en_data , axis=1)
        
    with open(id_path, encoding="utf-8") as f:
        id = np.array(f.readlines())
        id = np.expand_dims(id , axis=1)

    with open(label_path, encoding="utf-8") as f:
        labels = np.array(f.readlines())
        labels = np.expand_dims(labels , axis=1)

    dataframe = np.concatenate([id , data , en_data , labels ] ,axis = 1)

    df = pd.DataFrame(dataframe , columns=["Id" , "Arabic Line" , "English Line" , "Lables"])
    if not os.path.isdir(save_path): 
        os.mkdir(save_path)
    df.to_csv(save_path+split+"_ar_"+type+".csv",index=False,encoding='utf-8-sig')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-T","--type",      help="Type of the data" , choices=["MM","MF","FF","FM"] , type=str)
    parser.add_argument("-S","--split",     help="Split of the data" , choices=["train","dev","test"] , type=str)
    parser.add_argument("-P", "--path" ,    help="Path of the data" ,type=str)
    parser.add_argument("-SP", "--save_path" ,    help="The path for saving processed data" ,type=str)
    
    args = parser.parse_args() 
    main(args)
# 