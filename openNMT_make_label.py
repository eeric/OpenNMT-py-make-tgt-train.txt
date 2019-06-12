import os

def Splitfile(filepath,f1,f2):
    with open(filepath) as f:
        ids = f.readlines()
    ids = [x.strip().split(',') for x in ids]
    size = len(ids)
    for ii in range(size):
        sample = ids[ii]
        audio_path, transcript_path = sample[0], sample[1]
        f1.write(audio_path + '\n')#wav list file
        transcript = label_transcript(transcript_path)
        f2.write(transcript + '\n')#sentence text list file

def label_transcript(transcript_path):
        with open(transcript_path, 'r', encoding='utf8') as transcript_file:
            lines = transcript_file.read().replace('\n', '')
            transcript = blank_space(lines)
        return transcript
#label form		
def blank_space(sentence):
    tt=sentence.split(' ')
    num = len(tt)
    zz = []
    for jj in range(num):
        yy=[ x+' ' for x in list(tt[jj][:-1])]
        yy.append(tt[jj][-1])
        yy_str = "".join([str(x) for x in yy])
        zz.append(yy_str)
        if jj < num-1:
            zz.append(' <space> ')
    zz_str = "".join([str(x) for x in zz])
    return zz_str

if __name__ == '__main__':
    #'train.csv' from deepspeech.pytorch: https://github.com/SeanNaren/deepspeech.pytorch
    fpath = '/your_path_to/train.csv'
    fn1 = './data/src-train.txt'
    file1 = open(fn1, 'w')
    fn2 = './data/tgt-train.txt'
    file2 = open(fn2, 'w')
    Splitfile(fpath,file1,file2)
    file1.close()
    file2.close()
    print('ok')
