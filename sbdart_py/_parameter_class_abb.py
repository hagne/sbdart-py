from sbdart_py.parameters import Parameter

class Parameters_abb(object):
    def __init__(self,para_dict_list):
        self.para_dict_list = para_dict_list

    @property
    def ABAER(self):
        return Parameter("ABAER", "abb", self.para_dict_list)

    @ABAER.setter
    def ABAER(self,value):
        Parameter("ABAER", "abb", self.para_dict_list).set_value(value)

    @property
    def ALAT(self):
        return Parameter("ALAT", "abb", self.para_dict_list)

    @ALAT.setter
    def ALAT(self,value):
        Parameter("ALAT", "abb", self.para_dict_list).set_value(value)

    @property
    def ALBCON(self):
        return Parameter("ALBCON", "abb", self.para_dict_list)

    @ALBCON.setter
    def ALBCON(self,value):
        Parameter("ALBCON", "abb", self.para_dict_list).set_value(value)

    @property
    def ALON(self):
        return Parameter("ALON", "abb", self.para_dict_list)

    @ALON.setter
    def ALON(self,value):
        Parameter("ALON", "abb", self.para_dict_list).set_value(value)

    @property
    def AMIX(self):
        return Parameter("AMIX", "abb", self.para_dict_list)

    @AMIX.setter
    def AMIX(self,value):
        Parameter("AMIX", "abb", self.para_dict_list).set_value(value)

    @property
    def BTEMP(self):
        return Parameter("BTEMP", "abb", self.para_dict_list)

    @BTEMP.setter
    def BTEMP(self,value):
        Parameter("BTEMP", "abb", self.para_dict_list).set_value(value)

    @property
    def CORINT(self):
        return Parameter("CORINT", "abb", self.para_dict_list)

    @CORINT.setter
    def CORINT(self,value):
        Parameter("CORINT", "abb", self.para_dict_list).set_value(value)

    @property
    def CSZA(self):
        return Parameter("CSZA", "abb", self.para_dict_list)

    @CSZA.setter
    def CSZA(self,value):
        Parameter("CSZA", "abb", self.para_dict_list).set_value(value)

    @property
    def DBAER(self):
        return Parameter("DBAER", "abb", self.para_dict_list)

    @DBAER.setter
    def DBAER(self,value):
        Parameter("DBAER", "abb", self.para_dict_list).set_value(value)

    @property
    def GBAER(self):
        return Parameter("GBAER", "abb", self.para_dict_list)

    @GBAER.setter
    def GBAER(self,value):
        Parameter("GBAER", "abb", self.para_dict_list).set_value(value)

    @property
    def IAER(self):
        return Parameter("IAER", "abb", self.para_dict_list)

    @IAER.setter
    def IAER(self,value):
        Parameter("IAER", "abb", self.para_dict_list).set_value(value)

    @property
    def IDATM(self):
        return Parameter("IDATM", "abb", self.para_dict_list)

    @IDATM.setter
    def IDATM(self,value):
        Parameter("IDATM", "abb", self.para_dict_list).set_value(value)

    @property
    def IDAY(self):
        return Parameter("IDAY", "abb", self.para_dict_list)

    @IDAY.setter
    def IDAY(self,value):
        Parameter("IDAY", "abb", self.para_dict_list).set_value(value)

    @property
    def IDB(self):
        return Parameter("IDB", "abb", self.para_dict_list)

    @IDB.setter
    def IDB(self,value):
        Parameter("IDB", "abb", self.para_dict_list).set_value(value)

    @property
    def IMOMA(self):
        return Parameter("IMOMA", "abb", self.para_dict_list)

    @IMOMA.setter
    def IMOMA(self,value):
        Parameter("IMOMA", "abb", self.para_dict_list).set_value(value)

    @property
    def IMOMC(self):
        return Parameter("IMOMC", "abb", self.para_dict_list)

    @IMOMC.setter
    def IMOMC(self,value):
        Parameter("IMOMC", "abb", self.para_dict_list).set_value(value)

    @property
    def IOUT(self):
        return Parameter("IOUT", "abb", self.para_dict_list)

    @IOUT.setter
    def IOUT(self,value):
        Parameter("IOUT", "abb", self.para_dict_list).set_value(value)

    @property
    def ISALB(self):
        return Parameter("ISALB", "abb", self.para_dict_list)

    @ISALB.setter
    def ISALB(self,value):
        Parameter("ISALB", "abb", self.para_dict_list).set_value(value)

    @property
    def ISAT(self):
        return Parameter("ISAT", "abb", self.para_dict_list)

    @ISAT.setter
    def ISAT(self,value):
        Parameter("ISAT", "abb", self.para_dict_list).set_value(value)

    @property
    def JAER(self):
        return Parameter("JAER", "abb", self.para_dict_list)

    @JAER.setter
    def JAER(self,value):
        Parameter("JAER", "abb", self.para_dict_list).set_value(value)

    @property
    def KDIST(self):
        return Parameter("KDIST", "abb", self.para_dict_list)

    @KDIST.setter
    def KDIST(self,value):
        Parameter("KDIST", "abb", self.para_dict_list).set_value(value)

    @property
    def KRHCLR(self):
        return Parameter("KRHCLR", "abb", self.para_dict_list)

    @KRHCLR.setter
    def KRHCLR(self,value):
        Parameter("KRHCLR", "abb", self.para_dict_list).set_value(value)

    @property
    def LWP(self):
        return Parameter("LWP", "abb", self.para_dict_list)

    @LWP.setter
    def LWP(self,value):
        Parameter("LWP", "abb", self.para_dict_list).set_value(value)

    @property
    def NF(self):
        return Parameter("NF", "abb", self.para_dict_list)

    @NF.setter
    def NF(self,value):
        Parameter("NF", "abb", self.para_dict_list).set_value(value)

    @property
    def NGRID(self):
        return Parameter("NGRID", "abb", self.para_dict_list)

    @NGRID.setter
    def NGRID(self,value):
        Parameter("NGRID", "abb", self.para_dict_list).set_value(value)

    @property
    def NOSCT(self):
        return Parameter("NOSCT", "abb", self.para_dict_list)

    @NOSCT.setter
    def NOSCT(self,value):
        Parameter("NOSCT", "abb", self.para_dict_list).set_value(value)

    @property
    def NOTHRM(self):
        return Parameter("NOTHRM", "abb", self.para_dict_list)

    @NOTHRM.setter
    def NOTHRM(self,value):
        Parameter("NOTHRM", "abb", self.para_dict_list).set_value(value)

    @property
    def NPHI(self):
        return Parameter("NPHI", "abb", self.para_dict_list)

    @NPHI.setter
    def NPHI(self,value):
        Parameter("NPHI", "abb", self.para_dict_list).set_value(value)

    @property
    def NRE(self):
        return Parameter("NRE", "abb", self.para_dict_list)

    @NRE.setter
    def NRE(self,value):
        Parameter("NRE", "abb", self.para_dict_list).set_value(value)

    @property
    def NSTR(self):
        return Parameter("NSTR", "abb", self.para_dict_list)

    @NSTR.setter
    def NSTR(self,value):
        Parameter("NSTR", "abb", self.para_dict_list).set_value(value)

    @property
    def NZEN(self):
        return Parameter("NZEN", "abb", self.para_dict_list)

    @NZEN.setter
    def NZEN(self,value):
        Parameter("NZEN", "abb", self.para_dict_list).set_value(value)

    @property
    def O3TRP(self):
        return Parameter("O3TRP", "abb", self.para_dict_list)

    @O3TRP.setter
    def O3TRP(self,value):
        Parameter("O3TRP", "abb", self.para_dict_list).set_value(value)

    @property
    def PBAR(self):
        return Parameter("PBAR", "abb", self.para_dict_list)

    @PBAR.setter
    def PBAR(self,value):
        Parameter("PBAR", "abb", self.para_dict_list).set_value(value)

    @property
    def PHI(self):
        return Parameter("PHI", "abb", self.para_dict_list)

    @PHI.setter
    def PHI(self,value):
        Parameter("PHI", "abb", self.para_dict_list).set_value(value)

    @property
    def PMAER(self):
        return Parameter("PMAER", "abb", self.para_dict_list)

    @PMAER.setter
    def PMAER(self,value):
        Parameter("PMAER", "abb", self.para_dict_list).set_value(value)

    @property
    def PRNT(self):
        return Parameter("PRNT", "abb", self.para_dict_list)

    @PRNT.setter
    def PRNT(self,value):
        Parameter("PRNT", "abb", self.para_dict_list).set_value(value)

    @property
    def QBAER(self):
        return Parameter("QBAER", "abb", self.para_dict_list)

    @QBAER.setter
    def QBAER(self,value):
        Parameter("QBAER", "abb", self.para_dict_list).set_value(value)

    @property
    def RHAER(self):
        return Parameter("RHAER", "abb", self.para_dict_list)

    @RHAER.setter
    def RHAER(self,value):
        Parameter("RHAER", "abb", self.para_dict_list).set_value(value)

    @property
    def RHCLD(self):
        return Parameter("RHCLD", "abb", self.para_dict_list)

    @RHCLD.setter
    def RHCLD(self,value):
        Parameter("RHCLD", "abb", self.para_dict_list).set_value(value)

    @property
    def SAZA(self):
        return Parameter("SAZA", "abb", self.para_dict_list)

    @SAZA.setter
    def SAZA(self,value):
        Parameter("SAZA", "abb", self.para_dict_list).set_value(value)

    @property
    def SC(self):
        return Parameter("SC", "abb", self.para_dict_list)

    @SC.setter
    def SC(self,value):
        Parameter("SC", "abb", self.para_dict_list).set_value(value)

    @property
    def SCLH2O(self):
        return Parameter("SCLH2O", "abb", self.para_dict_list)

    @SCLH2O.setter
    def SCLH2O(self,value):
        Parameter("SCLH2O", "abb", self.para_dict_list).set_value(value)

    @property
    def SOLFAC(self):
        return Parameter("SOLFAC", "abb", self.para_dict_list)

    @SOLFAC.setter
    def SOLFAC(self,value):
        Parameter("SOLFAC", "abb", self.para_dict_list).set_value(value)

    @property
    def SPOWDER(self):
        return Parameter("SPOWDER", "abb", self.para_dict_list)

    @SPOWDER.setter
    def SPOWDER(self,value):
        Parameter("SPOWDER", "abb", self.para_dict_list).set_value(value)

    @property
    def SZA(self):
        return Parameter("SZA", "abb", self.para_dict_list)

    @SZA.setter
    def SZA(self,value):
        Parameter("SZA", "abb", self.para_dict_list).set_value(value)

    @property
    def TAERST(self):
        return Parameter("TAERST", "abb", self.para_dict_list)

    @TAERST.setter
    def TAERST(self,value):
        Parameter("TAERST", "abb", self.para_dict_list).set_value(value)

    @property
    def TBAER(self):
        return Parameter("TBAER", "abb", self.para_dict_list)

    @TBAER.setter
    def TBAER(self,value):
        Parameter("TBAER", "abb", self.para_dict_list).set_value(value)

    @property
    def TCLOUD(self):
        return Parameter("TCLOUD", "abb", self.para_dict_list)

    @TCLOUD.setter
    def TCLOUD(self,value):
        Parameter("TCLOUD", "abb", self.para_dict_list).set_value(value)

    @property
    def TEMIS(self):
        return Parameter("TEMIS", "abb", self.para_dict_list)

    @TEMIS.setter
    def TEMIS(self,value):
        Parameter("TEMIS", "abb", self.para_dict_list).set_value(value)

    @property
    def TIME(self):
        return Parameter("TIME", "abb", self.para_dict_list)

    @TIME.setter
    def TIME(self,value):
        Parameter("TIME", "abb", self.para_dict_list).set_value(value)

    @property
    def TTEMP(self):
        return Parameter("TTEMP", "abb", self.para_dict_list)

    @TTEMP.setter
    def TTEMP(self,value):
        Parameter("TTEMP", "abb", self.para_dict_list).set_value(value)

    @property
    def UO3(self):
        return Parameter("UO3", "abb", self.para_dict_list)

    @UO3.setter
    def UO3(self,value):
        Parameter("UO3", "abb", self.para_dict_list).set_value(value)

    @property
    def UW(self):
        return Parameter("UW", "abb", self.para_dict_list)

    @UW.setter
    def UW(self,value):
        Parameter("UW", "abb", self.para_dict_list).set_value(value)

    @property
    def UZEN(self):
        return Parameter("UZEN", "abb", self.para_dict_list)

    @UZEN.setter
    def UZEN(self,value):
        Parameter("UZEN", "abb", self.para_dict_list).set_value(value)

    @property
    def VIS(self):
        return Parameter("VIS", "abb", self.para_dict_list)

    @VIS.setter
    def VIS(self,value):
        Parameter("VIS", "abb", self.para_dict_list).set_value(value)

    @property
    def VZEN(self):
        return Parameter("VZEN", "abb", self.para_dict_list)

    @VZEN.setter
    def VZEN(self,value):
        Parameter("VZEN", "abb", self.para_dict_list).set_value(value)

    @property
    def WBAER(self):
        return Parameter("WBAER", "abb", self.para_dict_list)

    @WBAER.setter
    def WBAER(self,value):
        Parameter("WBAER", "abb", self.para_dict_list).set_value(value)

    @property
    def WLBAER(self):
        return Parameter("WLBAER", "abb", self.para_dict_list)

    @WLBAER.setter
    def WLBAER(self,value):
        Parameter("WLBAER", "abb", self.para_dict_list).set_value(value)

    @property
    def WLINC(self):
        return Parameter("WLINC", "abb", self.para_dict_list)

    @WLINC.setter
    def WLINC(self,value):
        Parameter("WLINC", "abb", self.para_dict_list).set_value(value)

    @property
    def WLINF(self):
        return Parameter("WLINF", "abb", self.para_dict_list)

    @WLINF.setter
    def WLINF(self,value):
        Parameter("WLINF", "abb", self.para_dict_list).set_value(value)

    @property
    def WLSUP(self):
        return Parameter("WLSUP", "abb", self.para_dict_list)

    @WLSUP.setter
    def WLSUP(self,value):
        Parameter("WLSUP", "abb", self.para_dict_list).set_value(value)

    @property
    def XCH4(self):
        return Parameter("XCH4", "abb", self.para_dict_list)

    @XCH4.setter
    def XCH4(self,value):
        Parameter("XCH4", "abb", self.para_dict_list).set_value(value)

    @property
    def XCO(self):
        return Parameter("XCO", "abb", self.para_dict_list)

    @XCO.setter
    def XCO(self,value):
        Parameter("XCO", "abb", self.para_dict_list).set_value(value)

    @property
    def XCO2(self):
        return Parameter("XCO2", "abb", self.para_dict_list)

    @XCO2.setter
    def XCO2(self,value):
        Parameter("XCO2", "abb", self.para_dict_list).set_value(value)

    @property
    def XHNO3(self):
        return Parameter("XHNO3", "abb", self.para_dict_list)

    @XHNO3.setter
    def XHNO3(self,value):
        Parameter("XHNO3", "abb", self.para_dict_list).set_value(value)

    @property
    def XN2(self):
        return Parameter("XN2", "abb", self.para_dict_list)

    @XN2.setter
    def XN2(self,value):
        Parameter("XN2", "abb", self.para_dict_list).set_value(value)

    @property
    def XN2O(self):
        return Parameter("XN2O", "abb", self.para_dict_list)

    @XN2O.setter
    def XN2O(self,value):
        Parameter("XN2O", "abb", self.para_dict_list).set_value(value)

    @property
    def XNH3(self):
        return Parameter("XNH3", "abb", self.para_dict_list)

    @XNH3.setter
    def XNH3(self,value):
        Parameter("XNH3", "abb", self.para_dict_list).set_value(value)

    @property
    def XNO(self):
        return Parameter("XNO", "abb", self.para_dict_list)

    @XNO.setter
    def XNO(self,value):
        Parameter("XNO", "abb", self.para_dict_list).set_value(value)

    @property
    def XNO2(self):
        return Parameter("XNO2", "abb", self.para_dict_list)

    @XNO2.setter
    def XNO2(self,value):
        Parameter("XNO2", "abb", self.para_dict_list).set_value(value)

    @property
    def XO2(self):
        return Parameter("XO2", "abb", self.para_dict_list)

    @XO2.setter
    def XO2(self,value):
        Parameter("XO2", "abb", self.para_dict_list).set_value(value)

    @property
    def XO4(self):
        return Parameter("XO4", "abb", self.para_dict_list)

    @XO4.setter
    def XO4(self,value):
        Parameter("XO4", "abb", self.para_dict_list).set_value(value)

    @property
    def XRSC(self):
        return Parameter("XRSC", "abb", self.para_dict_list)

    @XRSC.setter
    def XRSC(self,value):
        Parameter("XRSC", "abb", self.para_dict_list).set_value(value)

    @property
    def XSO2(self):
        return Parameter("XSO2", "abb", self.para_dict_list)

    @XSO2.setter
    def XSO2(self,value):
        Parameter("XSO2", "abb", self.para_dict_list).set_value(value)

    @property
    def ZAER(self):
        return Parameter("ZAER", "abb", self.para_dict_list)

    @ZAER.setter
    def ZAER(self,value):
        Parameter("ZAER", "abb", self.para_dict_list).set_value(value)

    @property
    def ZBAER(self):
        return Parameter("ZBAER", "abb", self.para_dict_list)

    @ZBAER.setter
    def ZBAER(self,value):
        Parameter("ZBAER", "abb", self.para_dict_list).set_value(value)

    @property
    def ZCLOUD(self):
        return Parameter("ZCLOUD", "abb", self.para_dict_list)

    @ZCLOUD.setter
    def ZCLOUD(self,value):
        Parameter("ZCLOUD", "abb", self.para_dict_list).set_value(value)

    @property
    def ZGRID1(self):
        return Parameter("ZGRID1", "abb", self.para_dict_list)

    @ZGRID1.setter
    def ZGRID1(self,value):
        Parameter("ZGRID1", "abb", self.para_dict_list).set_value(value)

    @property
    def ZGRID2(self):
        return Parameter("ZGRID2", "abb", self.para_dict_list)

    @ZGRID2.setter
    def ZGRID2(self,value):
        Parameter("ZGRID2", "abb", self.para_dict_list).set_value(value)

    @property
    def ZOUT(self):
        return Parameter("ZOUT", "abb", self.para_dict_list)

    @ZOUT.setter
    def ZOUT(self,value):
        Parameter("ZOUT", "abb", self.para_dict_list).set_value(value)

    @property
    def ZPRES(self):
        return Parameter("ZPRES", "abb", self.para_dict_list)

    @ZPRES.setter
    def ZPRES(self,value):
        Parameter("ZPRES", "abb", self.para_dict_list).set_value(value)

    @property
    def ZTRP(self):
        return Parameter("ZTRP", "abb", self.para_dict_list)

    @ZTRP.setter
    def ZTRP(self,value):
        Parameter("ZTRP", "abb", self.para_dict_list).set_value(value)

