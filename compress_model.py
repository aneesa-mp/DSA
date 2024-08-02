import bz2
import pickle


# Correctly format the file paths
input_file_path = 'C:\\Users\\anees\\Downloads\\model.pkl'
output_file_path = 'C:\\Users\\anees\\Downloads\\model.pkl.bz2'

with open(input_file_path, 'rb') as f_in, bz2.BZ2File(output_file_path, 'wb') as f_out:
    pickle.dump(pickle.load(f_in), f_out)
    