class feducial:
    """Class for feducials, store gate sequence and counts feducials constructed and gives each an index"""
    _counter=0
    def __init__(self,gate_seq):
        self._gate_seq=gate_seq
        self._index=type(self)._counter
        type(self)._counter+=1
    def __repr__(self):
        return "F_"+str(self._index)+": "+self._gate_seq
    def get_index(self):
        return self._index
    def get_gate_seq(self):
        return self._gate_seq

class gst:
    """Base class for going gst, (add more doc later)"""
    def __init__(self,gates):
        try:
            self._gates=list(map(str,gates))
        except:
            raise ValueError("can't make list of string out of input")
        self._feducials=None
        self._exp_data=None
        self._MS=None
        self._rho_tilde=None
        self._rho_hat=None
        self._G_tilde=None
        self._G_hat=None
    def __repr__(self):
        return "GST-class with base-gates "+str(self._gates)
    def read_data(self,filename):
        """Reads the data from file 'filename'. First lines should be feducials and then seperated by an empty line the experimental runs"""
        self._feducials=[]
        self._exp_data=[]
        feducial._counter=0
        with open(filename) as file:
            line='-1'
            while True: #read feducials
                line=file.readline()
                if line=='' or line=='\n': #test for empty line to prevent inifinite loop if format is wrong
                    break
                self._feducials.append(feducial(line[:-1]))
            while True: #read exp_data
                line=file.readline()
                if line=='':
                    break
                tmp_data=line.split(' ')
                tmp_data[1]=int(tmp_data[1]) #probability 1
                tmp_data[2]=int(tmp_data[2]) #probability 2
                self._exp_data.append(tuple(tmp_data))
    def get_feducials(self):
        return self._feducials
    def get_gates(self):
        return self._gates
    def get_exp_data(self):
        return self._exp_data
