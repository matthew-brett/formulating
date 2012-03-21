# IPython log file

import formula as F
import pylab
url = 'http://stats191.stanford.edu/data/kidney.table'
import StringIO as StringIO
s=StringIO()
s=StringIO.StringIO()
import urllib
s.write(urllib.urlopen(url).read()); s.seek(0); X = pylab.csv2rec(s)
Xdtype
X.dtype
s.write(urllib.urlopen(url).read()); s.seek(0); X = pylab.csv2rec(s, delimiter='\t')
s=StringIO.StringIO()
s.write(urllib.urlopen(url).read()); s.seek(0); X = pylab.csv2rec(s, delimiter='\t')
X.dtype
s
s.getvalue()
s.seek(0)
s=StringIO.StringIO()
s.write(urllib.urlopen(url).read()); s.seek(0); X = pylab.csv2rec(s, delimiter=' ')
X
X.dtype
W = F.Factor('W', np.unique(X['weight'])
)
import numpy as np
W = F.Factor('W', np.unique(X['weight'])
)
D = F.Factor('D', np.unique(X['duration'])
)
D
W
f = W*D
f.terms
f.design(X)
D = F.Factor('duration', np.unique(X['duration'])
)
W = F.Factor('weight', np.unique(X['weight'])
)
f = W*D
f.design(X)
get_ipython().magic(u'pinfo f.design')
d, c = f.design(X, contrasts={'D':D.main_effect,'W':W.main_effect, 'D:W':D.main_effect*W.main_effect)
d, c = f.design(X, contrasts={'D':D.main_effect,'W':W.main_effect, 'D:W':D.main_effect*W.main_effect))
d, c = f.design(X, contrasts={'D':D.main_effect,'W':W.main_effect, 'D:W':D.main_effect*W.main_effect})
c['D']
c['W']
c['D:W']
D.get_term(1)
D
W
W1 = W.get_term(1); W2=W.get_term(2)
d, c = f.design(X, contrasts={'D':D.main_effect,'W':W.main_effect, 'D:W':D.main_effect*W.main_effect,'W1-W2':W1-W2})
c['W1-W2']
d.dtype
d, c = f.design(X, contrasts={'D':D.main_effect,'W':W.main_effect, 'D:W':D.main_effect*W.main_effect,'W1-W2':W1-W2}, return_float=False)
d.dtype
d, c = f.design(X, contrasts={'D':D.main_effect,'W':W.main_effect, 'D:W':D.main_effect*W.main_effect,'W1-W2':W1-W2})
D = f.design(X)
D.dtype
c['W1-W2']
W1-W2
X['weight']
Wnew=np.empty(X['weight'].shape, dtype=np.dtype(['wnew', '|S1']))
Wnew=np.empty(X['weight'].shape, dtype=np.dtype([('wnew', '|S1')]))
Wnew[X['weight']==1] ='A'
Wnew[X['weight']==2] ='A'
Wnew[X['weight']==3] ='B'
fWnew = F.Factor(Wnew, ['A','B'])
get_ipython().magic(u'logstart ')
get_ipython().magic(u'pycat ipython_log.py')
get_ipython().magic(u'pwd ')
