from sbdart_py.parameters import get_param_descriptions, param_descriptions_abb, param_descriptions_name
from sbdart_py._parameter_class_abb import Parameters_abb
from sbdart_py._parameter_class_name import Parameters_name
import numpy as _np
import subprocess as _subprocess


def read_default_parameters(para_dict, fname='standard_input.txt', return_object=True, manipulate_param_description=True):
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


class SbDart(object):
    def __init__(self):
        self.parameter_dict = get_param_descriptions()
        read_default_parameters(self.parameter_dict, return_object=False)
        self.__std_input = None
        self.__inputs_orig = None
        self.__inputs_name = None

        self.parameters_by_name = Parameters_name(self.parameter_dict)
        self.parameters_by_abb = Parameters_abb(self.parameter_dict)
        pass


    # @property
    # def inputs_by_name(self):
    #     if not self.__inputs_name:
    #         parameters_name = Parameters_name()
    #         self.attach_names(parameters_name)
    #         self.__inputs_name = parameters_name
    #     return self.__inputs_name

    # def attach_names(self, parameters):
    #     ### attache the origina abbriviation to params
    #     for parm in param_descriptions:
    #         #     break
    #         para_name_visible = parm['name']
    #         para_name = parm['abb']
    #         para_name_intern = '__%s' % para_name
    #         #     break
    #         para_value = getattr(self.std_input, para_name)
    #         setattr(Parameters_name, para_name_visible, ParamProperty(para_name_intern))
    #         setattr(parameters, para_name_visible, para_value)
    #         par = getattr(parameters, para_name_visible)
    #         setattr(par, '__default', para_value)
    #         setattr(par, '__type', type(para_value).__name__)

    # return parameters

    @property
    def std_input(self):
        if not self.__std_input:
            self.__std_input = read_default_parameters()
        return self.__std_input

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
        inputstr = '''&INPUT
 /'''
        inputf = open('INPUT', 'w')
        inputf.write(inputstr)
        inputf.close()

        process = _subprocess.check_output('sbdart')
        self.result = process.decode()

        # remove INPUT file
        _subprocess.call(['rm', 'INPUT'])
        return self.result