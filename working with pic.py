import cv2
img = cv2.imread('week maze.png')



# put text
text_list = [
' number 1 ' ,
' number 2 ' ,
' number 3 ' ,
' number 4 ' ,
' number 5 ' ,
' number 6 ' ,
' number 7 ' ,
' number 8 ' ,
' number 9 ' ,
' number 10 ' ,
' number 11 ' ,
' number 12 ' ,
' number 13 ' ,
' number 14 ' ,
' number 15 ' ,
' number 16 ' ,
' number 17 ' ,
' number 18 ' ,
' number 19 ' ,
' number 20 ' ,
' number 21 ' ,
' number 22 ' ,
' number 23 ' ,
' number 24 ' ,
' number 25 ' ,
' number 26 ' ,
' number 27 ' ,
' number 28 ' ,
' number 29 ' ,
' number 30 ' ,
' number 31 ' ,
' number 32 ' ,
' number 33 ' ,
' number 34 ' ,
' number 35 ' ,
' number 36 ' ,
' number 37 ' ,
' number 38 ' ,
' number 39 ' ,
' number 40 ' ,
' number 41 ' ,
' number 42 ' ,
' number 43 ' ,
' number 44 ' ,
' number 45 ' ,
' number 46 ' ,
' number 47 ' ,
' number 48 ' ,
' number 49 ' ,
' number 50 ' ,
' number 51 ' ,
' number 52 ' ,
' number 53 ' ,
' number 54 ' ,
' number 55 ' ,
' number 56 ' ,
' number 57 ' ,
' number 58 ' ,
' number 59 ' ]


def put_text(text_list,img):
    #situations
    #--
    situation_one = [1,3,5,7,8,9,10,11,13,15,17,18,19,30,31,32,34,36,38,39,40,41,42,44,46,48]
    coordinates_situation_one = [(590,1093),(482,1092),(376,1093),(272,1092),(163,1096),(33,1095),(30,945),(33,829),(33,723),(33,617),(33,510),(33,403),(33,263),(740,882),(740,729),(740,619),(740,512),(740,403),(740,299),(740,194),(730,57),(588,57),(482,57),(374,57),(269,57),(162,57)]


    #-
    situation_one_small = [12,14,16,23,24,25,26,33,35,37]
    coordinates_situation_one_small = [(219,804),(218,698),(218,591),(541,430),(542,537),(198,645),(202,750),(523,591),(521,485),(525,375)]

    # |
    situation_four = [2,4,6,20,21,22,27,28,29,43,45,47]
    coordinates_situation_four = [(235,578),(235,472),(233,366),(873,206),(873,312),(874,419),(221,423),(223,527),(223,637),(865,474),(867,366),(865,257)]

    a=0
    b=0
    c=0
    situation_check = 0
    for text in text_list:
        situation_check = situation_check + 1
        
        
        if situation_check in situation_one:
            cv2.putText(img,text,coordinates_situation_one[a],cv2.FONT_HERSHEY_DUPLEX, 0.5 , (0,0,0),1)
            a = a+1
        if situation_check in situation_one_small:
            cv2.putText(img,text,coordinates_situation_one_small[b],cv2.FONT_HERSHEY_DUPLEX, 0.5 , (0,0,0),1)
            b = b+1
    #############################
        #if situation_check in situation_two:
            #img = cv2.rotate(img, cv2.rotate(45))
            #cv2.putText(img,text,place,cv2.FONT_HERSHEY_COMPLEX, 0.95 , (0,0,0),2)
            #img = cv2.rotate(img, cv2.ROTATE_315)


        #if situation_check in situation_three:
            #img = cv2.rotate(img, cv2.ROTATE_315)
            #cv2.putText(img,text,place,cv2.FONT_HERSHEY_COMPLEX, 0.95 , (0,0,0),2)
            #img = cv2.rotate(img, cv2.ROTATE_45)

    ############################
        if situation_check in situation_four:
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            cv2.putText(img,text,coordinates_situation_four[c],cv2.FONT_HERSHEY_DUPLEX, 0.5 , (0,0,0),1)
            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            c = c+1
    return img
def show_img(img):
    cv2.imshow('my image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite('new img.png', img)
    return


img = put_text(text_list,img) 
show_img(img)