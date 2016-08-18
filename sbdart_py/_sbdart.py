from sbdart_py.parameters import get_param_descriptions, param_descriptions_abb
from sbdart_py._parameter_class_abb import Parameters_abb
from sbdart_py._parameter_class_name import Parameters_name
from sbdart_py._parameter_class_aerosols import Parameters_aerosols
from sbdart_py._parameter_class_output_format import Parameters_output_format
import numpy as _np
import subprocess as _subprocess
import io as _io
import pandas as _pd


output_cols_01 = [{'abb': 'WL',
                   'col': -1,
                   'name': 'wavelength',
                   'name_short': 'wavelength',
                   'unit': 'microns'},
                  {'abb': 'FFV',
                   'col': 0,
                   'name': 'filter function value',
                   'name_short': 'filter_value'},
                  {'abb': 'TOPDN',
                   'col': 2,
                   'name': 'total downward flux at ZOUT(2) km',
                   'name_short': 'total_down_2',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'TOPUP',
                   'col': 3,
                   'name': 'total upward flux at ZOUT(2) km',
                   'name_short': 'total_up_2',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'TOPDIR',
                   'col': 4,
                   'name': 'direct downward flux at ZOUT(2) km',
                   'name_short': 'direct_down_2',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'BOTDN',
                   'col': 5,
                   'name': 'total downward flux at ZOUT(1) km',
                   'name_short': 'total_down_1',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'BOTUP',
                   'col': 6,
                   'name': 'total upward flux at  ZOUT(1) km',
                   'name_short': 'total_up_1',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'BOTDIR',
                   'col': 7,
                   'name': 'direct downward flux at ZOUT(1) km',
                   'name_short': 'direct_down_1',
                   'unit': '(w/m2/micron)'}
                  ]

output_cols_sorted_01 = sorted(output_cols_01, key=lambda x: x['col'])

output_cols_10 = [{'abb': 'WLINF',
                   'col': -2,
                   'name': 'lower wavelength limit',
                   'name_short': 'wavelength_min',
                   'unit': 'microns'},
                  {'abb': 'WLSUP',
                   'col': -1,
                   'name': 'upper wavelength limit',
                   'name_short': 'wavelength_max',
                   'unit': 'microns'},
                  {'abb': 'FFEW',
                   'col': 0,
                   'name': 'filter function equivalent width',
                   'name_short': 'filter_width'},
                  {'abb': 'TOPDN',
                   'col': 2,
                   'name': 'total downward flux at ZOUT(2) km',
                   'name_short': 'total_down_2',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'TOPUP',
                   'col': 3,
                   'name': 'total upward flux at ZOUT(2) km',
                   'name_short': 'total_up_2',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'TOPDIR',
                   'col': 4,
                   'name': 'direct downward flux at ZOUT(2) km',
                   'name_short': 'direct_down_2',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'BOTDN',
                   'col': 5,
                   'name': 'total downward flux at ZOUT(1) km',
                   'name_short': 'total_down_1',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'BOTUP',
                   'col': 6,
                   'name': 'total upward flux at  ZOUT(1) km',
                   'name_short': 'total_up_1',
                   'unit': '(w/m2/micron)'},
                  {'abb': 'BOTDIR',
                   'col': 7,
                   'name': 'direct downward flux at ZOUT(1) km',
                   'name_short': 'direct_down_1',
                   'unit': '(w/m2/micron)'}
                  ]

output_cols_sorted_10 = sorted(output_cols_10, key=lambda x: x['col'])

def _read_default_parameters(para_dict, fname='standard_input.txt', return_object=True, manipulate_param_description=True):
    std_input = type('StandardInputs', (object,), {'__doc__': 'class containing standart inputs'})

    para_list = []

    rein = open(fname, 'r')
    standard_input = rein.read()
    rein.close()

    result_lines = standard_input.split('\n')[1:]
    for e, line in enumerate(result_lines):
        if '/' in line:
            break
        if '=' not in line:
            vt = line.replace(',', '').strip()
            try:
                value = eval(vt)
            except NameError:
                value = vt
                #         print(value, type(value).__name__)
            para_list.append(value)
        else:
            if len(para_list) > 1:
                setattr(std_input, att_name, _np.array(para_list))
                if manipulate_param_description:
                    para_dict[param_descriptions_abb.index(att_name)]['value'] = _np.array(para_list)
                    para_dict[param_descriptions_abb.index(att_name)]['value_default'] = _np.array(para_list)
                    #             break
            param = line.replace(',', '').strip().split('=')
            att_name = param[0].strip()

            try:
                att_value = eval(param[1])
            except NameError:
                att_value = param[1]

            setattr(std_input, att_name, att_value)
            if manipulate_param_description:
                para_dict[param_descriptions_abb.index(att_name)]['value'] = att_value
                para_dict[param_descriptions_abb.index(att_name)]['value_default'] = att_value
            para_list = [att_value]

    if return_object:
        return std_input

def _translate_output(rtm, out_str):
    if rtm.parameters_by_category.output_format.output_format == 1:
        skip_lines = 3
        index_col = 0
        startcol = 1
        output_cols = output_cols_01
        column_names = [i['name_short'] for i in output_cols_sorted_01]

    elif rtm.parameters_by_category.output_format.output_format == 10:
        skip_lines = 0
        index_col = None
        startcol = 0
        output_cols = output_cols_10
        column_names = [i['name_short'] for i in output_cols_sorted_10]

    linelist = [','.join(i.split()) for i in out_str.split('\n')]

    out_csv = '\n'.join(linelist[skip_lines:])

    out_buff = _io.StringIO(out_csv)
    df_out = _pd.read_csv(out_buff,
                          sep = ',',
                          index_col=index_col,
                          names = column_names
                          )
    return df_out

class SbDart(object):
    def __init__(self):
        self.parameter_dict = get_param_descriptions()
        _read_default_parameters(self.parameter_dict, return_object=False)
        # self.__std_input = None
        self.__inputs_orig = None
        self.__inputs_name = None

        self.parameters_by_name = Parameters_name(self.parameter_dict)
        self.parameters_by_abb = Parameters_abb(self.parameter_dict)
        self.parameters_by_category = type('Parameters_by_category', (object,), {'aerosols': Parameters_aerosols(self.parameter_dict),
                                                                                 'output_format': Parameters_output_format(self.parameter_dict),
                                                                                 })

    # @property
    # def std_input(self):
    #     if not self.__std_input:
    #         self.__std_input = _read_default_parameters()
    #     return self.__std_input

    @property
    def inputs_original(self):
        if not self.__inputs_orig:
            parameters_abb = Parameters_abb()
            self.attach_abb(parameters_abb)
            self.__inputs_orig = parameters_abb
        return self.__inputs_orig

    # def attach_abb(self, parameters):
    #     for parm in param_descriptions:
    #         #     break
    #         para_name = parm['abb']
    #         para_name_intern = '__%s' % para_name
    #         #     break
    #         para_value = getattr(std_input, para_name)
    #         setattr(Parameters_abb, para_name, ParamProperty(para_name_intern))
    #         setattr(parameters, para_name, para_value)
    #         par = getattr(parameters, para_name)
    #         setattr(par, '__default', para_value)
    #         setattr(par, '__type', type(para_value).__name__)

    def run_model(self):
 #        inputstr = '''&INPUT
 # /'''


        input_list = []
        for para in self.parameter_dict:
            if _np.all(para['value'] == para['value_default']):
                continue
            para_str = '='.join([para['abb'], str(para['value'])])
            input_list.append(para_str)

        body = '    ' + ',\n    '.join(input_list)
        firstline = '&INPUT'
        lastline = '/'
        inputstr = '\n'.join([firstline, body, lastline])


        inputf = open('INPUT', 'w')
        inputf.write(inputstr)
        inputf.close()

        process = _subprocess.check_output('sbdart')
        self.result = _translate_output(self, process.decode())

        # remove INPUT file
        _subprocess.call(['rm', 'INPUT'])
        return self.result