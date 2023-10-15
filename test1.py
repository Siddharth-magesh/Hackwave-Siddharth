def validate_text(val):
    if (val.lower() == 'emergency exit'):
        m1 = 'Go straight until you reach the Operation Theatre\nTake a left turn after passing the Operation Theatre\nContinue straight until you see the Emergency Exit'
        n1 = "images/hospital_elevator.jpeg"
        z1 = "images/hospital_img_zoom/hospital_emergency_in.jpeg"
        return (m1, n1, z1)
    elif (val.lower() == 'elevator'):
        m2 = 'Go straight until you reach the Operation Theatre\nTake a left turn after passing the Operation Theatre\n Continue straight until you see the Emergency Exit\nThe elevator is on your left'
        n2 = "images/hospital_elevator.jpeg"
        z2 = "images/hospital_img_zoom/hospital_elevator_in.jpeg"
        return (m2, n2, z2)
    elif (val.lower() == 'patient route'):
        m3 = 'The Patient room no 3 and 4 can seen\n on your right just after your entry\nThe Patient room no 1 and 2\n is on the opposite path to the  Patient room no 3'
        n3 = "images/hospital_patient_room.jpeg"
        z3 = "images/hospital_img_zoom/hospital_patient_room_in.jpeg"
        return (m3, n3, z3)
    elif (val.lower() == 'general doctor'):
        m4 = 'Go straight until you reach the Vip room 3\nTake a left turn after passing the VIP room\nGo Straight and Take a left\nThen your destination will be on your Left'
        n4 = "images/hospital_general_doc.jpeg"
        z4 = "images/hospital_img_zoom/hospital_general_doc_in.jpeg"
        return (m4, n4, z4)
    elif (val.lower() == 'mri'):
        m5 = 'Go Straight untill the Dental room\nThe MRI room is on your right'
        n5 = "images/hospital_mri_scan.jpeg"
        z5 = "images/hospital_img_zoom/hospital_mri_ Scan_in.jpeg"
        return (m5, n5, z5)
    elif (val.lower() == 'gynacolagist'):
        m6 = 'Go Straight\nTake a left turn\nThe Gynecologists room is on your right'
        n6 = "images/hospital_gynacologist.jpeg"
        z6 = "images/hospital_img_zoom/hospital_gynacologist_in.jpeg"
        return (m6, n6, z6)
    elif (val.lower() == 'reception'):
        m7 = 'Go straight until the Operation Theatre\nThe Reception is on your Left'
        n7 = "images/hospital_reception.jpeg"
        z7 = "images/hospital_img_zoom/hospital_reception_in.jpeg"
        return (m7, n7, z7)
    elif (val.lower() == 'vip patients'):
        m8 = 'From Entry take the \nthird and fourth right\n to enter VIP room no 3 \nand 4 Respectively\nFrom entry take the first left \nand walk toward the end of the corridor,\n you can see the VIP room 1 infront of you \nand VIP room 2 adjacent to it'
        n8 = "images/hospital_vip_patient_room.jpeg"
        z8 = "images/hospital_img_zoom/hospital_vip_patient_room_in.jpeg"
        return (m8, n8, z8)
    elif (val.lower() == 'operation theatre'):
        m9 = 'Go straight untill the Reception\nThe Operation Theatre is on your right'
        n9 = "images/hospital_operation_theatre.jpeg"
        z9 = "images/hospital_img_zoom/hospital_operation_theatre_in.jpeg"
        return (m9, n9, z9)
    else:
        return ("Invalid Desination")


def validate_text_university(val):
    if (val.lower() == 'emergency exit'):
        m1 = "First Emergency Exit\nStraight, 2 rights, left, continue past basketball court\nSecond Emergency Exit\nStraight, right, cross court, right after Auditorium, second Exit left"
        n1 = "images/university_img/university_emergency_exit.jpeg"
        z1 = "images/university_img_zoom/university_emergency_exit_in.jpeg"
        return (m1, n1, z1)
    elif (val.lower() == 'auditorium'):
        m2 = 'Go Straight\nTake Right\nWalk Straight\nTake right\nWalk straight and you will cross the basketball court\nWalk Straight and cross the main ingate\nYou have Reached the Auditorium'
        n2 = "images/university_img/university_auditorium.jpeg"
        z2 = "images/university_img_zoom/university_auditorium_in.jpeg"
        return (m2, n2, z2)
    elif (val.lower() == 'classes'):
        m3 = 'Go straight\nturn right\ncross basketball court\npass main gate\nright after Auditorium Door\nstraight to classrooms'
        n3 = "images/university_img/university_classes.jpeg"
        z3 = "images/university_img_zoom/university_classes_in.jpeg"
        return (m3, n3, z3)
    elif (val.lower() == 'library'):
        m4 = 'Go straight\nturn right\nwalk straight\nthen take a right\n opposite the toilet to reach the library'
        n4 = "images/university_img/university_library.jpeg"
        z4 = "images/university_img_zoom/university_library_in.jpeg"
        return (m4, n4, z4)
    elif (val.lower() == 'seminar hall'):
        m5 = 'Go straight\nturn right\nwalk straight\nthen take a right followed by a left after\nthe toilet to reach the seminar hall.'
        n5 = "images/university_img/university_seminar_hall.jpeg"
        z5 = "images/university_img_zoom/university_seminar_hall_in.jpeg"
        return (m5, n5, z5)
    elif (val.lower() == 'admin office'):
        m6 = 'Go straight\nright\nstraight\nright\nright\nstraight\nright\nAdmin Office reached.'
        n6 = "images/university_img/university_admin_office.jpeg"
        z6 = "images/university_img_zoom/university_admin_office_in.jpeg"
        return (m6, n6, z6)
    elif (val.lower() == 'toilets'):
        m7 = 'Go straight\nturn right\nwalk straight\nthen take a right and a left after \nthe teachers cabin to reach the toilet.'
        n7 = "images/university_img/university_toilets.jpeg"
        z7 = "images/university_img_zoom/university_toilets_in.jpeg"
        return (m7, n7, z7)
    elif (val.lower() == 'principal office'):
        m8 = 'take the first left and first right'
        n8 = "images/university_img/university_principal_office.jpeg"
        z8 = ""
        return (m8, n8, z8)
    elif (val.lower() == 'health center'):
        m9 = 'take two consequtive lefts and a right'
        n9 = "images/university_img/university_health_centre.jpg"
        z9 = ""
        return (m9, n9, z9)
    else:
        return ("Invalid Desination")


def validate_text_mall(val):
    if (val.lower() == 'emergency exit'):
        m1 = "Straight\nfirst left\nescalators ahead\nEmergency Exit right\nanother Exit across from elevators"
        n1 = "images/mall_img/mall_emergency_exit.jpeg"
        z1 = "images/mall_img_zoom/mall_emergency_exit_in.jpeg"
        return (m1, n1, z1)
    elif (val.lower() == 'elevator'):
        m2 = 'Go straight\ntake the first left\ncontinue until escalators\nturn right to find the rest area\nelevators are across from there.'
        n2 = "images/mall_img/mall_elevator.jpeg"
        z2 = "images/mall_img_zoom/mall_elevator_in.jpeg"
        return (m2, n2, z2)
    elif (val.lower() == 'rest area'):
        m3 = 'Go straight\nfirst left\ncontinue to escalators\nturn right\nresting area ahead'
        n3 = "images/mall_img/mall_rest_area.jpeg"
        z3 = "images/mall_img_zoom/mall_rest_area_in.jpeg"
        return (m3, n3, z3)
    elif (val.lower() == 'star bucks'):
        m4 = 'Go straight\n take the left near the escalator\ncontinue straight\nand Starbucks will be on your right'
        n4 = "images/mall_img/mall_starbucks.jpeg"
        z4 = "images/mall_img_zoom/mall_starbucks_in.jpeg"
        return (m4, n4, z4)
    elif (val.lower() == 'toilets'):
        m5 = 'Go straight\ntoilet on right across escalators\nalternatively\ntake left by escalator\ngo straight\nturn right\ntoilet ahead'
        n5 = "images/mall_img/mall_toilets.jpeg"
        z5 = "images/mall_img_zoom/mall_toilets_In.jpeg"
        return (m5, n5, z5)
    elif (val.lower() == 'west side'):
        m6 = 'Go straight\nThe WestSide is on your Right across the Rest area'
        n6 = "images/mall_img/mall_westside.jpeg"
        z6 = "images/mall_img_zoom/mall_westside_in.jpeg"
        return (m6, n6, z6)
    elif (val.lower() == 'h and m'):
        m7 = 'Go straight\nfirst left\ncontinue to rest area\nright across elevators\nright by toilet\nits on your left'
        n7 = "images/mall_img/mall_h&m.jpeg"
        z7 = "images/mall_img_zoom/mall_h&m_in.jpeg"
        return (m7, n7, z7)
    elif (val.lower() == 'wildcraft'):
        m8 = 'Go straight\nleft by escalator\nnext right\ncontinue\nWildcraft on your right'
        n8 = "images/mall_img/mall_wildcraft.jpeg"
        z8 = "images/mall_img_zoom/mall_wildcraft_in.jpeg"
        return (m8, n8, z8)
    elif (val.lower() == 'nike'):
        m9 = 'Go straight\nfirst left\ncontinue to rest area\nright across elevators\nright by toilet\nits on your right'
        n9 = "images/mall_img/mall_nike.jpeg"
        z9 = "images/mall_img_zoom/mall_nike_in.jpeg"
        return (m9, n9, z9)
    else:
        return ("Invalid Desination")
