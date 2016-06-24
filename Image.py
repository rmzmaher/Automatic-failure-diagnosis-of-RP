#!/usr/local/bin/python

import cv2
import numpy

class Image:

        def findDescriptor(self,img):
                """ findDescriptor(img) finds and returns the
                Fourier-Descriptor of the image contour"""
                im = cv2.imread(img)
                #preprocessing
                #ret, = cv2.threshold(im,127,255,cv2.THRESH_BINARY)
                edges=cv2.Canny(im,100,1000)
                contour = []
                contour, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE,contour)
                #check
                cv2.drawContours(im, contour[-1], -1 , (0,255,0), 3)
                cv2.imshow("black", im)
                cv2.waitKey()
                #contour_array
                contour_array = contour[-1][:, 0, :]
                contour_complex = numpy.empty(contour_array.shape[:-1], dtype=complex)
                contour_complex.real = contour_array[:, 0]
                contour_complex.imag = contour_array[:, 1]
                fourier_result = numpy.fft.fft(contour_complex)
                return fourier_result
        
        
        def truncate_descriptor(self,descriptors, degree):
                """this function truncates an unshifted fourier descriptor array
                and returns one also unshifted"""
                descriptors = numpy.fft.fftshift(descriptors)
                center_index = len(descriptors) / 2
                descriptors = descriptors[center_index - degree / 2:center_index + degree / 2]
                descriptors = numpy.fft.ifftshift(descriptors)
                return descriptors
        
        def reconstruct(self,descriptors):
            """ reconstruct(descriptors, degree) attempts to reconstruct the image
            using the first [degree] descriptors of descriptors"""
            # truncate the long list of descriptors to certain length
            contour_reconstruct = numpy.fft.ifft(descriptors)
            contour_reconstruct = numpy.array(
                [contour_reconstruct.real, contour_reconstruct.imag])
            contour_reconstruct = numpy.transpose(contour_reconstruct)
            contour_reconstruct = numpy.expand_dims(contour_reconstruct, axis=1)
            # make positive
            if contour_reconstruct.min() < 0:
                contour_reconstruct -= contour_reconstruct.min()
            # normalization
            contour_reconstruct *= 800 / contour_reconstruct.max()
            # type cast to int32
            contour_reconstruct = contour_reconstruct.astype(numpy.int32, copy=False)
            black = numpy.zeros((2000, 2000), numpy.uint8)
            # draw and visualize
            cv2.drawContours(black, contour_reconstruct, -1, 255, thickness=-1)
            cv2.imshow("black", black)
            cv2.waitKey()
            cv2.imwrite("reconstruct_result.jpg", black)
            cv2.destroyAllWindows()
            return descriptors

        def addNoise(self,descriptors):
            """this function adds gaussian noise to descriptors
            descriptors should be a [N,2] numpy array"""
            scale = descriptors.max() / 10
            noise = numpy.random.normal(0, scale, descriptors.shape[0])
            # 0 is the mean of the normal distribution you are choosing from
            # scale is the standard deviation of the normal distribution
            #  the number of elements you get in array noise
            noise = noise + 1j * noise
            descriptors += noise
