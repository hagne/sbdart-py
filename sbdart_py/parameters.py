def get_param_descriptions():
    param_descriptions = [
    {'abb': 'ABAER',
     'name': 'aerosol_wavelength_exponent',
     'category': 'not_selected',
     'description': """Wavelength (Angstrom model) exponent used to extrapolate
          BLA extinction efficiency to wavelengths outside the
          range of WLBAER [Qext ~ (lambda)^(-abaer)].  This parameter
          is only operative when IAER=5.  (default=0)"""},
    {'abb': 'ALAT', 'name': 'define_it_1', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ALBCON', 'name': 'define_it_2', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ALON', 'name': 'define_it_3', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'AMIX', 'name': 'define_it_4', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'BTEMP', 'name': 'define_it_5', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'CORINT', 'name': 'define_it_6', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'CSZA', 'name': 'define_it_7', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'DBAER', 'name': 'define_it_8', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'GBAER', 'name': 'define_it_9', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'IAER', 'name': 'define_it_10', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'IDATM', 'name': 'define_it_11', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'IDAY', 'name': 'define_it_12', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'IDB', 'name': 'define_it_13', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'IMOMA', 'name': 'define_it_14', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'IMOMC', 'name': 'define_it_15', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'IOUT', 'name': 'define_it_16', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ISALB', 'name': 'define_it_17', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ISAT', 'name': 'define_it_18', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'JAER', 'name': 'define_it_19', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'KDIST', 'name': 'define_it_20', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'KRHCLR', 'name': 'define_it_21', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'LWP', 'name': 'define_it_22', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'NF', 'name': 'define_it_23', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'NGRID', 'name': 'define_it_24', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'NOSCT', 'name': 'define_it_25', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'NOTHRM', 'name': 'define_it_26', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'NPHI', 'name': 'define_it_27', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'NRE', 'name': 'define_it_28', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'NSTR', 'name': 'define_it_29', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'NZEN', 'name': 'define_it_30', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'O3TRP', 'name': 'define_it_31', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'PBAR', 'name': 'define_it_32', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'PHI', 'name': 'define_it_33', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'PMAER', 'name': 'define_it_34', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'PRNT', 'name': 'define_it_35', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'QBAER', 'name': 'define_it_36', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'RHAER', 'name': 'define_it_37', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'RHCLD', 'name': 'define_it_38', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'SAZA', 'name': 'define_it_39', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'SC', 'name': 'define_it_40', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'SCLH2O', 'name': 'define_it_41', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'SOLFAC', 'name': 'define_it_42', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'SPOWDER', 'name': 'define_it_43', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'SZA', 'name': 'define_it_44', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'TAERST', 'name': 'define_it_45', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'TBAER', 'name': 'define_it_46', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'TCLOUD', 'name': 'define_it_47', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'TEMIS', 'name': 'define_it_48', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'TIME', 'name': 'define_it_49', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'TTEMP', 'name': 'define_it_50', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'UO3', 'name': 'define_it_51', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'UW', 'name': 'define_it_52', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'UZEN', 'name': 'define_it_53', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'VIS', 'name': 'define_it_54', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'VZEN', 'name': 'define_it_55', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'WBAER', 'name': 'define_it_56', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'WLBAER', 'name': 'define_it_57', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'WLINC', 'name': 'define_it_58', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'WLINF', 'name': 'define_it_59', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'WLSUP', 'name': 'define_it_60', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XCH4', 'name': 'define_it_61', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XCO', 'name': 'define_it_62', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XCO2', 'name': 'define_it_63', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XHNO3', 'name': 'define_it_64', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XN2', 'name': 'define_it_65', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XN2O', 'name': 'define_it_66', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XNH3', 'name': 'define_it_67', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XNO', 'name': 'define_it_68', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XNO2', 'name': 'define_it_69', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XO2', 'name': 'define_it_70', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XO4', 'name': 'define_it_71', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XRSC', 'name': 'define_it_72', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'XSO2', 'name': 'define_it_73', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ZAER', 'name': 'define_it_74', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ZBAER', 'name': 'define_it_75', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ZCLOUD', 'name': 'define_it_76', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ZGRID1', 'name': 'define_it_77', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ZGRID2', 'name': 'define_it_78', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ZOUT', 'name': 'define_it_79', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ZPRES', 'name': 'define_it_80', 'category': 'not_selected', 'description': 'get it from documentation'},
    {'abb': 'ZTRP', 'name': 'define_it_81', 'category': 'not_selected', 'description': 'get it from documentation'},
    ]
    return param_descriptions.copy()

_pdt = get_param_descriptions()
param_descriptions_abb = [i['abb'] for i in _pdt]
param_descriptions_name = [i['name'] for i in _pdt]

class Parameter(object):
    def __init__(self, abb, what, para_dict_list):
        if what == 'abb':
            self._dict = para_dict_list[param_descriptions_abb.index(abb)]
        elif what == 'name':
            self._dict = para_dict_list[param_descriptions_name.index(abb)]

    def reset2default(self):
        self._dict['value'] = self._dict['value_default']

    def set_value(self, value):
        self._dict['value'] = value

    def __repr__(self):
        return str(self._dict['value'])


def generate_parameter_class(what, stdout=True, save_folder='/Users/htelg/prog/sbdart-py/sbdart_py/'):
    txt = ['from sbdart_py.parameters import Parameter',
           '',
           'class Parameters_%s(object):' % what,
           '    def __init__(self,para_dict_list):',
           '        self.para_dict_list = para_dict_list',
           '',
           ''
           ]
    joined = '\n'.join(txt)
    if stdout:
        print(joined)

    if save_folder:
        fname = save_folder + '_parameter_class_' + what + '.py'
        raus = open(fname, 'w')
        raus.write(joined)
    for par in param_descriptions:
        value = par[what]
        txt = ['    @property',
               '    def %s(self):' % value,
               '        return Parameter("%s", "%s", self.para_dict_list)' % (value, what),
               '',
               '    @%s.setter' % value,
               '    def %s(self,value):' % value,
               '        Parameter("%s", "%s", self.para_dict_list).set_value(value)' % (value, what),
               '',
               '']
        joined = '\n'.join(txt)
        if stdout:
            print(joined)
        if save_folder:
            raus.write(joined)

    if save_folder:
        raus.close()
