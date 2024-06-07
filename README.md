# distance_estimation
Camera calibration for distance estimation

## Repository Structure
### Main Directories:

#### 1.ZhangChBoardMethod
##### Description:
    This directory contains multiple tests done to test zhangs method.

##### Content:
    -Inside we have our three main python files used for the main test, a Main file  were the we runned the test and 2 files composed by different functions used in the main.

    -FirstTestChess: Contains the first alpha test donne. Its is compose of the differents used images  and 2 scripts, One main script to run the test and the second script being different fonctions definitions.

    -Test 0 - 4 : Are the main test of zhang's method implementation. These directories contiens the image used for each test and their results


#### 2.PointsHomography
##### Description:
    Directory containing our main study of using homography and camera calibration to estimate  real world distances in a image.

##### Content:
    -Inside we have our different scripts for the different tests and 2 directories. We have 2 classes CameraCalibration and SizeEstimations that will be instantiated and used in the different main scripts.
        ~Main_CCU is the main python file we use to retrieve our camera calibration transformation matrix and scale factor.
        
        ~Main_CCU_MoreImages same as Main_CCU but with more images used to calculate the transformation matrix.

        ~Main_SE_CCU is the file where we  apply the  camera calibration transformation matrix and scale factor previously saved  on  different images (taken by the same static camera) with objects of unknown dimensions  to estimate their size .

        ~Main_Homography is the main python file we use to retrieve our homography matrix and scale factor.

        ~Main_SE_H is the file where we  apply the  homography transformation matrix and scale factor previously saved  on  different images (taken by the same static camera) with objects of unknown dimensions  to estimate their size.

        ~Main_SE_UH is the last file where we apply both our camera calibration matrix to remove distortion the images and then the homography matrix. We then re calculate our scale factor and finally take the different images (taken by the same static camera) with objects of  unknown dimensions  to estimate their size.

    -Images directory, where we stock all the images, the ones we use to estimate our matrices, to calculate the scale factors and to estimate unknown dimensions.

    -Pickle directory, where we stock our pickle files that contains the different transformation matrices and scale factors.


#### 3.LinesHomography
##### Description:
    Directory containing the test of implementing Homography transformation with line correspondence.
    Although different test and implementations of DLT algorithm were made the results were unsuccessful.

##### Content:
    -Two main python files to execute the test.
    -Main_Alpha , where the implementation of dlt algorithm without Opencv and the input of different lines were made.
    -Main_SVDPoints, Test to compare our DLT algorithm for homography with points with OpenCv's algorithm
    -Directory with all the images used to test the homography. Some images have their lines used for correspondence marked


#### 4.HomographyAutomation
##### Description:
    Development of an web application using StreamLit for simplifying and automatizing the process of homographic image transformation  and dimensional estimation.

##### Content:
    -MainPage is hte first page of our web, were we are able to input an image from our pc and the set of real world coordinates of our reference points
    -Pages directory is were we'll find the rest of the pages (this is how streamlit is able to know there is multiple pages).
        1_PixelsInput is the second page were using the image uploaded before , we can click on it to then save the coordinates of that point. The idea is to register the image coordinates of the reference points input previously.

        2_Comparation is the third page that lets us compare the base image and its transformation.

        3_DistanceStimation is the final page and it first lets us calculate our scale factor by indicating in the image we used  a known distance as a reference, and then we can input another image (ideally another image taken by the same static camera with the same real world coordinate system) and measure the desired distance between 2 points.





