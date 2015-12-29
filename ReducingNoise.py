import column
import sys
import collections

##
# Takes a FASTA file. Takes away the columns where there are more than 50% indels.
# Call column and SeqDic. Caled by 50unique
##

def Indels(fil):
    seq_dic=column.SeqDic(fil)
    columns=column.column(fil)
    for k in columns:
        Indel = re.findall('-',columns[k])
        LenIndel = len(Indel)
        LenColumn = len(columns[k])
        if float(LenIndel)/LenColumn > 0.5:
            Pos=int(k)
            for key in seq_dic:
                seq_dic[key]=seq_dic[key][:Pos]+seq_dic[key][Pos+1:]
        else:
            pass

    return seq_dic

##
# Takes a FASTA file. Takes away the columns where at least 50% of amino acids
# are unique.
# Call Indels and column, Caled by MoreThan2.
##

def 50unique(fil)
    seq_dic=Indels(fil)
    columns=column.column(fil)
    for k in columns:
        results=collections.Counter(columns[k])
        cunter=0
        for key in results:
            if results[key]==1:
                cunter=cunter+1
            else:
                pass
        if float(cunter)/len(results)>=0.5:
            Pos=int(k)
                for keyS in seq_dic:
                    seq_dic[keyS]=seq_dic[keyS][:Pos]+seq_dic[keyS][Pos+1:]
            else:
                pass
    return seq_dic

##
# Takes a FASTA file. Takes away the columns where no amino acid appers more
# than twice.
# Call 50unique and column. Caled by ? 
##
def MoreThan2(fil):
    seq_dic=50unique(fil)
    columns=column.column(fil)
    for k in columns:
        results=collections.Counter(columns[k])
        number=[]
        for key in results:
            number.append(results[key])
            greater2=[i for i in number if i>2]
            if len(greater2)==0:
                Pos=int(k)
                for keyS in seq_dic:
                    seq_dic[keyS]=seq_dic[keyS][:Pos]+seq_dic[keyS][Pos+1:]
            else:
                pass
    print seq_dic
                
                
            
        
