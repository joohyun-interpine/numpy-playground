import pandas as pd
import numpy as np
import laspy

def load_npy_file(npy_file_path):
    df = pd.DataFrame(np.load(npy_file_path))
    array = np.load(npy_file_path)
    
    return array


def open_laz_file_to_numpy(laz_file_path):
    inFile = laspy.read(laz_file_path)
    pointcloud = np.vstack((inFile.x, inFile.y, inFile.z))    
    pointcloud = pointcloud.transpose()
    # headers_of_interest = []
    # output_headers = []
    # coord_headers = ['x', 'y', 'z']
    
    # if len(headers_of_interest) != 0:
    #     headers_of_interest = headers_of_interest[3:]
    #     for header in headers_of_interest:
    #         if header in header_names:
    #             pointcloud = np.vstack((pointcloud, getattr(inFile, header)))
    #             output_headers.append(header)
    
    return pointcloud
     
def main():
    # npy_file_path = r'C:\Users\JooHyunAhn\Interpine\GitRepos\TreeTools\data\smallchips\0000008.npy'
    # array = load_npy_file(npy_file_path)
    # print(array.shape)
    
    laz_file_path = r'C:\Users\JooHyunAhn\Interpine\GitRepos\TreeTools\data\LIR184_FT_output-sample\LIR184_working_point_cloud.laz'    
    pointcloud = open_laz_file_to_numpy(laz_file_path)
    print(type(pointcloud))
    print(pointcloud.shape)
    
    
main()
    

