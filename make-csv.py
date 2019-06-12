#make .csv file to deepspeech2.pytorch: https://github.com/SeanNaren/deepspeech.pytorch
import os

root = '/your_path'
wav = os.walk(root+'/'+'wav')
txt = root+'/'+'txt'
fn = './csv/test/LibriSpeech_dataset-test_clean.csv'
file = open(fn, 'w')
for path,d,filelist in wav:
    for filename in filelist:
        if filename.endswith('.wav'):
            tn = filename[:-4] + '.txt'
            if os.path.isfile(os.path.join(txt, tn)):
                sample = os.path.join(path, filename) + ',' + os.path.join(txt, tn) + '\n'
                file.write(sample)
file.close()
