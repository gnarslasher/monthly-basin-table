import xml.dom.minidom as minidom
import requests
import statistics
import pandas as pd
from datetime import date


def build_table():

    today = date.today()

    month_input = today.strftime('%m')
    year_input = today.strftime('%Y')

    reservoir_triplets = [
        '06216400:WY:BOR',
        '06224500:WY:BOR',
        '06258900:WY:BOR',
        '06281500:WY:BOR',
        '06110500:MT:BOR',
        '12367000:MT:BOR',
        '06116500:MT:BOR',
        '06140300:MT:BOR',
        '06286400:MT:BOR',
        '12375600:MT:BOR',
        '06058500:MT:BOR',
        '06015300:MT:BOR',
        '06212000:MT:BOR',
        '06122500:MT:BOR',
        '12332500:MT:BOR',
        '06040500:MT:BOR',
        '12371550:MT:BOR',
        '06131500:MT:BOR',
        '06093000:MT:BOR',
        '06136500:MT:BOR',
        '12325000:MT:BOR',
        '06079500:MT:BOR',
        '06065100:MT:BOR',
        '06038000:MT:BOR',
        '06058600:MT:BOR',
        '06066000:MT:BOR',
        '12362000:MT:BOR',
        '12344500:MT:BOR',
        '06101300:MT:BOR',
        '06095500:MT:BOR',
        '06064500:MT:BOR',
        '12301920:MT:BOR',
        '05015500:MT:BOR',
        '06012000:MT:BOR',
        '12380500:MT:BOR',
        '06090900:MT:BOR',
        '12330800:MT:BOR',
        '06119000:MT:BOR',
        '06049500:MT:BOR',
        '12380100:MT:BOR',
        '06204000:MT:BOR',
        '06155000:MT:BOR',
        '12336500:MT:BOR',
        '06763100:MT:BOR',
        '06083000:MT:BOR',
        '12391300:MT:BOR',
        '12342000:MT:BOR',
        '06080500:MT:BOR',
        '06020500:MT:BOR',
        '12323700:MT:BOR',
        '06075000:MT:BOR',
        '06094000:MT:BOR',
        '12390000:MT:BOR',
        '06307000:MT:BOR',
        '06036000:MT:BOR',
        '06082000:MT:BOR',
    ]
    swe_triplets = [
        '307:MT:SNTL',
        '309:WY:SNTL',
        '311:MT:SNTL',
        '313:MT:SNTL',
        '315:MT:SNTL',
        '318:MT:SNTL',
        '323:ID:SNTL',
        '325:WY:SNTL',
        '326:WY:SNTL',
        '328:MT:SNTL',
        '346:MT:SNTL',
        '347:MT:SNTL',
        '349:MT:SNTL',
        '350:WY:SNTL',
        '354:SD:SNTL',
        '355:MT:SNTL',
        '358:WY:SNTL',
        '360:MT:SNTL',
        '363:MT:SNTL',
        '365:MT:SNTL',
        '377:WY:SNTL',
        '379:WY:SNTL',
        '381:MT:SNTL',
        '384:WY:SNTL',
        '385:MT:SNTL',
        '402:WY:SNTL',
        '403:MT:SNTL',
        '405:WY:SNTL',
        '407:MT:SNTL',
        '410:MT:SNTL',
        '413:MT:SNTL',
        '414:MT:SNTL',
        '427:MT:SNTL',
        '433:MT:SNTL',
        '436:MT:SNTL',
        '437:MT:SNTL',
        '448:MT:SNTL',
        '451:WY:SNTL',
        '458:MT:SNTL',
        '469:MT:SNTL',
        '472:WY:SNTL',
        '480:MT:SNTL',
        '482:MT:SNTL',
        '487:MT:SNTL',
        '500:MT:SNTL',
        '501:WY:SNTL',
        '510:MT:SNTL',
        '512:WY:SNTL',
        '516:MT:SNTL',
        '525:WY:SNTL',
        '530:MT:SNTL',
        '535:ID:SNTL',
        '560:WY:SNTL',
        '562:MT:SNTL',
        '568:MT:SNTL',
        '576:MT:SNTL',
        '578:MT:SNTL',
        '585:WY:SNTL',
        '588:ID:SNTL',
        '590:MT:SNTL',
        '594:ID:SNTL',
        '603:MT:SNTL',
        '604:MT:SNTL',
        '609:MT:SNTL',
        '613:MT:SNTL',
        '616:WY:SNTL',
        '625:WY:SNTL',
        '635:MT:SNTL',
        '638:ID:SNTL',
        '646:MT:SNTL',
        '649:MT:SNTL',
        '656:MT:SNTL',
        '657:MT:SNTL',
        '662:MT:SNTL',
        '664:MT:SNTL',
        '667:MT:SNTL',
        '670:MT:SNTL',
        '676:WY:SNTL',
        '683:WY:SNTL',
        '690:MT:SNTL',
        '693:MT:SNTL',
        '696:MT:SNTL',
        '700:MT:SNTL',
        '703:WY:SNTL',
        '722:MT:SNTL',
        '725:MT:SNTL',
        '727:MT:SNTL',
        '751:WY:SNTL',
        '753:MT:SNTL',
        '754:MT:SNTL',
        '760:MT:SNTL',
        '775:WY:SNTL',
        '781:MT:SNTL',
        '783:MT:SNTL',
        '786:WY:SNTL',
        '787:MT:SNTL',
        '798:WY:SNTL',
        '806:WY:SNTL',
        '807:WY:SNTL',
        '813:MT:SNTL',
        '816:WY:SNTL',
        '818:WY:SNTL',
        '819:WY:SNTL',
        '822:WY:SNTL',
        '826:WY:SNTL',
        '835:MT:SNTL',
        '836:MT:SNTL',
        '837:WY:SNTL',
        '847:MT:SNTL',
        '850:MT:SNTL',
        '858:MT:SNTL',
        '860:ID:SNTL',
        '862:MT:SNTL',
        '875:WY:SNTL',
        '876:MT:SNTL',
        '878:WY:SNTL',
        '893:MT:SNTL',
        '901:MT:SNTL',
        '903:MT:SNTL',
        '916:MT:SNTL',
        '917:MT:SNTL',
        '918:MT:SNTL',
        '919:MT:SNTL',
        '920:SD:SNTL',
        '923:WY:SNTL',
        '924:MT:SNTL',
        '929:MT:SNTL',
        '930:MT:SNTL',
        '931:WY:SNTL',
        '932:MT:SNTL',
        '981:MT:SNTL',
        '982:WY:SNTL',
        '1008:MT:SNTL',
        '1009:MT:SNTL',
        '1105:MT:SNTL',
        '1106:MT:SNTL',
        '1130:WY:SNTL',
        '1131:WY:SNTL',
        '1132:WY:SNTL',
        '1144:MT:SNTL',
        '1287:MT:SNTL',
        '09D17:MT:SNOW',
        '12B07:MT:SNOW',
        '13E22:MT:SNOW',
        '13C16:MT:SNOW',
        '15A09:MT:SNOW',
        '14Z07:AB:SNOW',
        '14Z07S:AB:SNOW',
        '14Z03:AB:SNOW',
        '16X01:AB:SNOW',
        '16X13:AB:SNOW',
        '16X08:AB:SNOW',
        '15X04:AB:SNOW',
        '15X05:AB:SNOW',
        '14Z10:AB:SNOW',
        '10Z04:AB:SNOW',
        '10Z05:AB:SNOW',
        '14Y05:AB:SNOW',
        '16X16:AB:SNOW',
        '16X14:AB:SNOW',
        '13Z08:AB:SNOW',
        '14Y20:AB:SNOW',
        '14Y18:AB:SNOW',
        '18W02:AB:SNOW',
        '16X17:AB:SNOW',
        '16X06:AB:SNOW',
        '14Y07:AB:SNOW',
        '10Z06:AB:SNOW',
        '10Z07:AB:SNOW',
        '15Y02:AB:SNOW',
        '17W02:AB:SNOW',
        '16X02:AB:SNOW',
        '16X09:AB:SNOW',
        '10Z08:AB:SNOW',
        '10Z09:AB:SNOW',
        '16X15:AB:SNOW',
        '15X03:AB:SNOW',
        '17W01:AB:SNOW',
        '15Y24:AB:SNOW',
        '15Y03:AB:SNOW',
        '14Z01:AB:SNOW',
        '14Y09:AB:SNOW',
        '14Y08:AB:SNOW',
        '13E19:ID:SNOW',
        '15B07:ID:SNOW',
        '11G35:ID:SNOW',
        '15F02:ID:SNOW',
        '14G03:ID:SNOW',
        '16G09:ID:SNOW',
        '16A02:ID:SNOW',
        '16A03:ID:SNOW',
        '11E09:ID:SNOW',
        '11F17:ID:SNOW',
        '16F02:ID:SNOW',
        '16F04:ID:SNOW',
        '11F08:ID:SNOW',
        '13G02:ID:SNOW',
        '14E08:ID:SNOW',
        '16G10:ID:SNOW',
        '12E03:ID:SNOW',
        '15F15:ID:SNOW',
        '13E17:ID:SNOW',
        '13F02:ID:SNOW',
        '14F18:ID:SNOW',
        '14D06:ID:SNOW',
        '14C11:ID:SNOW',
        '12G12:ID:SNOW',
        '16F01:ID:SNOW',
        '16F13:ID:SNOW',
        '16F12:ID:SNOW',
        '16E15:ID:SNOW',
        '11G14:ID:SNOW',
        '13F20:ID:SNOW',
        '11G34:ID:SNOW',
        '11G07:ID:SNOW',
        '11F19:ID:SNOW',
        '15C02:ID:SNOW',
        '16B03:ID:SNOW',
        '13E29:ID:SNOW',
        '13F10:ID:SNOW',
        '12E04:ID:SNOW',
        '13E28:ID:SNOW',
        '12G22:ID:SNOW',
        '11G36:ID:SNOW',
        '16B05:ID:SNOW',
        '14F21:ID:SNOW',
        '11E12:ID:SNOW',
        '15E01:ID:SNOW',
        '14G08:ID:SNOW',
        '11E16:ID:SNOW',
        '11F15:ID:SNOW',
        '15F12:ID:SNOW',
        '13G03:ID:SNOW',
        '12G06:ID:SNOW',
        '16B13:ID:SNOW',
        '11E14:ID:SNOW',
        '16E20:ID:SNOW',
        '11F12:ID:SNOW',
        '16E19:ID:SNOW',
        '15F01:ID:SNOW',
        '13E26:ID:SNOW',
        '14F09:ID:SNOW',
        '11F14:ID:SNOW',
        '14F20:ID:SNOW',
        '13F05:ID:SNOW',
        '16E17:ID:SNOW',
        '11F18:ID:SNOW',
        '12G02:ID:SNOW',
        '14D05:ID:SNOW',
        '16E02:ID:SNOW',
        '17B06:ID:SNOW',
        '15F19:ID:SNOW',
        '16G11:ID:SNOW',
        '16F08:ID:SNOW',
        '16F10:ID:SNOW',
        '16F09:ID:SNOW',
        '16F11:ID:SNOW',
        '15B05:ID:SNOW',
        '16A11:ID:SNOW',
        '16E16:ID:SNOW',
        '16B11:ID:SNOW',
        '13E30:ID:SNOW',
        '15D02:ID:SNOW',
        '11F01:ID:SNOW',
        '11G09:ID:SNOW',
        '12G08:ID:SNOW',
        '16F06:ID:SNOW',
        '13F06:ID:SNOW',
        '17E06:ID:SNOW',
        '15F20:ID:SNOW',
        '16E03:ID:SNOW',
        '16B12:ID:SNOW',
        '12G10:ID:SNOW',
        '11G26:ID:SNOW',
        '11E08:ID:SNOW',
        '16G12:ID:SNOW',
        '16C21:ID:SNOW',
        '12E05:ID:SNOW',
        '11G04:ID:SNOW',
        '11G28:ID:SNOW',
        '10D14:MT:SNOW',
        '14A19:MT:SNOW',
        '15B11:MT:SNOW',
        '15B16:MT:SNOW',
        '15B15:MT:SNOW',
        '12D09:MT:SNOW',
        '14B03:MT:SNOW',
        '11D09:MT:SNOW',
        '09C05:MT:SNOW',
        '12C19:MT:SNOW',
        '14B04:MT:SNOW',
        '09D14:MT:SNOW',
        '09A08:MT:SNOW',
        '11D14:MT:SNOW',
        '15A10:MT:SNOW',
        '14A13:MT:SNOW',
        '12D08:MT:SNOW',
        '12B06:MT:SNOW',
        '09D01:MT:SNOW',
        '11E29:MT:SNOW',
        '12C05:MT:SNOW',
        '15B22:MT:SNOW',
        '14A15:MT:SNOW',
        '10D30:MT:SNOW',
        '12C09:MT:SNOW',
        '12C17:MT:SNOW',
        '13B10:MT:SNOW',
        '10D05:MT:SNOW',
        '13A02:MT:SNOW',
        '13C42:MT:SNOW',
        '12C15:MT:SNOW',
        '10C13:MT:SNOW',
        '13D01:MT:SNOW',
        '13C09:MT:SNOW',
        '13D15:MT:SNOW',
        '10C07:MT:SNOW',
        '13B04:MT:SNOW',
        '12D10:MT:SNOW',
        '12B09:MT:SNOW',
        '13A19:MT:SNOW',
        '12D07:MT:SNOW',
        '13D21:MT:SNOW',
        '10C14:MT:SNOW',
        '11D12:MT:SNOW',
        '12A01:MT:SNOW',
        '13D02:MT:SNOW',
        '13D09:MT:SNOW',
        '15B23:MT:SNOW',
        '10C02:MT:SNOW',
        '14A09:MT:SNOW',
        '10C11:MT:SNOW',
        '11E05:MT:SNOW',
        '14A03:MT:SNOW',
        '14A16:MT:SNOW',
        '10B02:MT:SNOW',
        '10B01:MT:SNOW',
        '13B13:MT:SNOW',
        '13A03:MT:SNOW',
        '13C04:MT:SNOW',
        '13D27:MT:SNOW',
        '10C12:MT:SNOW',
        '13A14:MT:SNOW',
        '10C01:MT:SNOW',
        '14A06:MT:SNOW',
        '11E04:MT:SNOW',
        '11D10:MT:SNOW',
        '14A05:MT:SNOW',
        '13C21:MT:SNOW',
        '13C22:MT:SNOW',
        '13C08:MT:SNOW',
        '13C37:MT:SNOW',
        '13A05:MT:SNOW',
        '11D15:MT:SNOW',
        '10D19:MT:SNOW',
        '13A16:MT:SNOW',
        '12C20:MT:SNOW',
        '13A07:MT:SNOW',
        '13D25:MT:SNOW',
        '10D01:MT:SNOW',
        '14D02:MT:SNOW',
        '12C10:MT:SNOW',
        '14D01:MT:SNOW',
        '13B07:MT:SNOW',
        '12C16:MT:SNOW',
        '09D13:MT:SNOW',
        '09D12:MT:SNOW',
        '10D28:MT:SNOW',
        '13A06:MT:SNOW',
        '12D01:MT:SNOW',
        '11E21:MT:SNOW',
        '13A08:MT:SNOW',
        '15A01:MT:SNOW',
        '14B06:MT:SNOW',
        '15B24:MT:SNOW',
        '11D21:MT:SNOW',
        '09A01:MT:SNOW',
        '13D24:MT:SNOW',
        '13C02:MT:SNOW',
        '12D05:MT:SNOW',
        '13B02:MT:SNOW',
        '12C01:MT:SNOW',
        '13C07:MT:SNOW',
        '14A17:MT:SNOW',
        '09A07:MT:SNOW',
        '12C02:MT:SNOW',
        '12C03:MT:SNOW',
        '09D04:MT:SNOW',
        '13B01:MT:SNOW',
        '14A18:MT:SNOW',
        '11E06:MT:SNOW',
        '13B05:MT:SNOW',
        '14A07:MT:SNOW',
        '11E07:MT:SNOW',
        '12B04:MT:SNOW',
        '12B03:MT:SNOW',
        '03F04:SD:SNOW',
        '03E01:SD:SNOW',
        '06H11:WY:SNOW',
        '10E08:WY:SNOW',
        '10F02:WY:SNOW',
        '04E02:WY:SNOW',
        '10G11:WY:SNOW',
        '08G02:WY:SNOW',
        '09F20:WY:SNOW',
        '10G07:WY:SNOW',
        '10F21:WY:SNOW',
        '06H17:WY:SNOW',
        '09F06:WY:SNOW',
        '10F28:WY:SNOW',
        '10F06:WY:SNOW',
        '06H24:WY:SNOW',
        '06H12:WY:SNOW',
        '09F07:WY:SNOW',
        '10E13:WY:SNOW',
        '08G04:WY:SNOW',
        '10E15:WY:SNOW',
        '10G03:WY:SNOW',
        '06H02:WY:SNOW',
        '07H01:WY:SNOW',
        '10F30:WY:SNOW',
        '10E14:WY:SNOW',
        '10F26:WY:SNOW',
        '10E04:WY:SNOW',
        '09G06:WY:SNOW',
        '10E09:WY:SNOW',
        '06H03:WY:SNOW',
        '04F01:WY:SNOW',
        '10E01:WY:SNOW',
        '04E05:WY:SNOW',
        '07E24:WY:SNOW',
        '08G06:WY:SNOW',
        '10F04:WY:SNOW',
        '06H16:WY:SNOW',
        '06H26:WY:SNOW',
        '04E04:WY:SNOW',
        '10E19:WY:SNOW',
        '06H05:WY:SNOW',
        '07E15:WY:SNOW',
        '10E18:WY:SNOW',
        '07E27:WY:SNOW',
        '09G11:WY:SNOW',
        '05H01:WY:SNOW',
        '06H18:WY:SNOW',
        '07E04:WY:SNOW',
        '04E03:WY:SNOW',
        '10G21:WY:SNOW',
        '06H06:WY:SNOW',
        '07E38:WY:SNOW',
        '09F15:WY:SNOW',
        '10E12:WY:SNOW',
        '10F20:WY:SNOW',
        '07E05:WY:SNOW',
        '06E01:WY:SNOW',
        '09F03:WY:SNOW',
        '10F24:WY:SNOW',
        '10E07:WY:SNOW',
        '10F09:WY:SNOW',
        '10F05:WY:SNOW',
        '07E35:WY:SNOW',
        '07E13:WY:SNOW',
    ]
    pcp_triplets = [
        '1165:MT:SNTLT',
        '1190:MT:SNTLT',
        '309:WY:SNTL',
        '325:WY:SNTL',
        '326:WY:SNTL',
        '931:WY:SNTL',
        '350:WY:SNTL',
        '358:WY:SNTL',
        '377:WY:SNTL',
        '379:WY:SNTL',
        '384:WY:SNTL',
        '1130:WY:SNTL',
        '402:WY:SNTL',
        '405:WY:SNTL',
        '923:WY:SNTL',
        '451:WY:SNTL',
        '472:WY:SNTL',
        '501:WY:SNTL',
        '512:WY:SNTL',
        '525:WY:SNTL',
        '560:WY:SNTL',
        '1131:WY:SNTL',
        '1047:WY:SNTL',
        '585:WY:SNTL',
        '616:WY:SNTL',
        '625:WY:SNTL',
        '676:WY:SNTL',
        '683:WY:SNTL',
        '703:WY:SNTL',
        '751:WY:SNTL',
        '1132:WY:SNTL',
        '775:WY:SNTL',
        '786:WY:SNTL',
        '798:WY:SNTL',
        '806:WY:SNTL',
        '807:WY:SNTL',
        '816:WY:SNTL',
        '818:WY:SNTL',
        '819:WY:SNTL',
        '822:WY:SNTL',
        '826:WY:SNTL',
        '837:WY:SNTL',
        '868:WY:SNTL',
        '875:WY:SNTL',
        '878:WY:SNTL',
        '916:MT:SNTL',
        '307:MT:SNTL',
        '311:MT:SNTL',
        '313:MT:SNTL',
        '315:MT:SNTL',
        '318:MT:SNTL',
        '328:MT:SNTL',
        '346:MT:SNTL',
        '347:MT:SNTL',
        '349:MT:SNTL',
        '1144:MT:SNTL',
        '355:MT:SNTL',
        '360:MT:SNTL',
        '363:MT:SNTL',
        '365:MT:SNTL',
        '981:MT:SNTL',
        '381:MT:SNTL',
        '385:MT:SNTL',
        '403:MT:SNTL',
        '407:MT:SNTL',
        '410:MT:SNTL',
        '413:MT:SNTL',
        '414:MT:SNTL',
        '427:MT:SNTL',
        '919:MT:SNTL',
        '433:MT:SNTL',
        '436:MT:SNTL',
        '437:MT:SNTL',
        '448:MT:SNTL',
        '458:MT:SNTL',
        '1105:MT:SNTL',
        '1106:MT:SNTL',
        '469:MT:SNTL',
        '480:MT:SNTL',
        '482:MT:SNTL',
        '487:MT:SNTL',
        '918:MT:SNTL',
        '500:MT:SNTL',
        '510:MT:SNTL',
        '516:MT:SNTL',
        '530:MT:SNTL',
        '562:MT:SNTL',
        '568:MT:SNTL',
        '576:MT:SNTL',
        '578:MT:SNTL',
        '590:MT:SNTL',
        '603:MT:SNTL',
        '604:MT:SNTL',
        '609:MT:SNTL',
        '613:MT:SNTL',
        '635:MT:SNTL',
        '646:MT:SNTL',
        '649:MT:SNTL',
        '656:MT:SNTL',
        '657:MT:SNTL',
        '903:MT:SNTL',
        '662:MT:SNTL',
        '664:MT:SNTL',
        '667:MT:SNTL',
        '670:MT:SNTL',
        '1008:MT:SNTL',
        '930:MT:SNTL',
        '690:MT:SNTL',
        '693:MT:SNTL',
        '696:MT:SNTL',
        '932:MT:SNTL',
        '700:MT:SNTL',
        '722:MT:SNTL',
        '917:MT:SNTL',
        '725:MT:SNTL',
        '929:MT:SNTL',
        '727:MT:SNTL',
        '753:MT:SNTL',
        '754:MT:SNTL',
        '760:MT:SNTL',
        '783:MT:SNTL',
        '781:MT:SNTL',
        '787:MT:SNTL',
        '1009:MT:SNTL',
        '901:MT:SNTL',
        '813:MT:SNTL',
        '893:MT:SNTL',
        '835:MT:SNTL',
        '836:MT:SNTL',
        '847:MT:SNTL',
        '850:MT:SNTL',
        '924:MT:SNTL',
        '858:MT:SNTL',
        '862:MT:SNTL',
        '876:MT:SNTL',
        '323:ID:SNTL',
        '535:ID:SNTL',
        '588:ID:SNTL',
        '594:ID:SNTL',
        '638:ID:SNTL',
        '1081:ID:SNTL',
        '860:ID:SNTL',
        'TU02:MT:MPRC',
        'TU08:MT:MPRC',
        'ML15:MT:MPRC',
        'ML14:MT:MPRC',
        'MB02:MT:MPRC',
        'MB01:MT:MPRC',
        'TT01:MT:MPRC',
        'TU07:MT:MPRC',
        '0540:WY:COOP',
        '0680:WY:COOP',
        '0740:WY:COOP',
        '0778:WY:COOP',
        '1000:WY:COOP',
        '1165:WY:COOP',
        '1175:WY:COOP',
        '1284:WY:COOP',
        '1775:WY:COOP',
        '1816:WY:COOP',
        '1840:WY:COOP',
        '1905:WY:COOP',
        '2399:WY:COOP',
        '2415:WY:COOP',
        '2595:WY:COOP',
        '2715:WY:COOP',
        '3031:WY:COOP',
        '4080:WY:COOP',
        '5055:WY:COOP',
        '5345:WY:COOP',
        '5390:WY:COOP',
        '5506:WY:COOP',
        '5770:WY:COOP',
        '6195:WY:COOP',
        '6845:WY:COOP',
        '7115:WY:COOP',
        '7376:WY:COOP',
        '7388:WY:COOP',
        '7760:WY:COOP',
        '8124:WY:COOP',
        '8160:WY:COOP',
        '8155:WY:COOP',
        '8209:WY:COOP',
        '8626:WY:COOP',
        '8758:WY:COOP',
        '8852:WY:COOP',
        '8875:WY:COOP',
        '9025:WY:COOP',
        '9785:WY:COOP',
        '9905:WY:COOP',
        '5870:SD:COOP',
        '0088:MT:COOP',
        '0110:MT:COOP',
        '0199:MT:COOP',
        '0375:MT:COOP',
        '0392:MT:COOP',
        '0412:MT:COOP',
        '0622:MT:COOP',
        '0636:MT:COOP',
        '0739:MT:COOP',
        '0743:MT:COOP',
        '0770:MT:COOP',
        '0775:MT:COOP',
        '0780:MT:COOP',
        '0755:MT:COOP',
        '0807:MT:COOP',
        '0923:MT:COOP',
        '1008:MT:COOP',
        '1047:MT:COOP',
        '1044:MT:COOP',
        '1081:MT:COOP',
        '1084:MT:COOP',
        '1088:MT:COOP',
        '1102:MT:COOP',
        '1127:MT:COOP',
        '1231:MT:COOP',
        '1297:MT:COOP',
        '1318:MT:COOP',
        '1525:MT:COOP',
        '1557:MT:COOP',
        '1552:MT:COOP',
        '1692:MT:COOP',
        '1722:MT:COOP',
        '1737:MT:COOP',
        '1758:MT:COOP',
        '1875:MT:COOP',
        '1905:MT:COOP',
        '1938:MT:COOP',
        '1974:MT:COOP',
        '1984:MT:COOP',
        '1995:MT:COOP',
        '2122:MT:COOP',
        '2173:MT:COOP',
        '2221:MT:COOP',
        '2275:MT:COOP',
        '2301:MT:COOP',
        '2347:MT:COOP',
        '2409:MT:COOP',
        '2421:MT:COOP',
        '2438:MT:COOP',
        '2500:MT:COOP',
        '2629:MT:COOP',
        '2689:MT:COOP',
        '2793:MT:COOP',
        '2820:MT:COOP',
        '2827:MT:COOP',
        '2857:MT:COOP',
        '2996:MT:COOP',
        '3013:MT:COOP',
        '3098:MT:COOP',
        '3110:MT:COOP',
        '3113:MT:COOP',
        '3176:MT:COOP',
        '3139:MT:COOP',
        '3366:MT:COOP',
        '3378:MT:COOP',
        '3489:MT:COOP',
        '3558:MT:COOP',
        '3570:MT:COOP',
        '3581:MT:COOP',
        '3617:MT:COOP',
        '3707:MT:COOP',
        '3727:MT:COOP',
        '3751:MT:COOP',
        '3530:MT:COOP',
        '3885:MT:COOP',
        '3915:MT:COOP',
        '3929:MT:COOP',
        '3939:MT:COOP',
        '3996:MT:COOP',
        '4038:MT:COOP',
        '4055:MT:COOP',
        '4084:MT:COOP',
        '4133:MT:COOP',
        '4174:MT:COOP',
        '4241:MT:COOP',
        '4328:MT:COOP',
        '4358:MT:COOP',
        '4364:MT:COOP',
        '4447:MT:COOP',
        '4506:MT:COOP',
        '4512:MT:COOP',
        '4522:MT:COOP',
        '4538:MT:COOP',
        '4545:MT:COOP',
        '4558:MT:COOP',
        '4715:MT:COOP',
        '4766:MT:COOP',
        '4820:MT:COOP',
        '4954:MT:COOP',
        '4978:MT:COOP',
        '4985:MT:COOP',
        '5015:MT:COOP',
        '5020:MT:COOP',
        '5030:MT:COOP',
        '5040:MT:COOP',
        '5045:MT:COOP',
        '5080:MT:COOP',
        '5086:MT:COOP',
        '5153:MT:COOP',
        '5338:MT:COOP',
        '5387:MT:COOP',
        '5572:MT:COOP',
        '5596:MT:COOP',
        '5603:MT:COOP',
        '5608:MT:COOP',
        '5668:MT:COOP',
        '5690:MT:COOP',
        '5712:MT:COOP',
        '5745:MT:COOP',
        '5754:MT:COOP',
        '5761:MT:COOP',
        '5870:MT:COOP',
        '5872:MT:COOP',
        '5961:MT:COOP',
        '6008:MT:COOP',
        '6157:MT:COOP',
        '6190:MT:COOP',
        '6236:MT:COOP',
        '6238:MT:COOP',
        '6304:MT:COOP',
        '6472:MT:COOP',
        '6586:MT:COOP',
        '6601:MT:COOP',
        '6615:MT:COOP',
        '6640:MT:COOP',
        '6691:MT:COOP',
        '6700:MT:COOP',
        '6747:MT:COOP',
        '6862:MT:COOP',
        '6893:MT:COOP',
        '6902:MT:COOP',
        '6918:MT:COOP',
        '6927:MT:COOP',
        '7034:MT:COOP',
        '7128:MT:COOP',
        '7136:MT:COOP',
        '7159:MT:COOP',
        '7214:MT:COOP',
        '7248:MT:COOP',
        '7250:MT:COOP',
        '7263:MT:COOP',
        '7382:MT:COOP',
        '7425:MT:COOP',
        '7448:MT:COOP',
        '7500:MT:COOP',
        '7540:MT:COOP',
        '7560:MT:COOP',
        '7618:MT:COOP',
        '7620:MT:COOP',
        '7740:MT:COOP',
        '7800:MT:COOP',
        '7286:MT:COOP',
        '7292:MT:COOP',
        '7318:MT:COOP',
        '7864:MT:COOP',
        '7894:MT:COOP',
        '7964:MT:COOP',
        '7978:MT:COOP',
        '8021:MT:COOP',
        '7996:MT:COOP',
        '8043:MT:COOP',
        '8101:MT:COOP',
        '8211:MT:COOP',
        '8233:MT:COOP',
        '8324:MT:COOP',
        '8363:MT:COOP',
        '8380:MT:COOP',
        '8415:MT:COOP',
        '8430:MT:COOP',
        '8501:MT:COOP',
        '8569:MT:COOP',
        '8597:MT:COOP',
        '8607:MT:COOP',
        '8693:MT:COOP',
        '8732:MT:COOP',
        '8809:MT:COOP',
        '8777:MT:COOP',
        '8930:MT:COOP',
        '8902:MT:COOP',
        '8957:MT:COOP',
        '9023:MT:COOP',
        '9033:MT:COOP',
        '9067:MT:COOP',
        '9082:MT:COOP',
        '9103:MT:COOP',
        '9240:MT:COOP',
        '0375:ID:COOP',
        '1180:ID:COOP',
        '6586:ID:COOP',
        '8380:ID:COOP',
    ]

    Kootenai_RES = {
        '12301920': []
    }
    Flathead_RES = {
        '12375600': [],
        '12380500': [],
        '12380100': [],
        '12362000': [],
        '12371550': []
    }
    UpperClark_RES = {
        '12325000': [],
        '12332500': [],
        '12336500': []
    }
    Bitterroot_RES = {
        '12342000': [],
        '12344500': []
    }
    LowerClark_RES = {
        '12391300': [],
        '12390000': [],
    }
    Jefferson_RES = {
        '06012000': [],
        '06015300': [],
        '06020500': []
    }
    Madison_RES = {
        '06040500': [],
        '06038000': [],
    }
    Gallatin_RES = {
        '06049500': []
    }
    HeadMainstem_RES = {
        '06058500': [],
        '06058600': [],
        '06064500': [],
        '06065100': [],
        '06066000': [],
        '06131500': []
    }
    SJM_RES = {
        '06075000': [],
        '06110500': [],
        '06116500': [],
        '06119000': [],
        '06122500': []
    }
    STM_RES = {
        '06079500': [],
        '06080500': [],
        '06082000': [],
        '06090900': [],
        '06093000': [],
        '06094000': [],
        '06095500': [],
        '06101300': [],
        '06083000': []
    }
    SMM_RES = {
        '05015500': [],
        '06136500': [],
        '06155000': []
    }
    UpperYellowstone_RES = {
        '06204000': [],
        '06212000': []
    }
    Bighorn_RES = {
        '06286400': [],
        '06281500': [],
        '06258900': [],
        '06216400': [],
        '06224500': []
    }
    Tongue_RES = {
        '06307000': []
    }
    Powder_RES = {}

    Kootenai_SWE = {
        '311': [],
        '15B11': [],
        '15B16': [],
        '15B15': [],
        '323': [],
        '15A10': [],
        '14A13': [],
        '918': [],
        '500': [],
        '510': [],
        '516': [],
        '15A09': [],
        '932': [],
        '787': [],
        '14A07': []
    }
    Flathead_SWE = {
        '14A19': [],
        '307': [],
        '14B03': [],
        '346': [],
        '14B04': [],
        '1144': [],
        '14A13': [],
        '14A15': [],
        '13A02': [],
        '469': [],
        '13B04': [],
        '482': [],
        '500': [],
        '14A09': [],
        '510': [],
        '14A03': [],
        '14A16': [],
        '13B13': [],
        '14A06': [],
        '562': [],
        '14A05': [],
        '613': [],
        '13A05': [],
        '13A16': [],
        '646': [],
        '664': [],
        '667': [],
        '693': [],
        '14B06': [],
        '783': [],
        '13B02': [],
        '787': [],
        '14A17': [],
        '13B01': [],
        '14A18': [],
        '13B05': [],
        '14A07': []
    }
    UpperClark_SWE = {
        '13C16': [],
        '313': [],
        '315': [],
        '12C19': [],
        '349': [],
        '12D08': [],
        '410': [],
        '413': [],
        '414': [],
        '12C17': [],
        '13B10': [],
        '13C42': [],
        '12C15': [],
        '13C09': [],
        '604': [],
        '13C21': [],
        '13C22': [],
        '13C08': [],
        '13C37': [],
        '12C20': [],
        '657': [],
        '903': [],
        '667': [],
        '12C16': [],
        '930': [],
        '722': [],
        '760': [],
        '13C02': [],
        '12C01': [],
        '13C07': [],
        '901': [],
        '12C02': [],
        '12C03': [],
        '850': []
    }
    Bitterroot_SWE = {
        '13C16': [],
        '433': [],
        '13D02': [],
        '588': [],
        '662': [],
        '727': [],
        '760': [],
        '835': [],
        '836': []
    }
    LowerClark_SWE = {
        '15B11': [],
        '15B16': [],
        '15B15': [],
        '14B03': [],
        '15B22': [],
        '15B23': [],
        '530': [],
        '535': [],
        '588': [],
        '594': [],
        '932': [],
        '15B24': [],
        '15B05': [],
        '783': [],
        '901': []
    }
    Jefferson_SWE = {
        '916': [],
        '313': [],
        '315': [],
        '318': [],
        '355': [],
        '12D08': [],
        '381': [],
        '403': [],
        '12C09': [],
        '13E22': [],
        '436': [],
        '448': [],
        '13D15': [],
        '12D10': [],
        '12D07': [],
        '13D21': [],
        '487': [],
        '13D02': [],
        '13E28': [],
        '11E04': [],
        '568': [],
        '576': [],
        '603': [],
        '638': [],
        '12C20': [],
        '13D25': [],
        '656': [],
        '12D01': [],
        '722': [],
        '727': [],
        '753': [],
        '13D24': [],
        '13C07': [],
        '12C03': [],
        '860': []
    }
    Madison_SWE = {
        '916': [],
        '328': [],
        '347': [],
        '385': [],
        '403': [],
        '11D12': [],
        '11E05': [],
        '590': [],
        '603': [],
        '609': [],
        '10E19': [],
        '10E18': [],
        '11E21': [],
        '813': [],
        '924': [],
        '858': []
    }
    Gallatin_SWE = {
        '10D14': [],
        '11D09': [],
        '328': [],
        '365': [],
        '385': [],
        '578': [],
        '11D10': [],
        '590': [],
        '10D01': [],
        '11D21': [],
        '929': [],
        '754': [],
        '11E06': []
    }
    HeadMainstem_SWE = {
        '360': [],
        '12C05': [],
        '487': [],
        '903': [],
        '722': [],
        '12C01': [],
        '12C02': [],
        '12C03': [],
        '893': []
    }
    SJM_SWE = {
        '09C05': [],
        '360': [],
        '427': [],
        '919': [],
        '437': [],
        '10C13': [],
        '1106': [],
        '10C07': [],
        '10C14': [],
        '10C11': [],
        '10C12': [],
        '1008': [],
        '690': [],
        '700': [],
        '781': [],
        '1009': []
    }
    STM_SWE = {
        '307': [],
        '12B06': [],
        '458': [],
        '12A01': [],
        '12B07': [],
        '13A05': [],
        '649': [],
        '693': [],
        '847': [],
        '876': [],
        '12B04': [],
        '12B03': []
    }
    SMM_SWE = {
        '09A08': [],
        '482': [],
        '10Z04': [],
        '10Z05': [],
        '13A03': [],
        '13A14': [],
        '13Z08': [],
        '613': [],
        '13A16': [],
        '10Z06': [],
        '10Z07': [],
        '13A07': [],
        '13A06': [],
        '13A08': [],
        '917': [],
        '10Z08': [],
        '10Z09': [],
        '09A07': []
    }
    UpperYellowstone_SWE = {
        '326': [],
        '09D14': [],
        '363': [],
        '365': [],
        '981': [],
        '09D01': [],
        '384': [],
        '407': [],
        '10D05': [],
        '10C13': [],
        '1105': [],
        '472': [],
        '480': [],
        '10E04': [],
        '10E01': [],
        '635': [],
        '10E19': [],
        '670': [],
        '683': [],
        '696': [],
        '700': [],
        '11D21': [],
        '725': [],
        '929': [],
        '754': [],
        '806': [],
        '807': [],
        '816': [],
        '09D04': [],
        '837': [],
        '862': [],
        '09D17': [],
        '875': [],
        '878': []
    }
    Bighorn_SWE = {
        '309': [],
        '325': [],
        '350': [],
        '358': [],
        '472': [],
        '501': [],
        '560': [],
        '616': [],
        '07E24': [],
        '625': [],
        '07E27': [],
        '676': [],
        '703': [],
        '07E04': [],
        '751': [],
        '806': [],
        '807': [],
        '819': [],
        '07E35': [],
        '878': []
    }
    Tongue_SWE = {
        '931': [],
        '358': [],
        '377': [],
        '451': [],
        '1131': [],
        '07E15': [],
        '07E38': [],
        '751': [],
        '818': [],
        '798': [],
        '07E13': []
    }
    Powder_SWE = {
        '325': [],
        '402': [],
        '501': [],
        '512': [],
        '625': [],
        '07E27': [],
        '703': [],
        '1132': [],
        '07E05': [],
        '06E01': []
    }

    Kootenai_PCP = {
        '311:MT:SNTL': [],
        '323:ID:SNTL': [],
        '918:MT:SNTL': [],
        '500:MT:SNTL': [],
        '510:MT:SNTL': [],
        '516:MT:SNTL': [],
        '932:MT:SNTL': [],
        '787:MT:SNTL': [],
        '2827:MT:COOP': [],
        '5015:MT:COOP': [],
        '5020:MT:COOP': []
    }
    Flathead_PCP = {
        '1144:MT:SNTL': [],
        '1165:MT:SNTLT': [],
        '1190:MT:SNTLT': [],
        '307:MT:SNTL': [],
        '346:MT:SNTL': [],
        '469:MT:SNTL': [],
        '482:MT:SNTL': [],
        '500:MT:SNTL': [],
        '510:MT:SNTL': [],
        '562:MT:SNTL': [],
        '613:MT:SNTL': [],
        '646:MT:SNTL': [],
        '664:MT:SNTL': [],
        '667:MT:SNTL': [],
        '693:MT:SNTL': [],
        '783:MT:SNTL': [],
        '787:MT:SNTL': [],
        '0755:MT:COOP': [],
        '4558:MT:COOP': [],
        '6640:MT:COOP': [],
        '8902:MT:COOP': []
    }
    UpperClark_PCP = {
        '313:MT:SNTL': [],
        '315:MT:SNTL': [],
        '349:MT:SNTL': [],
        '410:MT:SNTL': [],
        '413:MT:SNTL': [],
        '414:MT:SNTL': [],
        '604:MT:SNTL': [],
        '657:MT:SNTL': [],
        '667:MT:SNTL': [],
        '722:MT:SNTL': [],
        '760:MT:SNTL': [],
        '850:MT:SNTL': [],
        '901:MT:SNTL': [],
        '903:MT:SNTL': [],
        '930:MT:SNTL': [],
        '1318:MT:COOP': [],
        '6472:MT:COOP': [],
        '7448:MT:COOP': [],
        'ML15:MT:MPRC': []
    }
    Bitterroot_PCP = {
        '433:MT:SNTL': [],
        '588:ID:SNTL': [],
        '662:MT:SNTL': [],
        '727:MT:SNTL': [],
        '760:MT:SNTL': [],
        '835:MT:SNTL': [],
        '836:MT:SNTL': [],
        '2221:MT:COOP': [],
        '3885:MT:COOP': [],
        '7894:MT:COOP': []
    }
    LowerClark_PCP = {
        '1190:MT:SNTLT': [],
        '530:MT:SNTL': [],
        '535:ID:SNTL': [],
        '588:ID:SNTL': [],
        '594:ID:SNTL': [],
        '783:MT:SNTL': [],
        '901:MT:SNTL': [],
        '932:MT:SNTL': [],
        '4084:MT:COOP': [],
        '5745:MT:COOP': [],
        '8043:MT:COOP': [],
        '8211:MT:COOP': [],
        '8380:MT:COOP': []
    }
    Jefferson_PCP = {
        '313:MT:SNTL': [],
        '315:MT:SNTL': [],
        '318:MT:SNTL': [],
        '355:MT:SNTL': [],
        '381:MT:SNTL': [],
        '403:MT:SNTL': [],
        '436:MT:SNTL': [],
        '448:MT:SNTL': [],
        '487:MT:SNTL': [],
        '568:MT:SNTL': [],
        '576:MT:SNTL': [],
        '603:MT:SNTL': [],
        '638:ID:SNTL': [],
        '656:MT:SNTL': [],
        '722:MT:SNTL': [],
        '727:MT:SNTL': [],
        '753:MT:SNTL': [],
        '860:ID:SNTL': [],
        '916:MT:SNTL': [],
        '0110:MT:COOP': [],
        '1008:MT:COOP': [],
        '2409:MT:COOP': [],
        '3707:MT:COOP': [],
        '8430:MT:COOP': [],
        '8597:MT:COOP': [],
        '9067:MT:COOP': [],
        '9082:MT:COOP': []
    }
    Madison_PCP = {
        '328:MT:SNTL': [],
        '347:MT:SNTL': [],
        '385:MT:SNTL': [],
        '403:MT:SNTL': [],
        '590:MT:SNTL': [],
        '603:MT:SNTL': [],
        '609:MT:SNTL': [],
        '813:MT:SNTL': [],
        '858:MT:SNTL': [],
        '916:MT:SNTL': [],
        '924:MT:SNTL': [],
        '2793:MT:COOP': [],
        '4038:MT:COOP': [],
        '6157:MT:COOP': [],
        '6845:WY:COOP': []
    }
    Gallatin_PCP = {
        '328:MT:SNTL': [],
        '365:MT:SNTL': [],
        '385:MT:SNTL': [],
        '578:MT:SNTL': [],
        '590:MT:SNTL': [],
        '929:MT:SNTL': [],
        '754:MT:SNTL': [],
        '0622:MT:COOP': [],
        '1044:MT:COOP': []
    }
    HeadMainstem_PCP = {
        '360:MT:SNTL': [],
        '487:MT:SNTL': [],
        '903:MT:SNTL': [],
        '722:MT:SNTL': [],
        '893:MT:SNTL': [],
        '4055:MT:COOP': [],
        '4241:MT:COOP': [],
        '8324:MT:COOP': []
    }
    SJM_PCP = {
        '360:MT:SNTL': [],
        '427:MT:SNTL': [],
        '919:MT:SNTL': [],
        '437:MT:SNTL': [],
        '1106:MT:SNTL': [],
        '1008:MT:SNTL': [],
        '690:MT:SNTL': [],
        '700:MT:SNTL': [],
        '781:MT:SNTL': [],
        '1009:MT:SNTL': [],
        '2347:MT:COOP': [],
        '3727:MT:COOP': [],
        '3939:MT:COOP': [],
        '4538:MT:COOP': [],
        '4545:MT:COOP': [],
        '4954:MT:COOP': [],
        '4978:MT:COOP': [],
        '4985:MT:COOP': [],
        '5596:MT:COOP': [],
        '5761:MT:COOP': [],
        '5872:MT:COOP': [],
        '6008:MT:COOP': [],
        '7214:MT:COOP': [],
        '7263:MT:COOP': [],
        '7864:MT:COOP': []
    }
    STM_PCP = {
        '307:MT:SNTL': [],
        '458:MT:SNTL': [],
        '649:MT:SNTL': [],
        '693:MT:SNTL': [],
        '847:MT:SNTL': [],
        '876:MT:SNTL': [],
        '1692:MT:COOP': [],
        '1737:MT:COOP': [],
        '1974:MT:COOP': [],
        '2173:MT:COOP': [],
        '2629:MT:COOP': [],
        '2820:MT:COOP': [],
        '2857:MT:COOP': [],
        '3489:MT:COOP': [],
        '3617:MT:COOP': [],
        '7978:MT:COOP': [],
        '8101:MT:COOP': []
    }
    SMM_PCP = {
        '482:MT:SNTL': [],
        '613:MT:SNTL': [],
        '917:MT:SNTL': [],
        '1722:MT:COOP': [],
        '3110:MT:COOP': [],
        '3530:MT:COOP': [],
        '3558:MT:COOP': [],
        '3996:MT:COOP': [],
        '4174:MT:COOP': [],
        '4766:MT:COOP': [],
        '5338:MT:COOP': [],
        '6236:MT:COOP': [],
        '6238:MT:COOP': [],
        '7292:MT:COOP': [],
        '7620:MT:COOP': [],
        '8415:MT:COOP': [],
        'TU07:MT:MPRC': [],
        'TU08:MT:MPRC': []
    }
    UpperYellowstone_PCP = {
        '1105:MT:SNTL': [],
        '326:WY:SNTL': [],
        '363:MT:SNTL': [],
        '365:MT:SNTL': [],
        '384:WY:SNTL': [],
        '407:MT:SNTL': [],
        '472:WY:SNTL': [],
        '480:MT:SNTL': [],
        '635:MT:SNTL': [],
        '670:MT:SNTL': [],
        '683:WY:SNTL': [],
        '696:MT:SNTL': [],
        '700:MT:SNTL': [],
        '725:MT:SNTL': [],
        '754:MT:SNTL': [],
        '806:WY:SNTL': [],
        '807:WY:SNTL': [],
        '816:WY:SNTL': [],
        '837:WY:SNTL': [],
        '862:MT:SNTL': [],
        '875:WY:SNTL': [],
        '878:WY:SNTL': [],
        '929:MT:SNTL': [],
        '981:MT:SNTL': [],
        '0780:MT:COOP': [],
        '0807:MT:COOP': [],
        '1938:MT:COOP': [],
        '2996:MT:COOP': [],
        '4506:MT:COOP': [],
        '5080:MT:COOP': [],
        '5086:MT:COOP': [],
        '5603:MT:COOP': [],
        '6190:MT:COOP': [],
        '6862:MT:COOP': [],
        '6918:MT:COOP': [],
        '7800:MT:COOP': [],
        '9023:MT:COOP': [],
        'TT01:MT:MPRC': []}
    Bighorn_PCP = {
        '309:WY:SNTL': [],
        '325:WY:SNTL': [],
        '350:WY:SNTL': [],
        '358:WY:SNTL': [],
        '472:WY:SNTL': [],
        '501:WY:SNTL': [],
        '560:WY:SNTL': [],
        '616:WY:SNTL': [],
        '625:WY:SNTL': [],
        '676:WY:SNTL': [],
        '703:WY:SNTL': [],
        '751:WY:SNTL': [],
        '806:WY:SNTL': [],
        '807:WY:SNTL': [],
        '819:WY:SNTL': [],
        '878:WY:SNTL': []
    }
    Tongue_PCP = {
        '1131:WY:SNTL': [],
        '358:WY:SNTL': [],
        '377:WY:SNTL': [],
        '451:WY:SNTL': [],
        '751:WY:SNTL': [],
        '798:WY:SNTL': [],
        '818:WY:SNTL': [],
        '931:WY:SNTL': []
    }
    Powder_PCP = {
        '1132:WY:SNTL': [],
        '325:WY:SNTL': [],
        '402:WY:SNTL': [],
        '501:WY:SNTL': [],
        '512:WY:SNTL': [],
        '625:WY:SNTL': [],
        '703:WY:SNTL': []
    }

    # *********PROGRAM************

    if month_input == '01':
        month = '12'
        year = str(int(year_input) - 1)
    else:
        month = str(int(month_input) - 1)
        year = year_input

    date_input = month + '/01/' + year
    date_swe = month_input + '/01/' + year_input

    if month == '10' or month == '11' or month == '12':
        wy_start = year
    else:
        wy_start = str(int(year) - 1)

    month_index = {
        '10': 12,
        '11': 1,
        '12': 2,
        '1': 3,
        '2': 4,
        '3': 5,
        '4': 6,
        '5': 7,
        '6': 8,
        '7': 9,
        '8': 10,
        '9': 11
    }

    sort_order = [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]
    month_value = {10: 12, 11: 1, 12: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11}

    headers = {'Content-type': 'text/soap'}
    wsURL = "https://wcc.sc.egov.usda.gov/awdbWebService/services?WSDL"

    # reservoirs
    soap_reservoir_current = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getData>
          $StationTriplet$   
          <elementCd>RESC</elementCd>
          <ordinal>1</ordinal>
          <duration>MONTHLY</duration>
          <getFlags>false</getFlags>
          <beginDate>$BEGINDATE$</beginDate>
          <endDate>$ENDDATE$</endDate>
          <alwaysReturnDailyFeb29>false</alwaysReturnDailyFeb29>
        </q0:getData>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()
    soap_reservoir_normal = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getCentralTendencyData>
          $StationTriplet$   
          <elementCd>RESC</elementCd>
          <duration>MONTHLY</duration>
          <getFlags>false</getFlags>
          <beginMonth>$MONTH$</beginMonth>
          <beginDay>01</beginDay>
          <endMonth>$MONTH$</endMonth>
          <endDay>01</endDay>
          <centralTendencyType>NORMAL</centralTendencyType>
        </q0:getCentralTendencyData>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()
    soap_reservoir_capacity = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getReservoirMetadataMultiple>
          $StationTriplet$
        </q0:getReservoirMetadataMultiple>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()

    reservoir_list = []
    for i in range(len(reservoir_triplets)):
        station = '<stationTriplets>' + reservoir_triplets[i] + '</stationTriplets>'
        reservoir_list.append(station)
    reservoirs = "\n".join(reservoir_list)
    soap_reservoir_current = soap_reservoir_current.replace("$StationTriplet$", reservoirs)
    soap_reservoir_current = soap_reservoir_current.replace("$BEGINDATE$", date_input)
    soap_reservoir_current = soap_reservoir_current.replace("$ENDDATE$", date_input)
    soap_reservoir_normal = soap_reservoir_normal.replace("$StationTriplet$", reservoirs)
    soap_reservoir_normal = soap_reservoir_normal.replace("$MONTH$", month)
    soap_reservoir_normal = soap_reservoir_normal.replace("$MONTH$", month)
    soap_reservoir_capacity = soap_reservoir_capacity.replace("$StationTriplet$", reservoirs)

    reservoir_dict = {}
    response = requests.post(wsURL, data=soap_reservoir_current, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length == 5:
            if returns.getElementsByTagName('values')[0].firstChild:
                date_output = returns.getElementsByTagName('beginDate')[0].firstChild.data
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                id_output = triplet_output.split(':', 1)
                id_output = id_output[0]
                current_value = returns.getElementsByTagName('values')[0].firstChild.data
                current_value = float(current_value)
                reservoir_dict.update({id_output: [current_value]})
            else:
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                id_output = triplet_output.split(':', 1)
                id_output = id_output[0]
                reservoir_dict.update({id_output: [None]})
        else:
            triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
            id_output = triplet_output.split(':', 1)
            id_output = id_output[0]
            reservoir_dict.update({id_output: [None]})

    reservoir_normals = []
    response = requests.post(wsURL, data=soap_reservoir_normal, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length == 7:
            if returns.getElementsByTagName('values')[0].firstChild:
                normal_value = returns.getElementsByTagName('values')[0].firstChild.data
                normal_value = float(normal_value)
                reservoir_normals.append(normal_value)
            else:
                reservoir_normals.append(None)
        else:
            reservoir_normals.append(None)

    if len(reservoir_normals) == len(reservoir_dict):
        i = 1
        for k, v in reservoir_dict.items():
            reservoir_dict[k].append(reservoir_normals[i - 1])
            i = i + 1
    else:
        print('Reservoir Error')

    for k, v in reservoir_dict.items():
        if type(v[0]) is float and type(v[1]) is float and v[1] > 0:
            percent = v[0] / v[1] * 100
            percent = round(percent)
            reservoir_dict[k].append(percent)
        else:
            reservoir_dict[k].append(None)

    reservoir_capacity = {}
    response = requests.post(wsURL, data=soap_reservoir_capacity, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length == 3:
            if returns.getElementsByTagName('usableCapacity')[0].firstChild:
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                id_output = triplet_output.split(':', 1)
                id_output = id_output[0]
                current_value = returns.getElementsByTagName('usableCapacity')[0].firstChild.data
                current_value = float(current_value)
                reservoir_capacity.update({id_output: current_value})
            else:
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                id_output = triplet_output.split(':', 1)
                id_output = id_output[0]
                reservoir_capacity.update({id_output: None})
        else:
            triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
            id_output = triplet_output.split(':', 1)
            id_output = id_output[0]
            reservoir_capacity.update({id_output: None})

    if len(reservoir_capacity) == len(reservoir_dict):
        for k, v in reservoir_dict.items():
            reservoir_dict[k].append(reservoir_capacity[k])
    else:
        print('Reservoir Error')

    for k, v in reservoir_dict.items():
        if type(v[0]) is float and type(v[3]) is float and v[3] > 0:
            percent = v[0] / v[3] * 100
            percent = round(percent)
            reservoir_dict[k].append(percent)
        else:
            reservoir_dict[k].append(None)

    # snow water equivalent
    soap_swe_current = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getData>
          $StationTriplet$
          <elementCd>WTEQ</elementCd>
          <ordinal>1</ordinal>
          <duration>SEMIMONTHLY</duration>
          <getFlags>false</getFlags>
          <beginDate>$BEGINDATE$</beginDate>
          <endDate>$ENDDATE$</endDate>
          <alwaysReturnDailyFeb29>false</alwaysReturnDailyFeb29>
        </q0:getData>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()
    soap_swe_normal = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getCentralTendencyData>
          $StationTriplet$
          <elementCd>WTEQ</elementCd>
          <duration>SEMIMONTHLY</duration>
          <getFlags>false</getFlags>
          <beginMonth>$BEGINMONTH$</beginMonth>
          <beginDay>01</beginDay>
          <endMonth>$ENDMONTH$</endMonth>
          <endDay>01</endDay>
          <centralTendencyType>NORMAL</centralTendencyType>
        </q0:getCentralTendencyData>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()

    swe_list = []
    for i in range(len(swe_triplets)):
        station = '<stationTriplets>' + swe_triplets[i] + '</stationTriplets>'
        swe_list.append(station)
    swe = "\n".join(swe_list)
    soap_swe_current = soap_swe_current.replace("$StationTriplet$", swe)
    soap_swe_current = soap_swe_current.replace("$BEGINDATE$", date_swe)
    soap_swe_current = soap_swe_current.replace("$ENDDATE$", date_swe)
    soap_swe_normal = soap_swe_normal.replace("$StationTriplet$", swe)
    soap_swe_normal = soap_swe_normal.replace("$BEGINMONTH$", month_input)
    soap_swe_normal = soap_swe_normal.replace("$ENDMONTH$", month_input)

    swe_dict = {}
    response = requests.post(wsURL, data=soap_swe_current, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length == 8:
            if returns.getElementsByTagName('values')[0].firstChild:
                date_output = returns.getElementsByTagName('beginDate')[0].firstChild.data
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                id_output = triplet_output.split(':', 1)
                id_output = id_output[0]
                current_value = returns.getElementsByTagName('values')[0].firstChild.data
                current_value = float(current_value)
                swe_dict.update({id_output: [current_value]})
            else:
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                id_output = triplet_output.split(':', 1)
                id_output = id_output[0]
                swe_dict.update({id_output: [None]})
        else:
            triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
            id_output = triplet_output.split(':', 1)
            id_output = id_output[0]
            swe_dict.update({id_output: [None]})

    swe_normals = []
    response = requests.post(wsURL, data=soap_swe_normal, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length == 8:
            if returns.getElementsByTagName('values')[0].firstChild:
                normal_value = returns.getElementsByTagName('values')[0].firstChild.data
                normal_value = float(normal_value)
                swe_normals.append(normal_value)
            else:
                swe_normals.append(None)
        else:
            swe_normals.append(None)

    if len(swe_normals) == len(swe_dict):
        i = 1
        for k, v in swe_dict.items():
            swe_dict[k].append(swe_normals[i - 1])
            i = i + 1
    else:
        print('SWE Error')

    for k, v in swe_dict.items():
        if type(v[0]) is float and type(v[1]) is float and v[1] > 0:
            percent = v[0] / v[1] * 100
            percent = round(percent)
            swe_dict[k].append(percent)
        else:
            swe_dict[k].append(None)

    # monthly precipitation
    soap_mpcp_current = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getData>
          $StationTriplet$
          <elementCd>PRCP</elementCd>
          <ordinal>1</ordinal>
          <duration>MONTHLY</duration>
          <getFlags>false</getFlags>
          <beginDate>$BEGINDATE$</beginDate>
          <endDate>$ENDDATE$</endDate>
          <alwaysReturnDailyFeb29>false</alwaysReturnDailyFeb29>
        </q0:getData>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()
    soap_mpcp_normal = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getCentralTendencyData>
          $StationTriplet$
          <elementCd>PRCP</elementCd>
          <duration>MONTHLY</duration>
          <getFlags>false</getFlags>
          <beginMonth>$BEGINMONTH$</beginMonth>
          <beginDay>01</beginDay>
          <endMonth>$ENDMONTH$</endMonth>
          <endDay>01</endDay>
          <centralTendencyType>AVERAGE</centralTendencyType>
        </q0:getCentralTendencyData>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()

    mpcp_list = []
    for i in range(len(pcp_triplets)):
        station = '<stationTriplets>' + pcp_triplets[i] + '</stationTriplets>'
        mpcp_list.append(station)
    pcp = "\n".join(mpcp_list)
    soap_mpcp_current = soap_mpcp_current.replace("$StationTriplet$", pcp)
    soap_mpcp_current = soap_mpcp_current.replace("$BEGINDATE$", date_input)
    soap_mpcp_current = soap_mpcp_current.replace("$ENDDATE$", date_input)
    soap_mpcp_normal = soap_mpcp_normal.replace("$StationTriplet$", pcp)
    soap_mpcp_normal = soap_mpcp_normal.replace("$BEGINMONTH$", month)
    soap_mpcp_normal = soap_mpcp_normal.replace("$ENDMONTH$", month)

    mpcp_dict = {}
    response = requests.post(wsURL, data=soap_mpcp_current, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length == 5:
            if returns.getElementsByTagName('values')[0].firstChild:
                date_output = returns.getElementsByTagName('beginDate')[0].firstChild.data
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                current_value = returns.getElementsByTagName('values')[0].firstChild.data
                current_value = float(current_value)
                mpcp_dict.update({triplet_output: [current_value]})
            else:
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                mpcp_dict.update({triplet_output: [None]})
        else:
            triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
            mpcp_dict.update({triplet_output: [None]})

    mpcp_normals = []
    response = requests.post(wsURL, data=soap_mpcp_normal, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length == 7:
            if returns.getElementsByTagName('values')[0].firstChild:
                normal_value = returns.getElementsByTagName('values')[0].firstChild.data
                normal_value = float(normal_value)
                mpcp_normals.append(normal_value)
            else:
                mpcp_normals.append(None)
        else:
            mpcp_normals.append(None)

    if len(mpcp_normals) == len(mpcp_dict):
        i = 1
        for k, v in mpcp_dict.items():
            mpcp_dict[k].append(mpcp_normals[i - 1])
            i = i + 1
    else:
        print('Monthly PCP Error')

    for k, v in mpcp_dict.items():
        if type(v[0]) is float and type(v[1]) is float and v[1] > 0:
            percent = v[0] / v[1] * 100
            percent = round(percent)
            mpcp_dict[k].append(percent)
        else:
            mpcp_dict[k].append(None)

    # Water Year Precipitation
    soap_wpcp_current = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getData>
          $StationTriplet$
          <elementCd>PRCP</elementCd>
          <ordinal>1</ordinal>
          <duration>MONTHLY</duration>
          <getFlags>false</getFlags>
          <beginDate>10/01/$BEGINYEAR$</beginDate>
          <endDate>$ENDDATE$</endDate>
          <alwaysReturnDailyFeb29>false</alwaysReturnDailyFeb29>
        </q0:getData>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()
    soap_wpcp_normal = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:q0="http://www.wcc.nrcs.usda.gov/ns/awdbWebService" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <SOAP-ENV:Body>
        <q0:getCentralTendencyData>
          $StationTriplet$
          <elementCd>PRCP</elementCd>
          <duration>MONTHLY</duration>
          <getFlags>false</getFlags>
          <beginMonth>01</beginMonth>
          <beginDay>01</beginDay>
          <endMonth>12</endMonth>
          <endDay>01</endDay>
          <centralTendencyType>AVERAGE</centralTendencyType>
        </q0:getCentralTendencyData>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    '''.strip()

    wpcp_list = []
    for i in range(len(pcp_triplets)):
        station = '<stationTriplets>' + pcp_triplets[i] + '</stationTriplets>'
        wpcp_list.append(station)
    pcp = "\n".join(wpcp_list)
    soap_wpcp_current = soap_wpcp_current.replace("$StationTriplet$", pcp)
    soap_wpcp_current = soap_wpcp_current.replace("$BEGINYEAR$", wy_start)
    soap_wpcp_current = soap_wpcp_current.replace("$ENDDATE$", date_input)
    soap_wpcp_normal = soap_wpcp_normal.replace("$StationTriplet$", pcp)

    wpcp_dict = {}
    sum_dict = {}
    response = requests.post(wsURL, data=soap_wpcp_current, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length > 4:
            if returns.getElementsByTagName('values')[0].firstChild:
                date_output = returns.getElementsByTagName('beginDate')[0].firstChild.data
                length = returns.childNodes.length
                num_values = int(length - 4)
                num_values_time = month_value.get(int(month_input))
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                sum_dict.update({triplet_output: []})
                for i in range(0, num_values):
                    if returns.getElementsByTagName('values')[i].childNodes.length == 1:
                        value = float(returns.getElementsByTagName('values')[i].firstChild.data)
                        for k, v in sum_dict.items():
                            if k == triplet_output:
                                sum_dict[k].append(value)
                                if len(sum_dict[k]) == num_values_time:
                                    wpcp_dict.update({triplet_output: [round(sum(v), 2)]})
                                else:
                                    wpcp_dict.update({triplet_output: [None]})
                    else:
                        wpcp_dict.update({triplet_output: [None]})
            else:
                triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
                wpcp_dict.update({triplet_output: [None]})
        else:
            triplet_output = returns.getElementsByTagName('stationTriplet')[0].firstChild.data
            wpcp_dict.update({triplet_output: [None]})

    wpcp_normals = []
    response = requests.post(wsURL, data=soap_wpcp_normal, headers=headers)
    xmldoc = minidom.parseString(response.text)
    placemarks = xmldoc.getElementsByTagName('return')
    for returns in placemarks:
        if returns.childNodes.length == 18:
            if returns.getElementsByTagName('values')[0].firstChild:
                temporary_list = []
                for i in range(0, 12):
                    if returns.getElementsByTagName('values')[i].childNodes.length == 1:
                        temporary_list.insert(i, float(returns.getElementsByTagName('values')[i].firstChild.data))
                    else:
                        wpcp_normals.append(None)
                merged_list = [(sort_order[i], temporary_list[i]) for i in range(0, 12)]
                merged_list.sort()
                new_list = list(map(lambda x: x[1], merged_list))
                wpcp_normals.append(round(sum(new_list[0:month_index[month_input]]), 2))
                del temporary_list
            else:
                wpcp_normals.append(None)
        else:
            wpcp_normals.append(None)

    if len(wpcp_normals) == len(wpcp_dict):
        i = 1
        for k, v in wpcp_dict.items():
            wpcp_dict[k].append(wpcp_normals[i - 1])
            i = i + 1
    else:
        print('Water Year PCP Error')

    for k, v in wpcp_dict.items():
        if type(v[0]) is float and type(v[1]) is float and v[1] > 0:
            percent = v[0] / v[1] * 100
            percent = round(percent)
            wpcp_dict[k].append(percent)
        else:
            wpcp_dict[k].append(None)

    def BasinPercentCalculator(BasinDefinition, Dictionary):
        if len(BasinDefinition) > 0:
            BasinDefinition.update([(key, Dictionary[key]) for key in BasinDefinition.keys()])
            current = []
            normal = []
            for i in BasinDefinition:
                if len(BasinDefinition[i]) != 3 or BasinDefinition[i][0] == None or BasinDefinition[i][1] == None:
                    pass
                else:
                    current.append(BasinDefinition[i][0])
                    normal.append(BasinDefinition[i][1])
            if len(current) == len(normal):
                return round(sum(current) / sum(normal) * 100)
            else:
                return None
        else:
            return None

    def BasinPercentCalculator_Reservoir(BasinDefinition, Dictionary, Variable):
        if len(BasinDefinition) > 0:
            BasinDefinition.update([(key, Dictionary[key]) for key in BasinDefinition.keys()])
            current = []
            list = []
            for i in BasinDefinition:
                if len(BasinDefinition[i]) != 5 or BasinDefinition[i][0] == None or BasinDefinition[i][1] == None or \
                        BasinDefinition[i][3] == None:
                    pass
                else:
                    current.append(BasinDefinition[i][0])
                    if Variable == 1:
                        list.append(BasinDefinition[i][1])
                    else:
                        list.append(BasinDefinition[i][3])
            if len(current) == len(list):
                return round(sum(current) / sum(list) * 100)
            else:
                return None
        else:
            return None

    swe1 = BasinPercentCalculator(Kootenai_SWE, swe_dict)
    swe2 = BasinPercentCalculator(Flathead_SWE, swe_dict)
    swe3 = BasinPercentCalculator(UpperClark_SWE, swe_dict)
    swe4 = BasinPercentCalculator(Bitterroot_SWE, swe_dict)
    swe5 = BasinPercentCalculator(LowerClark_SWE, swe_dict)
    swe6 = BasinPercentCalculator(Jefferson_SWE, swe_dict)
    swe7 = BasinPercentCalculator(Madison_SWE, swe_dict)
    swe8 = BasinPercentCalculator(Gallatin_SWE, swe_dict)
    swe9 = BasinPercentCalculator(HeadMainstem_SWE, swe_dict)
    swe10 = BasinPercentCalculator(SJM_SWE, swe_dict)
    swe11 = BasinPercentCalculator(STM_SWE, swe_dict)
    swe12 = BasinPercentCalculator(SMM_SWE, swe_dict)
    swe13 = BasinPercentCalculator(UpperYellowstone_SWE, swe_dict)
    swe14 = BasinPercentCalculator(Bighorn_SWE, swe_dict)
    swe15 = BasinPercentCalculator(Tongue_SWE, swe_dict)
    swe16 = BasinPercentCalculator(Powder_SWE, swe_dict)

    mpcp1 = BasinPercentCalculator(Kootenai_PCP, mpcp_dict)
    mpcp2 = BasinPercentCalculator(Flathead_PCP, mpcp_dict)
    mpcp3 = BasinPercentCalculator(UpperClark_PCP, mpcp_dict)
    mpcp4 = BasinPercentCalculator(Bitterroot_PCP, mpcp_dict)
    mpcp5 = BasinPercentCalculator(LowerClark_PCP, mpcp_dict)
    mpcp6 = BasinPercentCalculator(Jefferson_PCP, mpcp_dict)
    mpcp7 = BasinPercentCalculator(Madison_PCP, mpcp_dict)
    mpcp8 = BasinPercentCalculator(Gallatin_PCP, mpcp_dict)
    mpcp9 = BasinPercentCalculator(HeadMainstem_PCP, mpcp_dict)
    mpcp10 = BasinPercentCalculator(SJM_PCP, mpcp_dict)
    mpcp11 = BasinPercentCalculator(STM_PCP, mpcp_dict)
    mpcp12 = BasinPercentCalculator(SMM_PCP, mpcp_dict)
    mpcp13 = BasinPercentCalculator(UpperYellowstone_PCP, mpcp_dict)
    mpcp14 = BasinPercentCalculator(Bighorn_PCP, mpcp_dict)
    mpcp15 = BasinPercentCalculator(Tongue_PCP, mpcp_dict)
    mpcp16 = BasinPercentCalculator(Powder_PCP, mpcp_dict)

    wpcp1 = BasinPercentCalculator(Kootenai_PCP, wpcp_dict)
    wpcp2 = BasinPercentCalculator(Flathead_PCP, wpcp_dict)
    wpcp3 = BasinPercentCalculator(UpperClark_PCP, wpcp_dict)
    wpcp4 = BasinPercentCalculator(Bitterroot_PCP, wpcp_dict)
    wpcp5 = BasinPercentCalculator(LowerClark_PCP, wpcp_dict)
    wpcp6 = BasinPercentCalculator(Jefferson_PCP, wpcp_dict)
    wpcp7 = BasinPercentCalculator(Madison_PCP, wpcp_dict)
    wpcp8 = BasinPercentCalculator(Gallatin_PCP, wpcp_dict)
    wpcp9 = BasinPercentCalculator(HeadMainstem_PCP, wpcp_dict)
    wpcp10 = BasinPercentCalculator(SJM_PCP, wpcp_dict)
    wpcp11 = BasinPercentCalculator(STM_PCP, wpcp_dict)
    wpcp12 = BasinPercentCalculator(SMM_PCP, wpcp_dict)
    wpcp13 = BasinPercentCalculator(UpperYellowstone_PCP, wpcp_dict)
    wpcp14 = BasinPercentCalculator(Bighorn_PCP, wpcp_dict)
    wpcp15 = BasinPercentCalculator(Tongue_PCP, wpcp_dict)
    wpcp16 = BasinPercentCalculator(Powder_PCP, wpcp_dict)

    res1 = BasinPercentCalculator_Reservoir(Kootenai_RES, reservoir_dict, 1)
    res2 = BasinPercentCalculator_Reservoir(Flathead_RES, reservoir_dict, 1)
    res3 = BasinPercentCalculator_Reservoir(UpperClark_RES, reservoir_dict, 1)
    res4 = BasinPercentCalculator_Reservoir(Bitterroot_RES, reservoir_dict, 1)
    res5 = BasinPercentCalculator_Reservoir(LowerClark_RES, reservoir_dict, 1)
    res6 = BasinPercentCalculator_Reservoir(Jefferson_RES, reservoir_dict, 1)
    res7 = BasinPercentCalculator_Reservoir(Madison_RES, reservoir_dict, 1)
    res8 = BasinPercentCalculator_Reservoir(Gallatin_RES, reservoir_dict, 1)
    res9 = BasinPercentCalculator_Reservoir(HeadMainstem_RES, reservoir_dict, 1)
    res10 = BasinPercentCalculator_Reservoir(SJM_RES, reservoir_dict, 1)
    res11 = BasinPercentCalculator_Reservoir(STM_RES, reservoir_dict, 1)
    res12 = BasinPercentCalculator_Reservoir(SMM_RES, reservoir_dict, 1)
    res13 = BasinPercentCalculator_Reservoir(UpperYellowstone_RES, reservoir_dict, 1)
    res14 = BasinPercentCalculator_Reservoir(Bighorn_RES, reservoir_dict, 1)
    res15 = BasinPercentCalculator_Reservoir(Tongue_RES, reservoir_dict, 1)
    res16 = BasinPercentCalculator_Reservoir(Powder_RES, reservoir_dict, 1)

    rescap1 = BasinPercentCalculator_Reservoir(Kootenai_RES, reservoir_dict, 2)
    rescap2 = BasinPercentCalculator_Reservoir(Flathead_RES, reservoir_dict, 2)
    rescap3 = BasinPercentCalculator_Reservoir(UpperClark_RES, reservoir_dict, 2)
    rescap4 = BasinPercentCalculator_Reservoir(Bitterroot_RES, reservoir_dict, 2)
    rescap5 = BasinPercentCalculator_Reservoir(LowerClark_RES, reservoir_dict, 2)
    rescap6 = BasinPercentCalculator_Reservoir(Jefferson_RES, reservoir_dict, 2)
    rescap7 = BasinPercentCalculator_Reservoir(Madison_RES, reservoir_dict, 2)
    rescap8 = BasinPercentCalculator_Reservoir(Gallatin_RES, reservoir_dict, 2)
    rescap9 = BasinPercentCalculator_Reservoir(HeadMainstem_RES, reservoir_dict, 2)
    rescap10 = BasinPercentCalculator_Reservoir(SJM_RES, reservoir_dict, 2)
    rescap11 = BasinPercentCalculator_Reservoir(STM_RES, reservoir_dict, 2)
    rescap12 = BasinPercentCalculator_Reservoir(SMM_RES, reservoir_dict, 2)
    rescap13 = BasinPercentCalculator_Reservoir(UpperYellowstone_RES, reservoir_dict, 2)
    rescap14 = BasinPercentCalculator_Reservoir(Bighorn_RES, reservoir_dict, 2)
    rescap15 = BasinPercentCalculator_Reservoir(Tongue_RES, reservoir_dict, 2)
    rescap16 = BasinPercentCalculator_Reservoir(Powder_RES, reservoir_dict, 2)

    columbia_swe = statistics.mean([swe1, swe2, swe3, swe4, swe5])
    missouri_swe = statistics.mean([swe6, swe7, swe8, swe9, swe10, swe11, swe12])
    yellowstone_swe = statistics.mean([swe13, swe14, swe15, swe16])
    montana_swe = statistics.mean([columbia_swe, missouri_swe, yellowstone_swe])

    columbia_mpcp = statistics.mean([mpcp1, mpcp2, mpcp3, mpcp4, mpcp5])
    missouri_mpcp = statistics.mean([mpcp6, mpcp7, mpcp8, mpcp9, mpcp10, mpcp11, mpcp12])
    yellowstone_mpcp = statistics.mean([mpcp13, mpcp14, mpcp15, mpcp16])
    montana_mpcp = statistics.mean([columbia_mpcp, missouri_mpcp, yellowstone_mpcp])

    columbia_wpcp = statistics.mean([wpcp1, wpcp2, wpcp3, wpcp4, wpcp5])
    missouri_wpcp = statistics.mean([wpcp6, wpcp7, wpcp8, wpcp9, wpcp10, wpcp11, wpcp12])
    yellowstone_wpcp = statistics.mean([wpcp13, wpcp14, wpcp15, wpcp16])
    montana_wpcp = statistics.mean([columbia_wpcp, missouri_wpcp, yellowstone_wpcp])

    columbia_res = statistics.mean([res1, res2, res3, res4, res5])
    missouri_res = statistics.mean([res6, res7, res8, res9, res10, res11, res12])
    yellowstone_res = statistics.mean([res13, res14, res15])
    montana_res = statistics.mean([columbia_res, missouri_res, yellowstone_res])

    columbia_rescap = statistics.mean([rescap1, rescap2, rescap3, rescap4, rescap5])
    missouri_rescap = statistics.mean([rescap6, rescap7, rescap8, rescap9, rescap10, rescap11, rescap12])
    yellowstone_rescap = statistics.mean([rescap13, rescap14, rescap15])
    montana_rescap = statistics.mean([columbia_rescap, missouri_rescap, yellowstone_rescap])

    swe_percentages = {
        'Columbia River Basin': columbia_swe,
        'Kootenai in Montana': swe1,
        'Flathead in Montana': swe2,
        'Upper Clark Fork': swe3,
        'Bitterroot': swe4,
        'Lower Clark Fork': swe5,
        'Missouri River Basin': missouri_swe,
        'Jefferson': swe6,
        'Madison': swe7,
        'Gallatin': swe8,
        'Headwaters Mainstem': swe9,
        'Smith-Judith-Musselshell': swe10,
        'Sun-Teton-Marias': swe11,
        'St. Mary-Milk': swe12,
        'Yellowstone River Basin': yellowstone_swe,
        'Upper Yellowstone': swe13,
        'Bighorn': swe14,
        'Tongue': swe15,
        'Powder': swe16,
        'Montana State-Wide': montana_swe
    }

    mpcp_percentages = {
        'Columbia River Basin': columbia_mpcp,
        'Kootenai in Montana': mpcp1,
        'Flathead in Montana': mpcp2,
        'Upper Clark Fork': mpcp3,
        'Bitterroot': mpcp4,
        'Lower Clark Fork': mpcp5,
        'Missouri River Basin': missouri_mpcp,
        'Jefferson': mpcp6,
        'Madison': mpcp7,
        'Gallatin': mpcp8,
        'Headwaters Mainstem': mpcp9,
        'Smith-Judith-Musselshell': mpcp10,
        'Sun-Teton-Marias': mpcp11,
        'St. Mary-Milk': mpcp12,
        'Yellowstone River Basin': yellowstone_mpcp,
        'Upper Yellowstone': mpcp13,
        'Bighorn': mpcp14,
        'Tongue': mpcp15,
        'Powder': mpcp16,
        'Montana State-Wide': montana_mpcp
    }

    wpcp_percentages = {
        'Columbia River Basin': columbia_wpcp,
        'Kootenai in Montana': wpcp1,
        'Flathead in Montana': wpcp2,
        'Upper Clark Fork': wpcp3,
        'Bitterroot': wpcp4,
        'Lower Clark Fork': wpcp5,
        'Missouri River Basin': missouri_wpcp,
        'Jefferson': wpcp6,
        'Madison': wpcp7,
        'Gallatin': wpcp8,
        'Headwaters Mainstem': wpcp9,
        'Smith-Judith-Musselshell': wpcp10,
        'Sun-Teton-Marias': wpcp11,
        'St. Mary-Milk': wpcp12,
        'Yellowstone River Basin': yellowstone_wpcp,
        'Upper Yellowstone': wpcp13,
        'Bighorn': wpcp14,
        'Tongue': wpcp15,
        'Powder': wpcp16,
        'Montana State-Wide': montana_wpcp
    }

    res_percentages = {
        'Columbia River Basin': columbia_res,
        'Kootenai in Montana': res1,
        'Flathead in Montana': res2,
        'Upper Clark Fork': res3,
        'Bitterroot': res4,
        'Lower Clark Fork': res5,
        'Missouri River Basin': missouri_res,
        'Jefferson': res6,
        'Madison': res7,
        'Gallatin': res8,
        'Headwaters Mainstem': res9,
        'Smith-Judith-Musselshell': res10,
        'Sun-Teton-Marias': res11,
        'St. Mary-Milk': res12,
        'Yellowstone River Basin': yellowstone_res,
        'Upper Yellowstone': res13,
        'Bighorn': res14,
        'Tongue': res15,
        'Powder': res16,
        'Montana State-Wide': montana_res
    }

    rescap_percentages = {
        'Columbia River Basin': columbia_rescap,
        'Kootenai in Montana': rescap1,
        'Flathead in Montana': rescap2,
        'Upper Clark Fork': rescap3,
        'Bitterroot': rescap4,
        'Lower Clark Fork': rescap5,
        'Missouri River Basin': missouri_rescap,
        'Jefferson': rescap6,
        'Madison': rescap7,
        'Gallatin': rescap8,
        'Headwaters Mainstem': rescap9,
        'Smith-Judith-Musselshell': rescap10,
        'Sun-Teton-Marias': rescap11,
        'St. Mary-Milk': rescap12,
        'Yellowstone River Basin': yellowstone_rescap,
        'Upper Yellowstone': rescap13,
        'Bighorn': rescap14,
        'Tongue': rescap15,
        'Powder': rescap16,
        'Montana State-Wide': montana_rescap
    }

    # pandas
    dict_list = [swe_percentages, mpcp_percentages, wpcp_percentages, res_percentages, rescap_percentages]
    df = pd.DataFrame(dict_list).transpose().fillna(-1).astype(int)
    df.columns = ['SWE', 'MPCP', 'WPCP', 'RES', 'RESCAP']
    df = df.where(df > 0, None)

    return df.to_html('templates/table.html', index=True, encoding='utf-8', classes='static/css/styles.css')
