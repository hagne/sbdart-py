from _parameters import param_descriptions, param_descriptions_abb, param_descriptions_name
from _parameters_class_abb import Parameters_abb
from _parameters_class_name import Parameters_name

class SbDart(object):
    def __init__(self):
        self.__std_input = None
        self.__inputs_orig = None
        self.__inputs_name = None
        pass

    @property
    def inputs_by_name(self):
        if not self.__inputs_name:
            parameters_name = Parameters_name()
            self.attach_names(parameters_name)
            self.__inputs_name = parameters_name
        return self.__inputs_name

    def attach_names(self, parameters):
        ### attache the origina abbriviation to params
        for parm in param_descriptions:
            #     break
            para_name_visible = parm['name']
            para_name = parm['abb']
            para_name_intern = '__%s' % para_name
            #     break
            para_value = getattr(self.std_input, para_name)
            setattr(Parameters_name, para_name_visible, ParamProperty(para_name_intern))
            setattr(parameters, para_name_visible, para_value)
            par = getattr(parameters, para_name_visible)
            setattr(par, '__default', para_value)
            setattr(par, '__type', type(para_value).__name__)

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

    def attach_abb(self, parameters):
        for parm in param_descriptions:
            #     break
            para_name = parm['abb']
            para_name_intern = '__%s' % para_name
            #     break
            para_value = getattr(std_input, para_name)
            setattr(Parameters_abb, para_name, ParamProperty(para_name_intern))
            setattr(parameters, para_name, para_value)
            par = getattr(parameters, para_name)
            setattr(par, '__default', para_value)
            setattr(par, '__type', type(para_value).__name__)

    def run_model(self):
        inputstr = '''&INPUT
 /'''
        inputf = open('INPUT', 'w')
        inputf.write(inputstr)
        inputf.close()

        process = subprocess.check_output('sbdart')
        self.result = process.decode()

        # remove INPUT file
        subprocess.call(['rm', 'INPUT'])
        return self.result