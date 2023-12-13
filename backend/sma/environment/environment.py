
import json
from datetime import datetime, timedelta

import time
from sma.agent.agent import Agent
from sma.environment.vehicle import Vehicle
from json import JSONEncoder


def date_to_datetime(dateStr):
    try:
        # 2023-06-14T15:39:20
        date_time_obj = datetime.strptime(dateStr[:19], "%Y-%m-%dT%H:%M:%S")

    except Exception as e:
        print('erreur ', e, type(dateStr), dateStr[:19])

    return date_time_obj


class Environment:
    def __init__(self):
        self.width=500
        self.height=500
        self.items=[]
        v = Vehicle()
        self.agents=[Agent(type="Driver",vehicle=v, line="ycjuGqyy^yktimdBIRAINAKLAKGAIEAIIAIGACQA?UADq@C@]ADc@ABg@ABg@ABg@ABi@ABk@ADi@ABk@ABi@ADi@ABi@ABi@A@k@A?i@AAg@AAg@AIcACG[AC[AEWA@SAEQAIKAMIAKMAMUAMYAO]AQa@AU_@AU_@AW_@AWa@AU_@AY_@AW_@AW]Ai@{@CQYAMSAGSAEOACGA?CAA?A?EACCACGAWNAMLAMTAQ\\AO\\ASb@ASh@AUj@AWj@AWj@AUh@AUd@AOb@AQ\\AO\\AMZAKTAIPAGLAGJAEDCABAA@AA@ACDCA?A?@A??C??A??AABACBAEDAGBAWPCODAODAQDASFAQDAOBAM@AIIAAUAE[AI_@AEc@AIi@AGk@AGo@AIs@AEu@AEw@AAw@A@y@AB}@AF{@AH}@AH{@AJ{@AN{@AP{@APy@ATy@AXw@A\\w@A\\s@A^q@A^o@Ab@k@Ad@k@AlAqACb@i@Ad@i@Ab@g@Ad@i@Ad@g@Ab@i@Ad@g@Ab@i@Ad@g@AfAoACb@g@Ab@g@Ab@c@A^c@A`@a@A\\_@A\\]AX[AXYAV[ARYA^m@CLOALKANEANAANAAN?AN@AL@AJFANJC@@AD?AA^AF?ADCA@EACGA??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A??A?AA??A?@A??A??A??A??A?AA@AA?CA@CAEGA@AAACA[MAEKACOA?SA?UA?WAEWAIUAMOAOIAQAAe@PCQJASFAU?AYEAm@[CSUAQUAOYAMYAIWAISAI_@CCIAEGACGAEIAEKAGOAKOAIUAOWAQWAQ[AS[ASYAU[AM_@AYQASWASWAUUAUWAWSAUUAUSAUUAUQAUSASUAUSAWUAUSASSAQQAQOAOSAMSAKWAGWAAYA?WADWAVe@CNKAPGAPAAPDAPHANNAJTADZABZAA\\AGbACEd@AEd@AGf@AGd@AGf@AGf@AGj@AGj@AGj@AIl@AGl@AQ|ACIp@AGr@AIv@AIx@AIz@AI~@AK~@AM`AAObAAOfAAOfAAQhAAe@xCCSlAAQlAAUnAASnAAk@bDCWnAAWrAAWpAAWrAAWrAAYpAAYpAAWpAAWpAAWnAAYpAAWnAAWnAAWnAAWpAAUnAAUpAASpAASnAAQpAAQpAAOrAAOpAAOrAAKrAAYjDCMtAAIvAASnDCItAAGvAAKvAASnDCIxAAKvAAIxAAIxAAWtDCMzAAKxAAKzAAKzAAKxAAMzAAKxAAMzAAMxAAYpDCMxAAMvAAMtAAOvAAMvAAOtAAQtAAQtAAQrAAQrAAQrAASrAASpAASpAAi@bDCUpAAUpAAWpAAUpAAWpAAYpAAWnAA[nAAYpAA[pAA[nAA[nAA[nAA]nAA]nAA]nAA]lAA_@nAA_@lAA_@lAAa@lAAa@jAAa@jAAa@lAAaAvCCc@jAAc@lAAc@jAAc@hAAc@hAAe@jAAe@hAAe@fAAc@hAAe@fAAe@fAAe@fAAkAjCCe@bAAe@bAAe@`AAgAbCCc@bAAc@`AAc@bAAc@bAAc@dAAe@bAAc@dAAe@bAAe@dAAc@dAAe@dAAe@dAAkAlCCe@fAAe@fAAkApCCc@hAAc@fAAa@jAAgArCCc@jAAa@lAAc@jAAc@lAAc@lAAe@lAAc@nAAc@pAAc@nAAe@pAAc@nAAc@nAAc@lAAc@nAAa@lAAc@jAAc@lAAc@lAAc@jAAc@lAAc@jAAe@jAAc@hAAe@jAAe@hAAkArCCe@fAAg@dAAg@fAAe@dAAg@dAAg@bAAg@dAAg@bAAg@bAAg@bAAi@bAAi@bAAi@`AAi@bAAqAbCCi@`AAg@`AAi@~@Ag@~@Ai@`AAg@~@Ag@~@Ag@~@Ag@~@Ag@~@Ag@~@Ai@`AAi@~@Ag@`AAsA`CCg@`AAi@bAAi@`AAg@bAAi@`AAqAfCCi@bAAe@bAAg@bAAg@`AAg@`AAe@`AAc@~@Ac@~@Ac@~@Aa@~@A_@~@Aa@~@A_@`AA_A~BC]~@A]~@A]`AA]`AA]`AA]bAA[dAA]dAA[dAA[dAA[dAA[fAAu@nCCWhAAYhAAWhAAWjAAUjAAUjAAUlAASlAASlAAQlAAe@|CCQlAAOnAAQnAAOlAAOnAAOlAAMnAAMlAAMlAAMnAAKlAAMlAAKjAAMlAAKlAAMjAAMlAAKhAAKjAAMhAAKhAAKfAAKfAAMfAAKbAAK`AAK`AAK~@AM|@AUvBCIx@AOv@AMr@AOr@AMn@AYxACKj@AKj@AKf@AKf@AIb@AGb@AG\\Ah@r@AGVAETAGb@CCNAANACPAETAi@PAWTAG`@AId@AIj@AKt@AMp@AOv@AQx@AQ|@AQ~@AQ`AAQbAAQdAASdAAQdAAQdAAQdAAQdAAQbAAQbAASdAAQfAAQdAAc@lCCSfAAQdAASfAAQfAAQfAASfAAQfAASfAAShAASjAAShAASjAAQjAASjAAe@vCCSjAAQlAASjAAQlAAQjAAQlAAOjAAQlAAQnAAOnAAOnAAOpAAQrAAOpAAOpAAOrAAMnAAOpAAOnAAMnAAMnAAOpAA]`DCMpAAOnAAMpAAMnAA]~CCMnAAMnAAMnAAOnAAMnAAMlAAOlAAMlAA[zCCMlAAOlAAMlAAOlAAOlAAMlAAQlAAQlAAQlAAc@xCCQlAASnAASjAASnAASlAAUjAAUjAAUjAAm@tCCWjAAWjAAWjAAWjAAWjAAWjAAYlAAYlAAYlAA[jAAYlAAYnAA[lAA[lAAYlAA[jAA[jAAYjAAYjAAYjAAYlAAu@xCC[jAAYjAA[lAAw@xCC[nAA[lAA[nAA[nAA[nAA]nAA[nAA[nAA[pAAYnAA[nAA[pAAw@`DC]nAA[lAA[nAA]nAAy@`DC]nAA]nAA]pAA]nAA{@bDC_@pAA]pAA_@nAA_@nAA]nAA_@lAA]nAA_@lAA_@lAA_@nAA_@lAA_@nAAa@nAA_@lAA_@pAA_@lAAa@nAA_@pAA_@lAA_@jAA_@jAA]hAA]hAA]jAA}@tCC]jAA_@jAA]jAA_AvCC_@jAA]lAA_@jAA]lAA_@jAA_@lAA_@lAA_@jAA]lAA_@lAA_@jAA_@lAAa@nAA_@lAA_@nAAa@lAA_@lAA_@nAA}@xCC_@jAA]jAA_@jAA]jAA]jAA_@hAA]jAA_@jAA]jAA_@jAA]jAA_@jAA]hAA_@jAA_@jAA]jAA]jAA_@jAA[hAA]hAA]hAA]hAA]hAA]fAA]fAAy@pCC[fAA[fAA[hAA[fAA[hAAYfAA[hAA[hAAYfAA[hAAYhAAYhAAYjAAWjAAq@xCCYlAAWnAAWnAAYlAAWnAAWpAAWpAAWnAAWnAAWpAAWpAASnAAWrAAUpAAUpAAUpAAk@bDCSpAAUpAAUpAASpAAUpAASpAASpAASnAASpAASpAASnAASpAASpAAQnAASnAAQpAASnAASnAAQnAASnAAg@`DCSnAASnAASlAASpAASpAASpAAUnAAUnAAUnAAUnAAUlAAWnAAUlAAWlAAWlAAWlAAWjAAYlAAYjAAWlAAYjAAYjAAYjAAs@rCC[hAAYhAA[fAA[fAA[dAA[fAA]dAA]fAA]fAA]dAA]dAA]fAA_@bAA_AhCC_@bAA_@bAAa@bAA_@bAAa@bAAa@`AAc@`AAa@bAAa@~@Ac@`AAa@~@Ac@|@Ac@|@Aa@|@AeAxBCa@z@Aa@z@Aa@z@Ac@z@Aa@x@Aa@x@Aa@x@Aa@x@Aa@v@AaArBCa@t@A_AlBC_@t@A]t@A_@t@A_@t@A]t@A_@r@A]r@A]r@A]t@A_@r@A]r@A]r@A]t@A[r@A]p@Aw@dBC]p@AYr@A[p@A[p@A[p@Aw@dBC[p@A[r@A[p@AYr@A[p@AYn@A[p@AYp@AYp@A[r@AYp@A[p@AYr@AYp@AYr@AYp@AYr@AYr@AWr@AYp@AYr@AYr@AWr@AYr@Aq@fBCWr@AYr@AWr@AYr@AWt@AWr@AWt@AWr@AYr@AWt@AWr@AWr@AWt@AWr@AUr@AWt@AWt@AWr@AWt@AWt@AWt@Am@hBCWt@AWt@AWr@AWt@AWt@AUt@AWr@AWt@AWr@AUt@Ao@jBCWr@AWt@AWt@AUr@AWt@AWt@AWr@AWt@AWt@AWr@AWr@AWt@AWr@AYt@AWr@AWr@AYr@AWr@AYr@AWr@AYr@AWp@AWr@AYr@AWr@As@hBCYt@A[t@AYt@A]t@AYt@A[r@A]t@A[r@A[t@A[r@A]r@A[t@A]r@A]r@Ay@hBC]r@A]t@Aa@r@A]r@A}@fBC_@r@A]r@A_@p@Aa@r@A]r@A_@r@A_@p@A_@p@A_@r@Aa@r@A_@p@A_@r@A_@p@A_@r@Aa@p@A_@p@AcAdBCa@r@Aa@r@Aa@r@AeAfBCa@r@Aa@r@Ac@t@Aa@r@Aa@r@Aa@p@A_@r@Aa@p@Aa@p@A_@p@AaAbBCa@p@A_@n@A_@r@Aa@n@A_@p@Aa@r@Aa@p@A_@p@A_@r@A_@n@Aa@n@A_AbBC_@p@A_@r@A_@p@A]r@A_@r@A_@r@A{@fBC]t@A]p@AYp@AYp@A[p@A[p@AYr@AYp@As@dBCYr@AWr@AWr@AWr@AWr@AWr@AWt@AUr@AWt@AUt@AUt@Ai@lBCUt@ASv@ASv@Ai@lBCQv@ASv@AQv@ASv@AQv@AOr@AOt@AMr@AOr@A_@hBCMt@AOv@AMt@AOv@AMx@AKv@AKz@AMz@AKx@AMz@AKz@AWtBCK|@AK|@AK|@AI|@AK|@AI~@AK|@AI|@AI|@AS~BCG~@AI|@AI~@AG~@AI~@AI~@AG|@AG|@AI|@AGz@AGz@AGz@AIx@AEz@AGx@AGz@AGx@AIx@AEv@AGx@AGv@AGx@AGv@AGx@AGv@AGv@AGv@AEv@AGt@AGv@AGv@AGt@AGv@AGv@AGt@AGv@AGt@AGv@AIv@AEt@AGv@AGt@AGt@AGv@AGt@AGt@AOlBCGt@AGt@AEt@AGr@AGr@AGr@AGp@AGn@AGn@AGn@AGn@AI~ACEn@AEl@AEl@AGn@AEn@AEl@AKzACGn@AEn@AGl@AEn@AGl@ACj@AEj@AGh@AKrACEd@AEb@AE`@AE^AE^AE\\AC^AEZAC\\AC\\AC\\AC\\AC\\AE^AE^AG`ACE`@AE`@ACb@AE`@AIfACEb@AC`@AEd@AEb@AEb@AEb@AC`@AE`@ACb@AC`@AIdACC`@AE`@AC^AE^AC\\AC\\ACXACXACTAATACRAARAAPAALAAJAAHAAJAAJAALAALAAHACNC?FAAHA?FA?FA?DA?@A@?A??A??A??G??A??A??A??A?BA?HA@HAGRCDVAZGAHFAFFAFFA@HABBA??C@?A@?AA?A??A?@A?AA??A??A??A??CB@ADDAHDAJHALHA`@\\CNLAPNARHARFARBAT@AT?ATAATAAl@CCVCAVAAn@ECVAATAATAAV?APAARAAT?ARAAP?APAANAAN?A\\CCL?AJAAH?AHAAD?ADAAB?A@?AD?C??A??A??A?AA??A??A??I??A??A??A@CADAAPBCJ?AL?ANAAN?APAAP?ARAARAATAATAATAATAATAAT?ATAATAARCATAAl@CCRAAT?ATCATAARAARCARAARAAb@BCNHALJAHRAHRAFVAFVAFXAFXAHZAJZAHVAHVAHTAFPAFJABJABFABDABDABDA@DA@DA@BA@BA@BA?@A@@A??A??A??AA@A@?A@@C??A??A??A??A??E??A??A??A??A??ADHCBHANZCHPAJNANNANNARLARLARPATPARTARXAPXAL^AL`@AJb@AXjACJf@ALf@ALh@ALh@ALj@ANj@ANj@ANl@A^~ACPn@APn@ANp@APn@ANp@ANp@ALp@ALp@ALr@AXhBCHt@AThBCHt@AHt@AFt@ADr@ADt@AHfBCBr@ADr@ADt@ABr@ADt@AFr@ABv@ADt@ADv@ABr@ADt@ABr@ABr@ABr@ABr@ABp@ABr@ADp@ABn@ABp@ADn@ABn@ADl@ABn@ADl@ABl@ADj@ADn@ADn@ADn@ABl@ADn@ABn@ADl@ABj@ABh@ABj@ABh@ABj@ABl@ABl@ADl@ABj@ABj@ABj@ADj@ADj@ABl@ADn@AF~ACDp@ABp@ABn@ADn@ADl@ABn@ABl@ABl@ABn@ABn@ADn@ABn@AH~ACBn@ADn@ABn@ABn@AH`BCBn@ABn@ABn@ADp@ABn@ABp@ADn@ABn@ADn@ABn@ABp@ABp@ABn@ADn@ABp@ABn@AH`BCBn@ADn@ABp@ADn@ABn@ABn@ABp@ADp@ABn@ABn@A@n@ABn@ABp@ABp@ABn@ABn@ADn@ABp@AH~ACBn@ABn@ADn@ABp@AD~ACBp@ABn@ABp@ABn@ADn@ABp@ADn@ADn@ADn@AG`BCCl@AQvACKf@AMd@ASb@AS`@AW\\AYZAYXA_@TA]PA]NA_@LA_@FA]HA_@HA_@FA_@HA]NA_@DA_@DA]DA_@BA}@FC]@A]BA[BA]@A[@A[@A[@AY?AY?AW?AWAAq@?CWAAWCAYAAWAAUAAU?ASAAQ?AKAAIAAE?AE?AAAAA?C?AAC?C"),
                     Agent(type="Rider",line="owiuGgc}^omtimdB@DACCABC?A?AA@A??A?BA?@A?@A??A??AA?A?AAAAACAA@@A@?A?@AAAA??A??A?@A?FA?AA?@AA?A?DAAAA@?AC@A?@AA@AA@A@?A?BAC@A?BAADAABACDAADAABACBAABAC@AC@AEBACDAABAA?AABAABAABAABA?@A?@A?@A@BAA@A?BAA?A?@A?@AABAC@AA@A?AA@@A?@A@@A?@A?@A@BA@BA?BA?@A?@A?@A?@AA?A@BA@?A?@A??A??A??A??A??A??A??A?@A??A??A??A??A?@A??A@BA?@A?@AA?A?@A??A??A??A??A?AA??A?AA?@A??AAAAA?A??A??A?@A??A??A??A??A??AA?A??AA?AA@AA@A?@AA?A??A??A??A??A??A??A??A??A??A??AA?AABA?@AA@A?AA??A??A??A?@AA@AA?A??A??A??A?AA??A?AA@@A?@A??A??A@@A?@A??ADEABAA@AA@?A@?A@?A??A??A??A@?A@AA@CA?AA??A??A??A??A??A??A@?A?AA??A?AA@?A??A?AA?CA?CAAGAAEACEACEAI?ACCAEGAAKAAMA?OACSAESAEUAMOAMMAUCAQAAUDASNASDAWFAWGAUMAUQAYQAQSAO[AKYAKWAKUAGOAGKAEKAEIAEIAEKAGMAIOAISAMSAMWAQYAQWASYAQ[AQ[AS[ASWASWAUWAUWAWUAWQAWSAWUAUSAUUAUUAUUAUSAUUAUSASSAQQAOSAOSAMSAOSAEYAAQA@MA@SABSAFQAJOAJMALGAJEAN?AP?ALLALNAR\\ADb@AAf@ACf@AEd@AEd@AEf@AEd@AGh@AGh@AGh@AGh@AGf@AIj@AGh@AGj@AIt@AIt@AIt@AEp@AO`AAO~@AM`AAM`AAM`AAO`AAMbAAQdAAOlAAQnAAQjAASjAASnAASnAAShAASlAAWjAASnAASpAAUrAAWtAAWvAAYvAAYxAA[|AA[|AAYzAAcBlIGyCpPQmAlF?G~@A?pAAInAAGvAAIrAAMrAAKrAAIrAAIlAAItAAItAAI~AAKbBAGvAAHrAAIrAAIvAAKxAAIrAAKtAAItAAOzAAK`BAMdBAIxAAGxAAKxAAKvAAMxAAMrAAMtAAMrAAMtAAMtAAMtAAOpAAOrAAQrAAQrAASrAAQlAASlAAUvAAUvAASxAAUvAAWxAAW|AAUxAAUxAAUxAAUtAAa@pAAYpAAWlAA[lAAWhAA[lAA[lAA[jAA]pAA]jAA]jAA]hAA_@lAAa@lAA_@lAA_@fAA_@jAAa@jAAc@jAAa@jAAe@lAAg@nAAg@tAAg@nAAe@jAAg@nAAg@lAAg@nAAi@jAAk@rAAg@nAAg@hAAg@hAAe@dAAc@bAAa@|@Aa@~@Ac@~@Ac@~@Ac@bAAc@~@Ac@~@Aa@~@Ac@~@Aa@~@Ac@dAAe@bAAe@`AAe@`AAg@fACg@dAAi@fAAg@fAAe@hAAe@jAAc@hAAa@hAA[hAA]fAA_@hAAe@fAA_@fAA_@jAAe@jAAc@lAAc@lAAc@nAAc@lAAc@lAAa@pAAc@rAAa@lAAe@lAAg@pAAe@nAAe@nAAe@lAAc@lAAc@nAAe@nAAc@pAAc@jAAc@jAAc@hAAe@lAAc@lAAc@jAAe@hAAk@~@Ae@fAAi@jAAe@`AAg@`AAc@|@Ac@~@Ag@bAAg@`AAg@`AAg@bAAe@`AAe@bAAi@~@Ak@dAAk@`AAi@~@Ag@|@Ag@|@Ak@~@Ai@z@Ai@z@Ak@|@Ai@v@Ak@|@Ag@~@Ai@x@Ag@|@Ai@z@Aa@fAAi@|@Ae@~@Ag@z@Ae@z@Ag@|@Ae@|@Ae@~@Ag@|@Ag@~@Ai@bAAi@`AAg@bAAi@bAAg@bAAe@|@Ac@|@Ac@|@Ae@bAAc@`AAa@|@Aa@`AAa@~@A_@|@A_@|@A_@bAA]`AA_@bAA]`AA_@dAA]fAA[bAA_@hAA]dAA[hAA[fAA[hAAYdAAWdAAWbAAWfAAWfAAU`AAUdAAS`AASfAAUhAAYzAASdAASjAAQfAAwAf@A_@dAAYbAAlAtBAQlAAMbAAMfAAMfAAOnAAMrAAOxAA{A|AAMfBAOtAAMtAAMtAAMhAAKrAAKzAAKnAAInAAIjAAGjAAGjAAGdAAEbAACbAAEfAACjAAGjAAEz@AGx@ACt@AEv@AQp@AOr@AMp@AKh@AMn@AMp@AKl@AMn@AId@AIf@AIn@AGd@ACZAIXACZACZAE^AEd@ACPAETAEHAQd@ACJACTAEXAEZAIf@AIl@AGf@AKj@AKt@AKt@AMz@AOz@AO|@AUlAAShAAQbAAS|@AQ|@Ai@vBCSbAAWdAAShAAWxAAOfAAQbAAUfAAOfAAUjAAShAAUhAAWlAAShAAWnAAQlAASjAASpAASlAASnAASrAASnAAQpAASnAASnAAQjAAQlAAQlAAQlAAOfAAOfAAOhAAMnAAOnAAMpAAQpAAOpAAOrAAOrAAQrAAQrAAOrAAMnAAMpAAMrAAMrAAOvAAO|AAM|AAM~AAM`BAK|AAKvAAQvAAQrAAOvAAOrAAOpAAOpAA]`DCOpAAOlAASzAAQrAAQrAAUjBAUhBAUhBApAnDAeCt@AQ|AAtB`BAoC\\AdBvCAWnAA??e@oTfv@M]`AA[`AAc@~@Aa@bAA_@|@A[`AA[x@AYn@ASf@AO`@AUh@A[dAAYr@AU~@A_@x@A]t@A_@v@A[t@A[r@A[p@A]r@A]v@A]t@AYp@AWr@AYx@AYv@A[x@Ag@jAAi@fAAg@~@Ae@`AAa@`AA??i@pClKi@pHzOAc`AdzBUgA~BA_A`AAq@n@Ag@n@Ac@l@Ag@ZAe@ZAg@h@AEtBA{@d@A]bDA_AxCA{AdFA}BrHA{C~JA??e@gChJAeEjQ_@{Mrs@QSvBAS`BAO|AAU`BA_@XA_@v@AQhAAWdAAUdAAWx@ASz@ASnAAw@BAFnFAOrAAKhBAULAUhAAItBAIpBAMjBA{@hIGQjAAShAASlAAShAASpAAUlAAUlAASdAAUlAAUhAAUhAAUhAAWlAAWdAAUfAAWfAAWfAAWfAAWdAAYfAA[dAA[hAA[hAAYhAAWhAA[dAA[dAA[dAA]fAA]fAA_@jAAa@jAA_@fAA]dAAa@hAA[z@Aa@jAA_@fAA_@fAAa@hAA_@fAA]fAA]`AA[n@ASx@ASbAAzAnDAUbAA[z@AUl@A[p@A[r@A]t@Ac@t@Ag@x@AwArBCm@z@Ae@~@Ae@bAAg@|@Ag@r@Ak@h@Ai@x@Ae@x@Ac@r@Ac@t@Ae@n@Aa@n@Aa@p@A_@t@Aa@t@Aa@r@A_ANA]x@A[r@A[t@A]r@A[p@Aa@z@A_@v@A]v@A[x@A[v@AQx@AIr@A@^A?f@AAh@Ao@pEAmC}AA[p@A]n@A_@n@A[p@A[p@A[p@AYp@A[p@A]p@A]r@A]n@AYp@A[r@A[t@AYr@AYt@A_@p@A_@j@AYp@AYj@A[n@A[l@A]n@A[l@A]t@A]t@A_@v@A]r@A[r@AWn@AUt@AYt@AUt@AYv@AWv@AYv@AYv@AWt@AWv@AWv@AWt@AWr@AUp@AWn@AWp@AUr@AUr@AUr@AUx@A[x@AUt@AWx@AWt@AWt@AUv@ASv@AUv@AUt@AUp@AYp@AUr@AWt@AWl@AYr@AWp@AUp@AUt@AWp@AWt@AYt@AWt@AYt@AWt@AYv@AYv@A[v@AWt@AYv@AYr@AWp@AWr@AYr@AYr@AWp@AWr@AWp@AYt@AYr@A[v@A[v@A[t@A[t@A[r@A[r@AYr@A]t@A]r@A[t@A]r@A]n@A[n@A]p@AYp@A]r@A[r@A[p@A]r@A_@r@A_@r@Aa@t@Aa@t@A_@t@A_@r@Aa@v@Ac@p@Aa@r@Ac@r@A_@n@A_@r@Aa@r@Aa@r@Aa@r@A_@p@Ae@l@Ac@j@Ae@h@Aa@|@Ag@z@Ag@|@Ai@~@Ag@z@Ai@`AAi@|@Ae@z@Ae@x@Ae@v@Aa@r@Ac@t@AWb@Ao@fAAe@x@Ag@|@Ae@t@A_@x@A_@|@Ag@v@Ae@`AAe@~@Ae@x@Ac@v@Ag@p@Ac@n@A_@f@A{JlNUA@?qAjBE???A?????y@lAEnAdf@{@}Uli@e@aEdL?yBdT_@k@zACf@`CA?d@AQ`AAEv@AEp@AX|@A_AHAAVACd@AMfCAK|@AObAAI|@AG~@AGx@ACn@AGz@AGv@A@|@ABfAAGfAAKhAAIlAAIhAAKjAAKlBA?TAKxBAdC|@ABj@AL`DARfAAZnAADfAA?NAB`@A@^O???oE`BGsD`D]{@z@?cFhEs@?@?j@znAwCMFAGAAGKAEBACAAA@A@BA?@AA@AA@A?BA?BA?@AABA??A?@A?@A?@AC@A?@AA?AA?A??A?AA??AA?A??A??A??AA?A@?AA?A??AA?A?@AA?AA?A?@AA?A??A??A@?AA@A??AA@AA@A?@AA?AA@AA?AA@AA?AA@A??AA?AA?AA?AA?A??AAAAA@A??AA?AA?AA@A?@AA?A@?A??A??A??A??A?AAA?AA?AA?AAAA??AA?AA?A")
                     ]
        self.tic_min=min([date_to_datetime(i.body.path[0][2]) for i in self.agents])
        self.tic=self.tic_min
        self.tic_max=max([date_to_datetime(i.body.path[len(i.body.path)-1][2]) for i in self.agents])

    def computePerception(self,agent):
        perceptions = []
        for a in self.agents:
            if a.uuid != agent.uuid:
                if agent.body.fustrum.inside(a.body,agent.body):
                    perceptions.append(a.body)
        a.perceptionsAgent=perceptions
        perceptions=[]
        for i in self.items:
            if agent.body.fustrum.inside(i,agent.body):
                perceptions.append(i)
        a.perceptionsItem=perceptions


    def computeDecision(self,agent):
        agent.doDecision()

    def applyDecision(self,agent):
        agent.body.update(self.tic)
        
    def run(self,tic):
        self.tic+=timedelta(seconds=tic)
        if self.tic > self.tic_max:
            self.tic=self.tic_min

        for a in self.agents:
            self.computePerception(a)
            self.computeDecision(a)

        for a in self.agents:
            self.applyDecision(a)



