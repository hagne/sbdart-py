from sbdart_py.parameters import Parameter

class Parameters_aerosols(object):
    def __init__(self,para_dict_list):
        self.para_dict_list = para_dict_list

    @property
    def aerosol_wavelength_exponent(self):
        return Parameter("aerosol_wavelength_exponent", "name", self.para_dict_list)

    @aerosol_wavelength_exponent.setter
    def aerosol_wavelength_exponent(self,value):
        Parameter("aerosol_wavelength_exponent", "name", self.para_dict_list)._set_value(value)

